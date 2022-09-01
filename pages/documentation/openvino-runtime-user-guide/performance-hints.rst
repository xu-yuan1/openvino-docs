.. index:: pair: page; High-level Performance Hints
.. _deploy_infer__performance_hints:

.. meta::
   :description: OpenVINO Runtime offers two dedicated high-level performance 
                 hints, namely throughput and latency, that help to configure 
                 an inference device.
   :keywords: OpenVINO Runtime, performance hints, high-level performance hints,
              device configuration, inference device, inference, model inference, 
              performance mode, latency, throughput, analyze performance, 
              increase performance, benchmark_app, device-specific configuration, 
              Compiled_Model, basic API, performance settings, batch size, 
              device configuration, Intel CPU, Intel GPU, latency hint, 
              throughput hint, num_requests, parallel inference requests,
              Async API, Asynchronous API, portability

High-level Performance Hints
============================

:target:`deploy_infer__performance_hints_1md_openvino_docs_ov_runtime_ug_performance_hints` 

Even though all :ref:`supported devices <deploy_infer__working_with_devices>` in OpenVINO™ offer low-level performance settings, utilizing them is not recommended outside of very few cases. The preferred way to configure performance in OpenVINO Runtime is using performance hints. This is a future-proof solution fully compatible with the :ref:`automatic device selection inference mode <deploy_infer__auto_plugin>` and designed with *portability* in mind.

The hints also set the direction of the configuration in the right order. Instead of mapping the application needs to the low-level performance settings, and keeping an associated application logic to configure each possible device separately, the hints express a target scenario with a single config key and let the *device* configure itself in response.

Previously, a certain level of automatic configuration was the result of the *default* values of the parameters. For example, the number of CPU streams was deduced from the number of CPU cores, when ``:ref:`ov::streams::AUTO <doxid-group__ov__runtime__cpp__prop__api_1gaddb29425af71fbb6ad3379c59342ff0e>``` (``CPU_THROUGHPUT_AUTO`` in the pre-API 2.0 terminology) was set. However, the resulting number of streams did not account for actual compute requirements of the model to be inferred. The hints, in contrast, respect the actual model, so the parameters for optimal throughput are calculated for each model individually (based on its compute versus memory bandwidth requirements and capabilities of the device).

Performance Hints: Latency and Throughput
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

As discussed in the :ref:`Optimization Guide <performance_optimization_guide_introduction>` there are a few different metrics associated with inference speed. Throughput and latency are some of the most widely used metrics that measure the overall performance of an application.

Therefore, in order to ease the configuration of the device, OpenVINO offers two dedicated hints, namely ``:ref:`ov::hint::PerformanceMode::THROUGHPUT <doxid-group__ov__runtime__cpp__prop__api_1gga032aa530efa40760b79af14913d48d73a50f9b1f40c078d242af7ec323ace44b3>``` and ``:ref:`ov::hint::PerformanceMode::LATENCY <doxid-group__ov__runtime__cpp__prop__api_1gga032aa530efa40760b79af14913d48d73a501069dd75f76384ba18f133fdce99c2>```. A special ``:ref:`ov::hint::PerformanceMode::UNDEFINED <doxid-group__ov__runtime__cpp__prop__api_1gga032aa530efa40760b79af14913d48d73a0db45d2a4141101bdfe48e3314cfbca3>``` hint acts the same as specifying no hint.

For more information on conducting performance measurements with the ``benchmark_app``, refer to the last section in this document.

Keep in mind that a typical model may take significantly more time to load with the ``:ref:`ov::hint::PerformanceMode::THROUGHPUT <doxid-group__ov__runtime__cpp__prop__api_1gga032aa530efa40760b79af14913d48d73a50f9b1f40c078d242af7ec323ace44b3>``` and consume much more memory, compared to the ``:ref:`ov::hint::PerformanceMode::LATENCY <doxid-group__ov__runtime__cpp__prop__api_1gga032aa530efa40760b79af14913d48d73a501069dd75f76384ba18f133fdce99c2>```.

Performance Hints: How It Works
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Internally, every device "translates" the value of the hint to the actual performance settings. For example, the ``:ref:`ov::hint::PerformanceMode::THROUGHPUT <doxid-group__ov__runtime__cpp__prop__api_1gga032aa530efa40760b79af14913d48d73a50f9b1f40c078d242af7ec323ace44b3>``` selects the number of CPU or GPU streams. Additionally, the optimal batch size is selected for the GPU and the :ref:`automatic batching <deploy_infer__automatic_batching>` is applied whenever possible. To check whether the device supports it, refer to the :ref:`devices/features support matrix <deploy_infer__working_with_devices>` article.

The resulting (device-specific) settings can be queried back from the instance of the ``ov:Compiled_Model``.

Be aware that the ``benchmark_app`` outputs the actual settings for the ``THROUGHPUT`` hint. See the example of the output below:

.. ref-code-block:: cpp

	$benchmark_app -hint tput -d CPU -m 'path to your favorite model'
	...
	[Step 8/11] Setting optimal runtime parameters
	[ INFO ] Device: CPU
	[ INFO ]   { PERFORMANCE_HINT , THROUGHPUT }
	...
	[ INFO ]   { OPTIMAL_NUMBER_OF_INFER_REQUESTS , 4 }
	[ INFO ]   { NUM_STREAMS , 4 }
	...

Using the Performance Hints: Basic API
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In the example code snippet below, ``:ref:`ov::hint::PerformanceMode::THROUGHPUT <doxid-group__ov__runtime__cpp__prop__api_1gga032aa530efa40760b79af14913d48d73a50f9b1f40c078d242af7ec323ace44b3>``` is specified for the ``:ref:`ov::hint::performance_mode <doxid-group__ov__runtime__cpp__prop__api_1ga2691fe27acc8aa1d1700ad40b6da3ba2>``` property for ``compile_model`` :





