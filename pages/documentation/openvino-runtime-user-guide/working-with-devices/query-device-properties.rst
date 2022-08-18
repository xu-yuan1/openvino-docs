.. index:: pair: page; Query Device Properties - Configuration
.. _doxid-openvino_docs__o_v__u_g_query_api:


Query Device Properties - Configuration
=======================================

:target:`doxid-openvino_docs__o_v__u_g_query_api_1md_openvino_docs_ov_runtime_ug_supported_plugins_config_properties`

The OpenVINO™ toolkit supports inference with several types of devices (processors or accelerators). This section provides a high-level description of the process of querying of different device properties and configuration values at runtime.

OpenVINO runtime has two types of properties:

* Read only properties which provide information about the devices (such as device name, thermal state, execution capabilities, etc.) and information about configuration values used to compile the model (``:ref:`ov::CompiledModel <doxid-classov_1_1_compiled_model>```) .

* Mutable properties which are primarily used to configure the ``:ref:`ov::Core::compile_model <doxid-classov_1_1_core_1a46555f0803e8c29524626be08e7f5c5a>``` process and affect final inference on a specific set of devices. Such properties can be set globally per device via ``:ref:`ov::Core::set_property <doxid-classov_1_1_core_1aa953cb0a1601dbc9a34ef6ba82b8476e>``` or locally for particular model in the ``:ref:`ov::Core::compile_model <doxid-classov_1_1_core_1a46555f0803e8c29524626be08e7f5c5a>``` and the ``:ref:`ov::Core::query_model <doxid-classov_1_1_core_1acdf8e64824fe4cf147c3b52ab32c1aab>``` calls.

An OpenVINO property is represented as a named constexpr variable with a given string name and a type. The following example represents a read-only property with a C++ name of ``:ref:`ov::available_devices <doxid-group__ov__runtime__cpp__prop__api_1gac4d3e86ef4fc43b1a80ec28c7be39ef1>```, a string name of ``AVAILABLE_DEVICES`` and a type of ``std::vector<std::string>`` :

.. ref-code-block:: cpp

	static constexpr Property<std::vector<std::string>, PropertyMutability::RO> available_devices{"AVAILABLE_DEVICES"};

Refer to the :ref:`Hello Query Device С++ Sample <doxid-openvino_inference_engine_samples_hello_query_device__r_e_a_d_m_e>` sources and the :ref:`Multi-Device execution <doxid-openvino_docs__o_v__u_g__running_on_multiple_devices>` documentation for examples of using setting and getting properties in user applications.

Get a Set of Available Devices
------------------------------

Based on the ``:ref:`ov::available_devices <doxid-group__ov__runtime__cpp__prop__api_1gac4d3e86ef4fc43b1a80ec28c7be39ef1>``` read-only property, OpenVINO Core collects information about currently available devices enabled by OpenVINO plugins and returns information, using the ``:ref:`ov::Core::get_available_devices <doxid-classov_1_1_core_1aabd82bca4826ee53893f7b5fc9bce813>``` method:

.. raw:: html

   <div class='sphinxtabset'>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="C++">





.. ref-code-block:: cpp

	:ref:`ov::Core <doxid-classov_1_1_core>` core;
	std::vector<std::string> :ref:`available_devices <doxid-group__ov__runtime__cpp__prop__api_1gac4d3e86ef4fc43b1a80ec28c7be39ef1>` = core.:ref:`get_available_devices <doxid-classov_1_1_core_1aabd82bca4826ee53893f7b5fc9bce813>`();

.. raw:: html

   </div>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="Python">





.. ref-code-block:: cpp

	core = Core()
	available_devices = core.available_devices

.. raw:: html

   </div>







.. raw:: html

   </div>

The function returns a list of available devices, for example:

.. ref-code-block:: cpp

	MYRIAD.1.2-ma2480
	MYRIAD.1.4-ma2480
	CPU
	GPU.0
	GPU.1

If there are multiple instances of a specific device, the devices are enumerated with a suffix comprising a full stop and a unique string identifier, such as ``.suffix``. Each device name can then be passed to:

