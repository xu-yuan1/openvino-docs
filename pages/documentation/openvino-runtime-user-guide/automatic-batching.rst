.. index:: pair: page; Automatic Batching
.. _doxid-openvino_docs__o_v__u_g__automatic__batching:


Automatic Batching
==================

:target:`doxid-openvino_docs__o_v__u_g__automatic__batching_1md_openvino_docs_ov_runtime_ug_automatic_batching` 

The Automatic Batching Execution mode (or Auto-batching for short) performs automatic 
batching on-the-fly to improve device utilization by grouping inference requests 
together, with no programming effort from the user. With Automatic Batching, gathering 
the input and scattering the output from the individual inference requests required 
for the batch happen transparently, without affecting the application code.

This article provides a preview of the new Automatic Batching function, including 
how it works, its configurations, and testing performance.

Enabling/Disabling Automatic Batching
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Auto-batching primarily targets the existing code written for inferencing many 
requests, each instance with the batch size 1. To obtain corresponding performance 
improvements, the application **must be running many inference requests simultaneously**. 
Auto-batching can also be used via a particular *virtual* device.

Batching is a straightforward way of leveraging the compute power of GPU and saving 
on communication overheads. Automatic Batching is "implicitly" triggered on the GPU 
when ``:ref:`ov::hint::PerformanceMode::THROUGHPUT <doxid-group__ov__runtime__cpp__prop__api_1gga032aa530efa40760b79af14913d48d73a50f9b1f40c078d242af7ec323ace44b3>``` 
is specified for the ``:ref:`ov::hint::performance_mode <doxid-group__ov__runtime__cpp__prop__api_1ga2691fe27acc8aa1d1700ad40b6da3ba2>``` 
property for the ``compile_model`` or ``set_property`` calls.

.. tab:: C++

   .. ref-code-block:: cpp

      auto compiled_model = core.compile_model(:ref:`model <doxid-group__ov__runtime__cpp__prop__api_1ga461856fdfb6d7533dc53355aec9e9fad>`, "GPU",
         :ref:`ov::hint::performance_mode <doxid-group__ov__runtime__cpp__prop__api_1ga2691fe27acc8aa1d1700ad40b6da3ba2>`(:ref:`ov::hint::PerformanceMode::THROUGHPUT <doxid-group__ov__runtime__cpp__prop__api_1gga032aa530efa40760b79af14913d48d73a50f9b1f40c078d242af7ec323ace44b3>`));

.. tab:: Python

   .. ref-code-block:: cpp

      config = {"PERFORMANCE_HINT": "THROUGHPUT"}
      compiled_model = core.compile_model(model, "GPU", config)


To enable Auto-batching in the legacy apps not akin to the notion of performance 
hints, you need to use the **explicit** device notion, such as ``BATCH:GPU``.

Disabling Automatic Batching
----------------------------

Auto-Batching can be disabled (for example, for the GPU device) to prevent being triggered by 
``:ref:`ov::hint::PerformanceMode::THROUGHPUT <doxid-group__ov__runtime__cpp__prop__api_1gga032aa530efa40760b79af14913d48d73a50f9b1f40c078d242af7ec323ace44b3>```. 
To do that, set ``:ref:`ov::hint::allow_auto_batching <doxid-group__ov__runtime__cpp__prop__api_1ga445a111e7219955c585eb418d2f4f80d>``` 
to **false** in addition to the ``:ref:`ov::hint::performance_mode <doxid-group__ov__runtime__cpp__prop__api_1ga2691fe27acc8aa1d1700ad40b6da3ba2>```, 
as shown below:

.. tab:: C++

   .. ref-code-block:: cpp

      // disabling the automatic batching
      // leaving intact other configurations options that the device selects for the 'throughput' hint 
      auto compiled_model = core.compile_model(:ref:`model <doxid-group__ov__runtime__cpp__prop__api_1ga461856fdfb6d7533dc53355aec9e9fad>`, "GPU", 
         :ref:`ov::hint::performance_mode <doxid-group__ov__runtime__cpp__prop__api_1ga2691fe27acc8aa1d1700ad40b6da3ba2>`(:ref:`ov::hint::PerformanceMode::THROUGHPUT <doxid-group__ov__runtime__cpp__prop__api_1gga032aa530efa40760b79af14913d48d73a50f9b1f40c078d242af7ec323ace44b3>`),
         :ref:`ov::hint::allow_auto_batching <doxid-group__ov__runtime__cpp__prop__api_1ga445a111e7219955c585eb418d2f4f80d>`(false));

.. tab:: Python

   .. ref-code-block:: cpp

      # disabling the automatic batching
      # leaving intact other configurations options that the device selects for the 'throughput' hint 
      config = {"PERFORMANCE_HINT": "THROUGHPUT",
               "ALLOW_AUTO_BATCHING": False}
      compiled_model = core.compile_model(model, "GPU", config)


