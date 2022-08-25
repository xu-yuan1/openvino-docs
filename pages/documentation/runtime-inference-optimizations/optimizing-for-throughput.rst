.. index:: pair: page; Optimizing for Throughput
.. _deployment_optimizing_for_throughput:

.. meta::
   :description: Throughput-oriented approaches in OpenVINO involve 
                 execution of a large number of inference requests 
                 simultaneously which improves the device utilization.
   :keywords: OpenVINO, throughput, Performance Hints, 
              model inference, high-level performance hints, inference
              mode, improving throughput, multi-device execution, 
              Asynchronous API, callbacks, inference request, compile_model,
              optimal_number_of_infer_requests

Optimizing for Throughput
=========================

:target:`deployment_optimizing_for_throughput_1md_openvino_docs_optimization_guide_dldt_deployment_optimization_tput` 

As described in the section on the :ref:`latency-specific considerations <deployment_optimizing_for_latency>`, 
one of the possible use cases is *delivering every single request at the 
minimal delay*. Throughput, on the other hand, is about inference scenarios in 
which potentially **large number of inference requests are served 
simultaneously to improve the device utilization**.

The associated increase in latency is not linearly dependent on the number of 
requests executed in parallel. A trade-off between overall throughput and 
serial performance of individual requests can be achieved with the right 
performance configuration of OpenVINO.

Basic and Advanced Ways of Leveraging Throughput
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

There are two ways of leveraging throughput with individual devices:

* **Basic (high-level)** flow with :ref:`OpenVINO performance hints <doxid-openvino_docs__o_v__u_g__performance__hints>` 
  which is inherently **portable and future-proof**.

* **Advanced (low-level)** approach of explicit **batching** and **streams**. 
  For more details, see the :ref:`runtime inference optimizations <deployment_throughput_advanced>`.

In both cases, the application should be designed to execute multiple inference 
requests in parallel, as described in the following section.

:target:`deployment_optimizing_for_throughput_1throughput_app_design`

Throughput-Oriented Application Design
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In general, most throughput-oriented inference applications should:

* Expose substantial amounts of *input* parallelism (e.g. process multiple 
  video- or audio- sources, text documents, etc).

* Decompose the data flow into a collection of concurrent inference requests 
  that are aggressively scheduled to be executed in parallel:
  
  * Setup the configuration for the *device* (for example, as parameters of 
    the ``:ref:`ov::Core::compile_model <doxid-classov_1_1_core_1a46555f0803e8c29524626be08e7f5c5a>```) 
    via either previously introduced :ref:`low-level explicit options <deployment_throughput_advanced>` 
    or :ref:`OpenVINO performance hints <doxid-openvino_docs__o_v__u_g__performance__hints>` (**preferable**):

    .. tab:: C++

       .. doxygensnippet:: ../../snippets/ov_auto_batching.cpp
          :language: cpp
          :fragment: [compile_model]

    .. tab:: Python

       .. doxygensnippet:: ../../snippets/ov_auto_batching.py
          :language: python
          :fragment: [compile_model]

  * Query the ``:ref:`ov::optimal_number_of_infer_requests <doxid-group__ov__runtime__cpp__prop__api_1ga087c6da667f7c3d8374aec5f6cbba027>``` 
    from the ``:ref:`ov::CompiledModel <doxid-classov_1_1_compiled_model>``` 
    (resulted from a compilation of the model for the device) to create the 
    number of the requests required to saturate the device.

* Use the Async API with callbacks, to avoid any dependency on the completion 
  order of the requests and possible device starvation, as explained in the 
  :ref:`common-optimizations section <deployment_general_optimizations>`.

Multi-Device Execution
~~~~~~~~~~~~~~~~~~~~~~

OpenVINO offers the automatic, scalable :ref:`multi-device inference mode <doxid-openvino_docs__o_v__u_g__running_on_multiple_devices>`, 
which is a simple *application-transparent* way to improve throughput. There 
is no need to re-architecture existing applications for any explicit multi-device 
support: no explicit network loading to each device, no separate per-device queues, 
no additional logic to balance inference requests between devices, etc. For the 
application using it, multi-device is like any other device, as it manages all 
processes internally. Just like with other throughput-oriented scenarios, there 
are several major pre-requisites for optimal multi-device performance:

* Using the :ref:`Asynchronous API <deployment_general_optimizations_1async_api>` 
  and :ref:`callbacks <openvino_inference_request>` in particular.

* Providing the multi-device (and hence the underlying devices) with enough 
  data to crunch. As the inference requests are naturally independent data pieces, 
  the multi-device performs load-balancing at the "requests" (outermost) level 
  to minimize the scheduling overhead.

Keep in mind that the resulting performance is usually a fraction of the 
"ideal" (plain sum) value, when the devices compete for certain resources such 
as the memory-bandwidth, which is shared between CPU and iGPU.

.. note:: While the legacy approach of optimizing the parameters of each device 
   separately works, the :ref:`OpenVINO performance hints <doxid-openvino_docs__o_v__u_g__performance__hints>` 
   allow configuring all devices (that are part of the specific multi-device configuration) at once.