* ``:ref:`ov::Core::compile_model <doxid-classov_1_1_core_1a46555f0803e8c29524626be08e7f5c5a>``` to load the model to a specific device with specific configuration properties.

* ``:ref:`ov::Core::get_property <doxid-classov_1_1_core_1a4fb9fc7375d04f744a27a9588cbcff1a>``` to get common or device-specific properties.

* All other methods of the ``:ref:`ov::Core <doxid-classov_1_1_core>``` class that accept ``deviceName``.

Working with Properties in Your Code
------------------------------------

The ``:ref:`ov::Core <doxid-classov_1_1_core>``` class provides the following method to query device information, set or get different device configuration properties:

* ``:ref:`ov::Core::get_property <doxid-classov_1_1_core_1a4fb9fc7375d04f744a27a9588cbcff1a>``` - Gets the current value of a specific property.

* ``:ref:`ov::Core::set_property <doxid-classov_1_1_core_1aa953cb0a1601dbc9a34ef6ba82b8476e>``` - Sets a new value for the property globally for specified ``device_name``.

The ``:ref:`ov::CompiledModel <doxid-classov_1_1_compiled_model>``` class is also extended to support the properties:

* ``:ref:`ov::CompiledModel::get_property <doxid-classov_1_1_compiled_model_1a109d701ffe8b5de096961c7c98ff0bed>```

* ``:ref:`ov::CompiledModel::set_property <doxid-classov_1_1_compiled_model_1a9beec68aa25d6535e26fae5df00aaba0>```

For documentation about OpenVINO common device-independent properties, refer to the ``openvino/runtime/properties.hpp``. Device-specific configuration keys can be found in corresponding device folders (for example, ``openvino/runtime/intel_gpu/properties.hpp``).

Working with Properties via Core
--------------------------------

Getting Device Properties
+++++++++++++++++++++++++

The code below demonstrates how to query ``HETERO`` device priority of devices which will be used to infer the model:

.. raw:: html

   <div class='sphinxtabset'>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="C++">





.. ref-code-block:: cpp

	auto device_priorites = core.:ref:`get_property <doxid-classov_1_1_core_1a4fb9fc7375d04f744a27a9588cbcff1a>`("HETERO", :ref:`ov::device::priorities <doxid-group__ov__runtime__cpp__prop__api_1gae88af90a18871677f39739cb0ef0101e>`);

.. raw:: html

   </div>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="Python">





.. ref-code-block:: cpp

	device_priorites = core.get_property("HETERO", "MULTI_DEVICE_PRIORITIES")

.. raw:: html

   </div>







.. raw:: html

   </div>





.. note::

   All properties have a type, which is specified during property declaration. 
   Based on this, actual type under ``auto`` is automatically deduced by C++ compiler.



To extract device properties such as available devices (``:ref:`ov::available_devices <doxid-group__ov__runtime__cpp__prop__api_1gac4d3e86ef4fc43b1a80ec28c7be39ef1>```), device name (``:ref:`ov::device::full_name <doxid-group__ov__runtime__cpp__prop__api_1gaabacd9ea113b966be7b53b1d70fd6f42>```), supported properties (``:ref:`ov::supported_properties <doxid-group__ov__runtime__cpp__prop__api_1ga097f1274f26f3f4e1aa4fc3928748592>```), and others, use the ``:ref:`ov::Core::get_property <doxid-classov_1_1_core_1a4fb9fc7375d04f744a27a9588cbcff1a>``` method:

.. raw:: html

   <div class='sphinxtabset'>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="C++">





.. ref-code-block:: cpp

	auto cpu_device_name = core.:ref:`get_property <doxid-classov_1_1_core_1a4fb9fc7375d04f744a27a9588cbcff1a>`("CPU", :ref:`ov::device::full_name <doxid-group__ov__runtime__cpp__prop__api_1gaabacd9ea113b966be7b53b1d70fd6f42>`);

.. raw:: html

   </div>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="Python">





