.. index:: pair: page; Configuring Devices
.. _doxid-openvino_2_0_configure_devices:


Configuring Devices
===================

:target:`doxid-openvino_2_0_configure_devices_1md_openvino_docs_ov_runtime_ug_migration_ov_2_0_configure_devices` Inference Engine API provides the `ability to configure devices <https://docs.openvino.ai/2021.4/openvino_docs_IE_DG_InferenceEngine_QueryAPI.html>`__ via configuration keys and `get device specific metrics <https://docs.openvino.ai/2021.4/openvino_docs_IE_DG_InferenceEngine_QueryAPI.html#getmetric>`__. The values taken from ``:ref:`InferenceEngine::Core::GetConfig <doxid-class_inference_engine_1_1_core_1a415077386694f95b57e4cccb0d334a55>``` are requested by the string name, while the return type is ``:ref:`InferenceEngine::Parameter <doxid-namespace_inference_engine_1aff2231f886c9f8fc9c226fd343026789>```, making users lost on what the actual type is stored in this parameter.

API 2.0 solves these issues by introducing :ref:`properties <deploy_infer__query_device_properties>`, which unify metrics and configuration key concepts. The main advantage is that they have the C++ type:

.. ref-code-block:: cpp

	static constexpr Property<std::string> full_name{"FULL_DEVICE_NAME"};

where the property can be requested from an inference device as:

.. ref-code-block:: cpp

	// 'auto' is automatically deduced as std::string
	// since the type is stored in the property
	auto full_device_name = core.get_property("CPU", :ref:`ov::device::full_name <doxid-group__ov__runtime__cpp__prop__api_1gaabacd9ea113b966be7b53b1d70fd6f42>`);

The snippets in the following sections demostrate the device configurations for migrating from Inference Engine to API 2.0.

Setting Configuration Values
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Inference Engine API**

.. raw:: html

   <div class='sphinxtabset'>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="C++">







.. raw:: html

   <div class='sphinxtabset'>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="Devices">





.. ref-code-block:: cpp

	core.SetConfig({ { :ref:`CONFIG_KEY <doxid-ie__plugin__config_8hpp_1aad09cfba062e8ec9fb7ab9383f656ec7>`(PERF_COUNT), :ref:`CONFIG_VALUE <doxid-ie__plugin__config_8hpp_1a2b1801501dc6436ffa1a9ed9c6333b40>`(:ref:`YES <doxid-namespace_inference_engine_1_1_plugin_config_params_1a42d48631fa3332ded8c776513e897bf3>`) } }, "CPU");

.. raw:: html

   </div>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="Model Loading">





.. ref-code-block:: cpp

	auto exec_network = core.LoadNetwork(:ref:`model <doxid-group__ov__runtime__cpp__prop__api_1ga461856fdfb6d7533dc53355aec9e9fad>`, "MULTI", {
	    { :ref:`MULTI_CONFIG_KEY <doxid-multi__device__config_8hpp_1aa887cd604b772a3a51ba73f9652ae6c4>`(DEVICE_PRIORITIES), "CPU, GPU" },
	    { :ref:`CONFIG_KEY <doxid-ie__plugin__config_8hpp_1aad09cfba062e8ec9fb7ab9383f656ec7>`(PERFORMANCE_HINT), :ref:`CONFIG_VALUE <doxid-ie__plugin__config_8hpp_1a2b1801501dc6436ffa1a9ed9c6333b40>`(:ref:`THROUGHPUT <doxid-namespace_inference_engine_1_1_plugin_config_params_1a0902fd7a7ca168b6a188daf4b75db92f>`) },
	    { :ref:`CONFIG_KEY <doxid-ie__plugin__config_8hpp_1aad09cfba062e8ec9fb7ab9383f656ec7>`(ENFORCE_BF16), :ref:`CONFIG_VALUE <doxid-ie__plugin__config_8hpp_1a2b1801501dc6436ffa1a9ed9c6333b40>`(:ref:`NO <doxid-namespace_inference_engine_1_1_plugin_config_params_1a3ceab5fe6f519a82b92c7a3794561c5f>`) } });

.. raw:: html

   </div>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="Execution">





.. ref-code-block:: cpp

	// turn CPU off for multi-device execution
	exec_network.SetConfig({ { :ref:`MULTI_CONFIG_KEY <doxid-multi__device__config_8hpp_1aa887cd604b772a3a51ba73f9652ae6c4>`(DEVICE_PRIORITIES), "GPU" } });

.. raw:: html

   </div>







.. raw:: html

   </div>







.. raw:: html

   </div>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="Python">







.. raw:: html

   <div class='sphinxtabset'>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="Devices">