Configuring Automatic Batching
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Following the OpenVINO naming convention, the *batching* device is assigned the label 
of *BATCH*. The configuration options are as follows:

+----------------------------+-----------------------------------------------------+------------------------------------------------------------+
| Parameter name             |            Parameter description                    | Examples                                                   |
+============================+=====================================================+============================================================+
| ``AUTO_BATCH_DEVICE``      | The name of the device to apply Automatic batching, | ``BATCH:GPU`` triggers the automatic batch size selection. |
|                            | with the optional batch size value in brackets.     |                                                            |
+----------------------------+-----------------------------------------------------+------------------------------------------------------------+
| ``ov::auto_batch_timeout`` | The timeout value, in ms. (1000 by default)         | You can reduce the timeout value to avoid performance      |
|                            |                                                     | penalty when the data arrives too unevenly).               |
|                            |                                                     | For example, set it to "100", or the contrary, i.e.,       |
|                            |                                                     | make it large enough to accommodate input                  |
|                            |                                                     | preparation (e.g. when it is a serial process).            |
+----------------------------+-----------------------------------------------------+------------------------------------------------------------+

Automatic Batch Size Selection
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In both the THROUGHPUT hint and the explicit BATCH device cases, the optimal batch 
size is selected automatically, as the implementation queries the 
``:ref:`ov::optimal_batch_size <doxid-group__ov__runtime__cpp__prop__api_1ga129bad2da2fc2a40a7d746d86fc9c68d>``` 
property from the device and passes the model graph as the parameter. The actual 
value depends on the model and device specifics, for example, the on-device memory 
for dGPUs. The support for Auto-batching is not limited to GPU. However, if a device does 
not support ``:ref:`ov::optimal_batch_size <doxid-group__ov__runtime__cpp__prop__api_1ga129bad2da2fc2a40a7d746d86fc9c68d>``` 
yet, to work with Auto-batching, an explicit batch size must be specified, e.g., ``BATCH:<device>(16)``.

This "automatic batch size selection" works on the presumption that the application queries 
``:ref:`ov::optimal_number_of_infer_requests <doxid-group__ov__runtime__cpp__prop__api_1ga087c6da667f7c3d8374aec5f6cbba027>``` 
to create the requests of the returned number and run them simultaneously:

.. tab:: C++

   .. ref-code-block:: cpp

      // when the batch size is automatically selected by the implementation
      // it is important to query/create and run the sufficient #requests
      auto compiled_model = core.compile_model(:ref:`model <doxid-group__ov__runtime__cpp__prop__api_1ga461856fdfb6d7533dc53355aec9e9fad>`, "GPU",
         :ref:`ov::hint::performance_mode <doxid-group__ov__runtime__cpp__prop__api_1ga2691fe27acc8aa1d1700ad40b6da3ba2>`(:ref:`ov::hint::PerformanceMode::THROUGHPUT <doxid-group__ov__runtime__cpp__prop__api_1gga032aa530efa40760b79af14913d48d73a50f9b1f40c078d242af7ec323ace44b3>`));
      auto num_requests = compiled_model.get_property(:ref:`ov::optimal_number_of_infer_requests <doxid-group__ov__runtime__cpp__prop__api_1ga087c6da667f7c3d8374aec5f6cbba027>`);

.. tab:: Python

   .. ref-code-block:: cpp

      # when the batch size is automatically selected by the implementation
      # it is important to query/create and run the sufficient requests
      config = {"PERFORMANCE_HINT": "THROUGHPUT"}
      compiled_model = core.compile_model(model, "GPU", config)
      num_requests = compiled_model.get_property("OPTIMAL_NUMBER_OF_INFER_REQUESTS")


Optimizing Performance by Limiting Batch Size
---------------------------------------------

If not enough inputs were collected, the ``timeout`` value makes the transparent 
execution fall back to the execution of individual requests. This value can be 
configured via the ``AUTO_BATCH_TIMEOUT`` property. The timeout, which adds itself 
to the execution time of the requests, heavily penalizes the performance. To avoid 
this, when your parallel slack is bounded, provide OpenVINO with an additional hint.

For example, when the application processes only 4 video streams, there is no need 
to use a batch larger than 4. The most future-proof way to communicate the limitations 
on the parallelism is to equip the performance hint with the optional ``ov::hint::num_requests`` 
configuration key set to 4. This will limit the batch size for the GPU and the number 
of inference streams for the CPU, hence each device uses ``ov::hint::num_requests`` 
while converting the hint to the actual device configuration options:

.. tab:: C++

   .. ref-code-block:: cpp

      // limiting the available parallel slack for the 'throughput' hint via the ov::hint::num_requests
      // so that certain parameters (like selected batch size) are automatically accommodated accordingly 
      auto compiled_model = core.compile_model(:ref:`model <doxid-group__ov__runtime__cpp__prop__api_1ga461856fdfb6d7533dc53355aec9e9fad>`, "GPU",
         :ref:`ov::hint::performance_mode <doxid-group__ov__runtime__cpp__prop__api_1ga2691fe27acc8aa1d1700ad40b6da3ba2>`(:ref:`ov::hint::PerformanceMode::THROUGHPUT <doxid-group__ov__runtime__cpp__prop__api_1gga032aa530efa40760b79af14913d48d73a50f9b1f40c078d242af7ec323ace44b3>`),
         ov::hint::num_requests(4));