.. ref-code-block:: cpp

	cpu_device_name = core.get_property("CPU", "FULL_DEVICE_NAME")

.. raw:: html

   </div>







.. raw:: html

   </div>



A returned value appears as follows: ``Intel(R) Core(TM) i7-8700 CPU @ 3.20GHz``.

.. note::

   In order to understand a list of supported properties on 
   ``:ref:`ov::Core <doxid-classov_1_1_core>``` or 
   ``:ref:`ov::CompiledModel <doxid-classov_1_1_compiled_model>``` 
   levels, use ``:ref:`ov::supported_properties <doxid-group__ov__runtime__cpp__prop__api_1ga097f1274f26f3f4e1aa4fc3928748592>``` 
   which contains a vector of supported property names. Properties which can be 
   changed, has ``:ref:`ov::PropertyName::is_mutable <doxid-structov_1_1_property_name_1a7c31d6356fad04394463ec5a3b9b4148>``` 
   returning the ``true`` value. Most of the properites which are changable on 
   ``:ref:`ov::Core <doxid-classov_1_1_core>``` level, cannot be changed once the 
   model is compiled, so it becomes immutable read-only property.





Configure a Work with a Model
+++++++++++++++++++++++++++++

The ``:ref:`ov::Core <doxid-classov_1_1_core>``` methods like:

* ``:ref:`ov::Core::compile_model <doxid-classov_1_1_core_1a46555f0803e8c29524626be08e7f5c5a>```

* ``:ref:`ov::Core::import_model <doxid-classov_1_1_core_1a0d2853511bd7ba60cb591f4685b91884>```

* ``:ref:`ov::Core::query_model <doxid-classov_1_1_core_1acdf8e64824fe4cf147c3b52ab32c1aab>```

accept a selection of properties as last arguments. Each of the properties should be used as a function call to pass a property value with a specified property type.

.. raw:: html

   <div class='sphinxtabset'>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="C++">





.. ref-code-block:: cpp

	auto compiled_model = core.:ref:`compile_model <doxid-classov_1_1_core_1a46555f0803e8c29524626be08e7f5c5a>`(:ref:`model <doxid-group__ov__runtime__cpp__prop__api_1ga461856fdfb6d7533dc53355aec9e9fad>`, "CPU",
	    :ref:`ov::hint::performance_mode <doxid-group__ov__runtime__cpp__prop__api_1ga2691fe27acc8aa1d1700ad40b6da3ba2>`(:ref:`ov::hint::PerformanceMode::THROUGHPUT <doxid-group__ov__runtime__cpp__prop__api_1gga032aa530efa40760b79af14913d48d73a50f9b1f40c078d242af7ec323ace44b3>`),
	    :ref:`ov::hint::inference_precision <doxid-group__ov__runtime__cpp__prop__api_1gad605a888f3c9b7598ab55023fbf44240>`(:ref:`ov::element::f32 <doxid-group__ov__element__cpp__api_1gadc8a5dda3244028a5c0b024897215d43>`));

.. raw:: html

   </div>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="Python">





.. ref-code-block:: cpp

	config = {"PERFORMANCE_HINT": "THROUGHPUT",
	        "INFERENCE_PRECISION_HINT": "f32"}
	compiled_model = core.compile_model(model, "CPU", config)

.. raw:: html

   </div>







.. raw:: html

   </div>



The example below specifies hints that a model should be compiled to be inferred with multiple inference requests in parallel to achieve best throughput, while inference should be performed without accuracy loss with FP32 precision.

Setting Properties Globally
+++++++++++++++++++++++++++

``:ref:`ov::Core::set_property <doxid-classov_1_1_core_1aa953cb0a1601dbc9a34ef6ba82b8476e>``` with a given device name should be used to set global configuration properties, which are the same across multiple ``:ref:`ov::Core::compile_model <doxid-classov_1_1_core_1a46555f0803e8c29524626be08e7f5c5a>```, ``:ref:`ov::Core::query_model <doxid-classov_1_1_core_1acdf8e64824fe4cf147c3b52ab32c1aab>```, and other calls. However, setting properties on a specific ``:ref:`ov::Core::compile_model <doxid-classov_1_1_core_1a46555f0803e8c29524626be08e7f5c5a>``` call applies properties only for the current call:

.. raw:: html

   <div class='sphinxtabset'>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="C++">





.. ref-code-block:: cpp

	// set letency hint is a default for CPU
	core.:ref:`set_property <doxid-classov_1_1_core_1aa953cb0a1601dbc9a34ef6ba82b8476e>`("CPU", :ref:`ov::hint::performance_mode <doxid-group__ov__runtime__cpp__prop__api_1ga2691fe27acc8aa1d1700ad40b6da3ba2>`(:ref:`ov::hint::PerformanceMode::LATENCY <doxid-group__ov__runtime__cpp__prop__api_1gga032aa530efa40760b79af14913d48d73a501069dd75f76384ba18f133fdce99c2>`));
	// compiled with latency configuration hint
	auto compiled_model_latency = core.:ref:`compile_model <doxid-classov_1_1_core_1a46555f0803e8c29524626be08e7f5c5a>`(:ref:`model <doxid-group__ov__runtime__cpp__prop__api_1ga461856fdfb6d7533dc53355aec9e9fad>`, "CPU");
	// compiled with overriden ov::hint::performance_mode value
	auto compiled_model_thrp = core.:ref:`compile_model <doxid-classov_1_1_core_1a46555f0803e8c29524626be08e7f5c5a>`(:ref:`model <doxid-group__ov__runtime__cpp__prop__api_1ga461856fdfb6d7533dc53355aec9e9fad>`, "CPU",
	    :ref:`ov::hint::performance_mode <doxid-group__ov__runtime__cpp__prop__api_1ga2691fe27acc8aa1d1700ad40b6da3ba2>`(:ref:`ov::hint::PerformanceMode::THROUGHPUT <doxid-group__ov__runtime__cpp__prop__api_1gga032aa530efa40760b79af14913d48d73a50f9b1f40c078d242af7ec323ace44b3>`));

.. raw:: html

   </div>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="Python">





.. ref-code-block:: cpp

	# latency hint is a default for CPU
	core.set_property("CPU", {"PERFORMANCE_HINT": "LATENCY"})
	# compiled with latency configuration hint
	compiled_model_latency = core.compile_model(model, "CPU")
	# compiled with overriden performance hint value
	config = {"PERFORMANCE_HINT": "THROUGHPUT"}
	compiled_model_thrp = core.compile_model(model, "CPU", config)

.. raw:: html

   </div>







.. raw:: html

   </div>





Properties on CompiledModel Level
---------------------------------

Getting Property
++++++++++++++++

The ``:ref:`ov::CompiledModel::get_property <doxid-classov_1_1_compiled_model_1a109d701ffe8b5de096961c7c98ff0bed>``` method is used to get property values the compiled model has been created with or a compiled model level property such as ``:ref:`ov::optimal_number_of_infer_requests <doxid-group__ov__runtime__cpp__prop__api_1ga087c6da667f7c3d8374aec5f6cbba027>``` :

.. raw:: html

   <div class='sphinxtabset'>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="C++">





.. ref-code-block:: cpp

	auto compiled_model = core.:ref:`compile_model <doxid-classov_1_1_core_1a46555f0803e8c29524626be08e7f5c5a>`(:ref:`model <doxid-group__ov__runtime__cpp__prop__api_1ga461856fdfb6d7533dc53355aec9e9fad>`, "CPU");
	auto nireq = compiled_model.:ref:`get_property <doxid-classov_1_1_compiled_model_1a109d701ffe8b5de096961c7c98ff0bed>`(:ref:`ov::optimal_number_of_infer_requests <doxid-group__ov__runtime__cpp__prop__api_1ga087c6da667f7c3d8374aec5f6cbba027>`);

.. raw:: html

   </div>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="Python">