.. ref-code-block:: cpp

	core.set_config({"PERF_COUNT": "YES"}, "CPU")

.. raw:: html

   </div>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="Model Loading">





.. ref-code-block:: cpp

	exec_network = core.load_network(net, "MULTI", {"DEVICE_PRIORITIES": "CPU, GPU",
	                                                "PERFORMANCE_HINT": "THROUGHPUT",
	                                                "ENFORCE_BF16": "NO"})

.. raw:: html

   </div>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="Execution">





.. ref-code-block:: cpp

	# turn CPU off for multi-device execution
	exec_network.set_config({"DEVICE_PRIORITIES": "GPU"})

.. raw:: html

   </div>







.. raw:: html

   </div>







.. raw:: html

   </div>







.. raw:: html

   </div>



**API 2.0**

.. raw:: html

   <div class='sphinxtabset'>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="C++">







.. raw:: html

   <div class='sphinxtabset'>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="Devices">





.. ref-code-block:: cpp

	core.set_property("CPU", :ref:`ov::enable_profiling <doxid-group__ov__runtime__cpp__prop__api_1gafc5bef2fc2b5cfb5a0709cfb04346438>`(true));

.. raw:: html

   </div>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="Model Loading">





.. ref-code-block:: cpp

	auto compiled_model = core.compile_model(:ref:`model <doxid-group__ov__runtime__cpp__prop__api_1ga461856fdfb6d7533dc53355aec9e9fad>`, "MULTI",
	    :ref:`ov::device::priorities <doxid-group__ov__runtime__cpp__prop__api_1gae88af90a18871677f39739cb0ef0101e>`("GPU", "CPU"),
	    :ref:`ov::hint::performance_mode <doxid-group__ov__runtime__cpp__prop__api_1ga2691fe27acc8aa1d1700ad40b6da3ba2>`(:ref:`ov::hint::PerformanceMode::THROUGHPUT <doxid-group__ov__runtime__cpp__prop__api_1gga032aa530efa40760b79af14913d48d73a50f9b1f40c078d242af7ec323ace44b3>`),
	    :ref:`ov::hint::inference_precision <doxid-group__ov__runtime__cpp__prop__api_1gad605a888f3c9b7598ab55023fbf44240>`(:ref:`ov::element::f32 <doxid-group__ov__element__cpp__api_1gadc8a5dda3244028a5c0b024897215d43>`));

.. raw:: html

   </div>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="Execution">





.. ref-code-block:: cpp

	// turn CPU off for multi-device execution
	compiled_model.set_property(:ref:`ov::device::priorities <doxid-group__ov__runtime__cpp__prop__api_1gae88af90a18871677f39739cb0ef0101e>`("GPU"));

.. raw:: html

   </div>







.. raw:: html

   </div>







.. raw:: html

   </div>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="Python">







.. raw:: html

   <div class='sphinxtabset'>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="Devices">





.. ref-code-block:: cpp

	core.set_property(device_name="CPU", properties={"PERF_COUNT": "YES"})

.. raw:: html

   </div>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="Model Loading">





.. ref-code-block:: cpp

	compiled_model = core.compile_model(model=model, device_name="MULTI", config=
	    {
	        "MULTI_DEVICE_PRIORITIES": "GPU,CPU",
	        "PERFORMANCE_HINT": "THROUGHPUT",
	        "INFERENCE_PRECISION_HINT": "f32"
	    })

.. raw:: html

   </div>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="Execution">





.. ref-code-block:: cpp

	# turn CPU off for multi-device execution
	compiled_model.set_property(properties={"MULTI_DEVICE_PRIORITIES": "GPU"})

.. raw:: html

   </div>







.. raw:: html

   </div>







.. raw:: html

   </div>







.. raw:: html

   </div>





Getting Information
~~~~~~~~~~~~~~~~~~~

**Inference Engine API**

.. raw:: html

   <div class='sphinxtabset'>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="C++">







.. raw:: html

   <div class='sphinxtabset'>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="Device Configuration">





.. ref-code-block:: cpp

	// a user has to parse std::string after
	auto :ref:`num_streams <doxid-group__ov__runtime__cpp__prop__api_1ga6c63a0223565f650475450fdb466bc0c>` = core.GetConfig("CPU", :ref:`CONFIG_KEY <doxid-ie__plugin__config_8hpp_1aad09cfba062e8ec9fb7ab9383f656ec7>`(CPU_THROUGHPUT_STREAMS)).as<std::string>();

.. raw:: html

   </div>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="Device metrics">





.. ref-code-block:: cpp

	auto full_device_name = core.GetMetric("CPU", :ref:`METRIC_KEY <doxid-ie__plugin__config_8hpp_1a69d0efa20c5b2bec020a706279f0c7be>`(FULL_DEVICE_NAME)).as<std::string>();