.. tab:: Python

   .. ref-code-block:: cpp

      config = {"PERFORMANCE_HINT": "THROUGHPUT",
               "PERFORMANCE_HINT_NUM_REQUESTS": "4"}
      # limiting the available parallel slack for the 'throughput'
      # so that certain parameters (like selected batch size) are automatically accommodated accordingly 
      compiled_model = core.compile_model(model, "GPU", config)


For the *explicit* usage, you can limit the batch size by using ``BATCH:GPU(4)``, 
where 4 is the number of requests running in parallel.

Other Performance Considerations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To achieve the best performance with Automatic Batching, the application should:

* Operate inference requests of the number that represents the multiple of the batch size. In the example above, for batch size 4, the application should operate 4, 8, 12, 16, etc. requests.

* Use the requests that are grouped by the batch size together. For example, the first 4 requests are inferred, while the second group of the requests is being populated. Essentially, Automatic Batching shifts the asynchronicity from the individual requests to the groups of requests that constitute the batches.
  
  * Balance the ``timeout`` value vs. the batch size. For example, in many cases, having a smaller ``timeout`` value/batch size may yield better performance than having a larger batch size with a ``timeout`` value that is not large enough to accommodate the full number of the required requests.
  
  * When Automatic Batching is enabled, the ``timeout`` property of ``:ref:`ov::CompiledModel <doxid-classov_1_1_compiled_model>``` can be changed anytime, even after the loading/compilation of the model. For example, setting the value to 0 disables Auto-batching effectively, as the collection of requests would be omitted.
  
  * Carefully apply Auto-batching to the pipelines. For example, in the conventional "video-sources -> detection -> classification" flow, it is most beneficial to do Auto-batching over the inputs to the detection stage. The resulting number of detections is usually fluent, which makes Auto-batching less applicable for the classification stage.

The following are limitations of the current implementations:

* Although it is less critical for the throughput-oriented scenarios, the load time with Auto-batching increases by almost double.
  
  * Certain networks are not safely reshapable by the "batching" dimension (specified as ``N`` in the layout terms). Besides, if the batching dimension is not zeroth, Auto-batching will not be triggered "implicitly" by the throughput hint.
  
  * The "explicit" notion, for example, ``BATCH:GPU``, using the relaxed dimensions tracking, often makes Auto-batching possible. For example, this method unlocks most **detection networks**.
  
  * When *forcing* Auto-batching via the "explicit" device notion, make sure that you validate the results for correctness.
  
  * Performance improvements happen at the cost of the growth of memory footprint. However, Auto-batching queries the available memory (especially for dGPU) and limits the selected batch size accordingly.

Testing Performance with Benchmark_app
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The ``benchmark_app`` sample, that has both 
:ref:`C++ <doxid-openvino_inference_engine_samples_benchmark_app__r_e_a_d_m_e>` 
and :ref:`Python <doxid-openvino_inference_engine_tools_benchmark_tool__r_e_a_d_m_e>` 
versions, is the best way to evaluate the performance of Automatic Batching:

* The most straightforward way is using the performance hints:
  
  * benchmark_app **-hint tput** -d GPU -m 'path to your favorite model'

* You can also use the "explicit" device notion to override the strict rules of the implicit reshaping by the batch dimension:
  
  * benchmark_app **-hint none -d BATCH:GPU** -m 'path to your favorite model'

* or override the automatically deduced batch size as well:
  
  * $benchmark_app -hint none -d **BATCH:GPU(16)** -m 'path to your favorite model'
  
  * This example also applies to CPU or any other device that generally supports batch execution.
  
  * Keep in mind that some shell versions (e.g. ``bash``) may require adding quotes around complex device names, i.e. ``-d "BATCH:GPU(16)"`` in this example.

Note that Benchmark_app performs a warm-up run of a *single* request. As Auto-Batching 
requires significantly more requests to execute in batch, this warm-up run hits the 
default timeout value (1000 ms), as reported in the following example:

.. ref-code-block:: cpp

	[ INFO ] First inference took 1000.18ms

This value also exposed as the final execution statistics on the ``benchmark_app`` exit:

.. ref-code-block:: cpp

	[ INFO ] Latency: 
	[ INFO ]  Max:      1000.18 ms

This is NOT the actual latency of the batched execution, so you are recommended to 
refer to other metrics in the same log, for example, "Median" or "Average" execution.

Additional Resources
--------------------

:ref:`Supported Devices <doxid-openvino_docs__o_v__u_g_supported_plugins__supported__devices>`