.. tab:: C++

    .. doxygensnippet:: ../../snippets/ov_auto_batching.cpp
       :language: cpp
       :fragment: [compile_model]

.. tab:: Python

    .. doxygensnippet:: ../../snippets/ov_auto_batching.py
       :language: python
       :fragment: [compile_model]

Additional (Optional) Hints from the App
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For an application that processes 4 video streams, the most future-proof way to communicate the limitation of the parallel slack is to equip the performance hint with the optional ``ov::hint::num_requests`` configuration key set to 4. As mentioned earlier, this will limit the batch size for the GPU and the number of inference streams for the CPU. Thus, each device uses the ``ov::hint::num_requests`` while converting the hint to the actual device configuration options:





.. tab:: C++

    .. doxygensnippet:: ../../snippets/ov_auto_batching.cpp
       :language: cpp
       :fragment: [hint_num_requests]

.. tab:: Python

    .. doxygensnippet:: ../../snippets/ov_auto_batching.py
       :language: python
       :fragment: [hint_num_requests]

Optimal Number of Inference Requests
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The hints are used on the presumption that the application queries ``:ref:`ov::optimal_number_of_infer_requests <doxid-group__ov__runtime__cpp__prop__api_1ga087c6da667f7c3d8374aec5f6cbba027>``` to create and run the returned number of requests simultaneously:





.. tab:: C++

    .. doxygensnippet:: ../../snippets/ov_auto_batching.cpp
       :language: cpp
       :fragment: [query_optimal_num_requests]

.. tab:: Python

    .. doxygensnippet:: ../../snippets/ov_auto_batching.py
       :language: python
       :fragment: [query_optimal_num_requests]

While an application is free to create more requests if needed (for example to support asynchronous inputs population) it is very important to at least run the ``:ref:`ov::optimal_number_of_infer_requests <doxid-group__ov__runtime__cpp__prop__api_1ga087c6da667f7c3d8374aec5f6cbba027>``` of the inference requests in parallel. It is recommended for efficiency, or device utilization, reasons.

Keep in mind that ``:ref:`ov::hint::PerformanceMode::LATENCY <doxid-group__ov__runtime__cpp__prop__api_1gga032aa530efa40760b79af14913d48d73a501069dd75f76384ba18f133fdce99c2>``` does not necessarily imply using single inference request. For example, multi-socket CPUs can deliver as many requests at the same minimal latency as the number of NUMA nodes in the system. To make your application fully scalable, make sure to query the ``:ref:`ov::optimal_number_of_infer_requests <doxid-group__ov__runtime__cpp__prop__api_1ga087c6da667f7c3d8374aec5f6cbba027>``` directly.

Prefer Async API
~~~~~~~~~~~~~~~~

The API of the inference requests offers Sync and Async execution. The ``:ref:`ov::InferRequest::infer() <doxid-classov_1_1_infer_request_1abcb7facc9f7c4b9226a1fd343e56958d>``` is inherently synchronous and simple to operate (as it serializes the execution flow in the current application thread). The Async "splits" the ``infer()`` into ``:ref:`ov::InferRequest::start_async() <doxid-classov_1_1_infer_request_1a5a05ae4352f804c865e11f5d68b983d5>``` and ``:ref:`ov::InferRequest::wait() <doxid-classov_1_1_infer_request_1ab0e0739da45789d816f8b5584a0b5691>``` (or callbacks). For more information, refer to the :ref:`API examples <deploy_infer__inference_request>`. Although the Synchronous API can be somewhat easier to start with, it is recommended to use the Asynchronous (callbacks-based) API in the production code. It is the most general and scalable way to implement the flow control for any possible number of requests (and thus both latency and throughput scenarios).

Combining the Hints and Individual Low-Level Settings
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

While sacrificing the portability to some extent, it is possible to combine the hints with individual device-specific settings. For example, use ``:ref:`ov::hint::PerformanceMode::THROUGHPUT <doxid-group__ov__runtime__cpp__prop__api_1gga032aa530efa40760b79af14913d48d73a50f9b1f40c078d242af7ec323ace44b3>``` to prepare a general configuration and override any of its specific values:







.. tab:: C++

    .. doxygensnippet:: ../../snippets/ov_auto_batching.cpp
       :language: cpp
       :fragment: [hint_plus_low_level]

.. tab:: Python

    .. doxygensnippet:: ../../snippets/ov_auto_batching.py
       :language: python
       :fragment: [hint_plus_low_level]

Testing Performance of the Hints with the Benchmark_App
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The ``benchmark_app``, that exists in both :ref:`C++ <doxid-openvino_inference_engine_samples_benchmark_app__r_e_a_d_m_e>` and :ref:`Python <doxid-openvino_inference_engine_tools_benchmark_tool__r_e_a_d_m_e>` versions, is the best way to evaluate the functionality of the performance hints for a particular device:

* benchmark_app **-hint tput** -d 'device' -m 'path to your model'

* benchmark_app **-hint latency** -d 'device' -m 'path to your model'

Disabling the hints to emulate the pre-hints era (highly recommended before trying the individual low-level settings, such as the number of streams as below, threads, etc):

* - benchmark_app **-hint none -nstreams 1** -d 'device' -m 'path to your model'

See Also
--------

:ref:`Supported Devices <doxid-openvino_docs__o_v__u_g_supported_plugins__supported__devices>`