.. raw:: html

   </div>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="Execution config">





.. ref-code-block:: cpp

	std::string perf_model = exec_network.GetConfig(:ref:`CONFIG_KEY <doxid-ie__plugin__config_8hpp_1aad09cfba062e8ec9fb7ab9383f656ec7>`(PERFORMANCE_HINT)).as<std::string>();

.. raw:: html

   </div>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="Execution metrics">





.. ref-code-block:: cpp

	auto nireq = exec_network.GetMetric(:ref:`EXEC_NETWORK_METRIC_KEY <doxid-ie__plugin__config_8hpp_1adb48efa632ae9bacfa86b8a3a0d9541e>`(OPTIMAL_NUMBER_OF_INFER_REQUESTS)).as<uint32_t>();

.. raw:: html

   </div>







.. raw:: html

   </div>







.. raw:: html

   </div>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="Python">







.. raw:: html

   <div class='sphinxtabset'>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="Device Configuration">





.. ref-code-block:: cpp

	num_streams = core.get_config("CPU", "CPU_THROUGHPUT_STREAMS")

.. raw:: html

   </div>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="Device metrics">





.. ref-code-block:: cpp

	full_device_name = core.get_metric("CPU", "FULL_DEVICE_NAME")

.. raw:: html

   </div>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="Execution config">





.. ref-code-block:: cpp

	perf_hint = exec_network.get_config("PERFORMANCE_HINT")

.. raw:: html

   </div>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="Execution metrics">





.. ref-code-block:: cpp

	nireq = exec_network.get_metric("OPTIMAL_NUMBER_OF_INFER_REQUESTS")

.. raw:: html

   </div>







.. raw:: html

   </div>







.. raw:: html

   </div>







.. raw:: html

   </div>



**API 2.0**

.. raw:: html

   <div class='sphinxtabset'>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="C++">







.. raw:: html

   <div class='sphinxtabset'>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="Device Configuration">





.. ref-code-block:: cpp

	// 'auto' is automatically deduced as ov::streams::Num
	// since the type is stored in the property
	auto :ref:`num_streams <doxid-group__ov__runtime__cpp__prop__api_1ga6c63a0223565f650475450fdb466bc0c>` = core.get_property("CPU", :ref:`ov::streams::num <doxid-group__ov__runtime__cpp__prop__api_1gaeeef815df8212c810bfa11a3f0bd8300>`);

.. raw:: html

   </div>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="Device metrics">





.. ref-code-block:: cpp

	// 'auto' is automatically deduced as std::string
	// since the type is stored in the property
	auto full_device_name = core.get_property("CPU", :ref:`ov::device::full_name <doxid-group__ov__runtime__cpp__prop__api_1gaabacd9ea113b966be7b53b1d70fd6f42>`);

.. raw:: html

   </div>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="Execution config">





.. ref-code-block:: cpp

	:ref:`ov::hint::PerformanceMode <doxid-group__ov__runtime__cpp__prop__api_1ga032aa530efa40760b79af14913d48d73>` perf_mode = compiled_model.get_property(:ref:`ov::hint::performance_mode <doxid-group__ov__runtime__cpp__prop__api_1ga2691fe27acc8aa1d1700ad40b6da3ba2>`);

.. raw:: html

   </div>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="Execution metrics">





.. ref-code-block:: cpp

	// 'auto' is deduced to 'uint32_t'
	auto nireq = compiled_model.get_property(:ref:`ov::optimal_number_of_infer_requests <doxid-group__ov__runtime__cpp__prop__api_1ga087c6da667f7c3d8374aec5f6cbba027>`);

.. raw:: html

   </div>







.. raw:: html

   </div>







.. raw:: html

   </div>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="Python">







.. raw:: html

   <div class='sphinxtabset'>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="Device Configuration">





.. ref-code-block:: cpp

	num_streams = core.get_property("CPU", "NUM_STREAMS")

.. raw:: html

   </div>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="Device metrics">





.. ref-code-block:: cpp

	full_device_name = core.get_property("CPU", "FULL_DEVICE_NAME")

.. raw:: html

   </div>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="Execution config">





.. ref-code-block:: cpp

	perf_mode = compiled_model.get_property("PERFORMANCE_HINT")

.. raw:: html

   </div>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="Execution metrics">





.. ref-code-block:: cpp

	nireq = compiled_model.get_property("OPTIMAL_NUMBER_OF_INFER_REQUESTS")

.. raw:: html

   </div>







.. raw:: html

   </div>







.. raw:: html

   </div>







.. raw:: html

   </div>