.. ref-code-block:: cpp

	compiled_model = core.compile_model(model, "CPU")
	nireq = compiled_model.get_property("OPTIMAL_NUMBER_OF_INFER_REQUESTS")

.. raw:: html

   </div>







.. raw:: html

   </div>



Or the current temperature of the ``MYRIAD`` device:

.. raw:: html

   <div class='sphinxtabset'>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="C++">





.. ref-code-block:: cpp

	auto compiled_model = core.:ref:`compile_model <doxid-classov_1_1_core_1a46555f0803e8c29524626be08e7f5c5a>`(:ref:`model <doxid-group__ov__runtime__cpp__prop__api_1ga461856fdfb6d7533dc53355aec9e9fad>`, "MYRIAD");
	float temperature = compiled_model.:ref:`get_property <doxid-classov_1_1_compiled_model_1a109d701ffe8b5de096961c7c98ff0bed>`(:ref:`ov::device::thermal <doxid-group__ov__runtime__cpp__prop__api_1ga821543ca749cd78a8ced9930e0fec466>`);

.. raw:: html

   </div>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="Python">





.. ref-code-block:: cpp

	compiled_model = core.compile_model(model, "MYRIAD")
	temperature = compiled_model.get_property("DEVICE_THERMAL")

.. raw:: html

   </div>







.. raw:: html

   </div>

Or the number of threads that would be used for inference on ``CPU`` device:

.. raw:: html

   <div class='sphinxtabset'>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="C++">





.. ref-code-block:: cpp

	auto compiled_model = core.:ref:`compile_model <doxid-classov_1_1_core_1a46555f0803e8c29524626be08e7f5c5a>`(:ref:`model <doxid-group__ov__runtime__cpp__prop__api_1ga461856fdfb6d7533dc53355aec9e9fad>`, "CPU");
	auto nthreads = compiled_model.:ref:`get_property <doxid-classov_1_1_compiled_model_1a109d701ffe8b5de096961c7c98ff0bed>`(:ref:`ov::inference_num_threads <doxid-group__ov__runtime__cpp__prop__api_1gae73c9d9977901744090317e2afe09440>`);

.. raw:: html

   </div>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="Python">





.. ref-code-block:: cpp

	compiled_model = core.compile_model(model, "CPU")
	nthreads = compiled_model.get_property("INFERENCE_NUM_THREADS")

.. raw:: html

   </div>







.. raw:: html

   </div>





Setting Properties for Compiled Model
+++++++++++++++++++++++++++++++++++++

The only mode that supports this method is :ref:`Multi-Device execution <doxid-openvino_docs__o_v__u_g__running_on_multiple_devices>` :

.. raw:: html

   <div class='sphinxtabset'>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="C++">





.. ref-code-block:: cpp

	auto compiled_model = core.:ref:`compile_model <doxid-classov_1_1_core_1a46555f0803e8c29524626be08e7f5c5a>`(:ref:`model <doxid-group__ov__runtime__cpp__prop__api_1ga461856fdfb6d7533dc53355aec9e9fad>`, "MULTI",
	    :ref:`ov::device::priorities <doxid-group__ov__runtime__cpp__prop__api_1gae88af90a18871677f39739cb0ef0101e>`("CPU", "GPU"));
	// change the order of priorities
	compiled_model.:ref:`set_property <doxid-classov_1_1_compiled_model_1a9beec68aa25d6535e26fae5df00aaba0>`(:ref:`ov::device::priorities <doxid-group__ov__runtime__cpp__prop__api_1gae88af90a18871677f39739cb0ef0101e>`("GPU", "CPU"));

.. raw:: html

   </div>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="Python">





.. ref-code-block:: cpp

	config = {"MULTI_DEVICE_PRIORITIES": "CPU,GPU"}
	compiled_model = core.compile_model(model, "MULTI", config)
	# change the order of priorities
	compiled_model.set_property({"MULTI_DEVICE_PRIORITIES": "GPU,CPU"})

.. raw:: html

   </div>







.. raw:: html

   </div>

