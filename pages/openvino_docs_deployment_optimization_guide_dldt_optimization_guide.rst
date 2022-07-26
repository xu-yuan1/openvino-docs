.. index:: pair: page; Runtime Inference Optimizations
.. _doxid-openvino_docs_deployment_optimization_guide_dldt_optimization_guide:


Runtime Inference Optimizations
===============================

:target:`doxid-openvino_docs_deployment_optimization_guide_dldt_optimization_guide_1md_openvino_docs_optimization_guide_dldt_deployment_optimization_guide`





.. toctree::
   :maxdepth: 1
   :hidden:

   openvino_docs_deployment_optimization_guide_common
   openvino_docs_deployment_optimization_guide_latency
   openvino_docs_deployment_optimization_guide_tput
   openvino_docs_deployment_optimization_guide_tput_advanced
   openvino_docs_deployment_optimization_guide_internals

Runtime optimizations, or deployment optimizations, focus on tuning inference parameters and execution means (e.g., the optimum number of requests executed simultaneously). Unlike model-level optimizations, they are highly specific to the hardware and case they are used for, and often come at a cost. ``:ref:`ov::hint::inference_precision <doxid-group__ov__runtime__cpp__prop__api_1gad605a888f3c9b7598ab55023fbf44240>``` is a "typical runtime configuration" which trades accuracy for performance, allowing ``fp16/bf16`` execution for the layers that remain in ``fp32`` after quantization of the original ``fp32`` model.

Therefore, optimization should start with defining the use case. For example, if it is about processing millions of samples by overnight jobs in data centers, throughput could be prioritized over latency. On the other hand, real-time usages would likely trade off throughput to deliver the results at minimal latency. A combined scenario is also possible, targeting the highest possible throughput, while maintaining a specific latency threshold.

It is also important to understand how the full-stack application would use the inference component "end-to-end." For example, to know what stages need to be orchestrated to save workload devoted to fetching and preparing input data.

For more information on this topic, see the following articles:

* :ref:`feature support by device <doxid-openvino_docs__o_v__u_g__working_with_devices_1features_support_matrix>`,

* :ref:`Inputs Pre-processing with the OpenVINO <doxid-openvino_docs_deployment_optimization_guide_common_1inputs_pre_processing>`.

* :ref:`Async API <doxid-openvino_docs_deployment_optimization_guide_common_1async_api>`.

* :ref:`The 'get_tensor' Idiom <doxid-openvino_docs_deployment_optimization_guide_common_1tensor_idiom>`.

* For variably-sized inputs, consider :ref:`dynamic shapes <doxid-openvino_docs__o_v__u_g__dynamic_shapes>`.

See the :ref:`latency <doxid-openvino_docs_deployment_optimization_guide_latency>` and :ref:`throughput <doxid-openvino_docs_deployment_optimization_guide_tput>` optimization guides, for **use-case-specific optimizations**

Writing Performance-Portable Inference Applications
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Although inference performed in OpenVINO Runtime can be configured with a multitude of low-level performance settings, it is not recommended in most cases. Firstly, achieving the best performance with such adjustments requires deep understanding of device architecture and the inference engine.

Secondly, such optimization may not translate well to other device-model combinations. In other words, one set of execution parameters is likely to result in different performance when used under different conditions. For example:

* both the CPU and GPU support the notion of :ref:`streams <doxid-openvino_docs_deployment_optimization_guide_tput_advanced>`, yet they deduce their optimal number very differently.

* Even among devices of the same type, different execution configurations can be considered optimal, as in the case of instruction sets or the number of cores for the CPU and the batch size for the GPU.

* Different models have different optimal parameter configurations, considering factors such as compute vs memory-bandwidth, inference precision, and possible model quantization.

* Execution "scheduling" impacts performance strongly and is highly device-specific, for example, GPU-oriented optimizations like batching, combining multiple inputs to achieve the optimal throughput, :ref:`do not always map well to the CPU <doxid-openvino_docs_deployment_optimization_guide_internals>`.

To make the configuration process much easier and its performance optimization more portable, the option of :ref:`Performance Hints <doxid-openvino_docs__o_v__u_g__performance__hints>` has been introduced. It comprises two high-level "presets" focused on either **latency** or **throughput** and, essentially, makes execution specifics irrelevant.

The Performance Hints functionality makes configuration transparent to the application, for example, anticipates the need for explicit (application-side) batching or streams, and facilitates parallel processing of separate infer requests for different input sources

Additional Resources
~~~~~~~~~~~~~~~~~~~~

* :ref:`Using Async API and running multiple inference requests in parallel to leverage throughput <doxid-openvino_docs_deployment_optimization_guide_tput_1throughput_app_design>`.

* :ref:`The throughput approach implementation details for specific devices <doxid-openvino_docs_deployment_optimization_guide_internals>`

* :ref:`Details on throughput <doxid-openvino_docs_deployment_optimization_guide_tput>`

* :ref:`Details on latency <doxid-openvino_docs_deployment_optimization_guide_latency>`

* :ref:`API examples and details <doxid-openvino_docs__o_v__u_g__performance__hints>`.

