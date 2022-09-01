.. index:: pair: page; Inference Pipeline
.. _doxid-openvino_2_0_inference_pipeline:


Inference Pipeline
==================

:target:`doxid-openvino_2_0_inference_pipeline_1md_openvino_docs_ov_runtime_ug_migration_ov_2_0_common_inference_pipeline` To infer models with OpenVINO™ Runtime, you usually need to perform the following steps in the application pipeline:

#. `Create a Core object. <#create-core>`__
   
   * 1.1. `(Optional) Load extensions. <#load-extensions>`__

#. `Read a model from a drive. <#read-model>`__
   
   * 2.1. `(Optional) Perform model preprocessing. <#perform-preprocessing>`__

#. `Load the model to the device. <#load-model-to-device>`__

#. `Create an inference request. <#create-inference-request>`__

#. `Fill input tensors with data. <#fill-tensor>`__

#. `Start inference. <#start-inference>`__

#. `Process the inference results. <#process-results>`__

Based on the steps, the following code demostrates how to change the application code to migrate to API 2.0.

.. _create-core:

1. Create a Core Object
~~~~~~~~~~~~~~~~~~~~~~~

**Inference Engine API**

.. raw:: html

   <div class='sphinxtabset'>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="C++">





.. ref-code-block:: cpp

	:ref:`InferenceEngine::Core <doxid-class_inference_engine_1_1_core>` core;





.. raw:: html

   </div>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="Python">





.. ref-code-block:: cpp

	import numpy as np
	import openvino.inference_engine as ie
	core = ie.IECore()





.. raw:: html

   </div>







.. raw:: html

   </div>



**API 2.0**

.. _load-extensions:

.. raw:: html

   <div class='sphinxtabset'>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="C++">





.. ref-code-block:: cpp

	:ref:`ov::Core <doxid-classov_1_1_core>` core;





.. raw:: html

   </div>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="Python">





.. ref-code-block:: cpp

	import openvino.runtime as ov
	core = :ref:`ov.Core <doxid-classov_1_1_core>`()





.. raw:: html

   </div>







.. raw:: html

   </div>





1.1 (Optional) Load Extensions
------------------------------

To load a model with custom operations, you need to add extensions for these operations. It is highly recommended to use :ref:`OpenVINO Extensibility API <extensibility__api_introduction>` to write extensions. However, you can also load the old extensions to the new OpenVINO™ Runtime:

**Inference Engine API**

.. raw:: html

   <div class='sphinxtabset'>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="C++">





.. ref-code-block:: cpp

	core.:ref:`AddExtension <doxid-class_inference_engine_1_1_core_1aac8284a60791abd6e50ddab0c695e38f>`(std::make_shared<InferenceEngine::Extension>("path_to_extension_library.so"));





.. raw:: html

   </div>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="Python">





.. ref-code-block:: cpp

	core.add_extension("path_to_extension_library.so", "CPU")





.. raw:: html

   </div>







.. raw:: html

   </div>



**API 2.0**

.. _read-model:

.. raw:: html

   <div class='sphinxtabset'>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="C++">





.. ref-code-block:: cpp

	core.add_extension(std::make_shared<InferenceEngine::Extension>("path_to_extension_library.so"));





.. raw:: html

   </div>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="Python">





.. ref-code-block:: cpp

	core.add_extension("path_to_extension_library.so")





.. raw:: html

   </div>







.. raw:: html

   </div>





2. Read a Model from a Drive
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Inference Engine API**

.. raw:: html

   <div class='sphinxtabset'>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="C++">





.. ref-code-block:: cpp

	:ref:`InferenceEngine::CNNNetwork <doxid-class_inference_engine_1_1_c_n_n_network>` network = core.:ref:`ReadNetwork <doxid-class_inference_engine_1_1_core_1ac716dda382aefd09264b60ea40def3ef>`("model.xml");





.. raw:: html

   </div>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="Python">





.. ref-code-block:: cpp

	network = core.read_network("model.xml")





.. raw:: html

   </div>







.. raw:: html

   </div>



**API 2.0**

.. raw:: html

   <div class='sphinxtabset'>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="C++">





.. ref-code-block:: cpp

	std::shared_ptr<ov::Model> :ref:`model <doxid-group__ov__runtime__cpp__prop__api_1ga461856fdfb6d7533dc53355aec9e9fad>` = core.read_model("model.xml");





.. raw:: html

   </div>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="Python">





.. ref-code-block:: cpp

	model = core.read_model("model.xml")





.. raw:: html

   </div>







.. raw:: html

   </div>



Reading a model has the same structure as the example in the :ref:`model creation migration guide <doxid-openvino_2_0_model_creation>`.

You can combine reading and compiling a model into a single call ``ov::Core::compile_model(filename, devicename)``.

.. _perform-preprocessing:

2.1 (Optional) Perform Model Preprocessing
------------------------------------------

When the application input data does not perfectly match the model input format, preprocessing may be necessary. See :ref:`preprocessing in API 2.0 <doxid-openvino_2_0_preprocessing>` for more details.

.. _load-model-to-device:

3. Load the Model to the Device
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Inference Engine API**

.. raw:: html

   <div class='sphinxtabset'>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="C++">





.. ref-code-block:: cpp

	:ref:`InferenceEngine::ExecutableNetwork <doxid-class_inference_engine_1_1_executable_network>` exec_network = core.:ref:`LoadNetwork <doxid-class_inference_engine_1_1_core_1a7b0b5ab0009abc572762422105b5c666>`(network, "CPU");





.. raw:: html

   </div>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="Python">





.. ref-code-block:: cpp

	# Load network to the device and create infer requests
	exec_network = core.load_network(network, "CPU", num_requests=4)





.. raw:: html

   </div>







.. raw:: html

   </div>



**API 2.0**

.. raw:: html

   <div class='sphinxtabset'>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="C++">





.. ref-code-block:: cpp

	:ref:`ov::CompiledModel <doxid-classov_1_1_compiled_model>` compiled_model = core.compile_model(:ref:`model <doxid-group__ov__runtime__cpp__prop__api_1ga461856fdfb6d7533dc53355aec9e9fad>`, "CPU");





.. raw:: html

   </div>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="Python">





.. ref-code-block:: cpp

	compiled_model = core.compile_model(model, "CPU")





.. raw:: html

   </div>







.. raw:: html

   </div>



If you need to configure devices with additional parameters for OpenVINO Runtime, refer to :ref:`Configuring Devices <doxid-openvino_2_0_configure_devices>`.

.. _create-inference-request:

4. Create an Inference Request
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Inference Engine API**

.. raw:: html

   <div class='sphinxtabset'>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="C++">





.. ref-code-block:: cpp

	:ref:`InferenceEngine::InferRequest <doxid-class_inference_engine_1_1_infer_request>` infer_request = exec_network.:ref:`CreateInferRequest <doxid-class_inference_engine_1_1_executable_network_1a5516b9b68b8fa0bcc72f19bc812ccf47>`();





.. raw:: html

   </div>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="Python">





.. ref-code-block:: cpp

	# Done in the previous step





.. raw:: html

   </div>







.. raw:: html

   </div>



**API 2.0**

.. _fill-tensor:

.. raw:: html

   <div class='sphinxtabset'>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="C++">





.. ref-code-block:: cpp

	:ref:`ov::InferRequest <doxid-classov_1_1_infer_request>` infer_request = compiled_model.:ref:`create_infer_request <doxid-classov_1_1_compiled_model_1ae3633c0eb5173ed776446fba32b95953>`();





.. raw:: html

   </div>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="Python">





.. ref-code-block:: cpp

	infer_request = compiled_model.create_infer_request()





.. raw:: html

   </div>







.. raw:: html

   </div>





5. Fill Input Tensors with Data
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Inference Engine API**

The Inference Engine API fills inputs with data of the ``I32`` precision (**not** aligned with the original model):

.. raw:: html

   <div class='sphinxtabset'>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="IR v10">







.. raw:: html

   <div class='sphinxtabset'>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="C++">





.. ref-code-block:: cpp

	:ref:`InferenceEngine::Blob::Ptr <doxid-class_inference_engine_1_1_blob_1abb6c4f89181e2dd6d8a29ada2dfb4060>` input_blob1 = infer_request.GetBlob(inputs.begin()->first);
	// fill first blob
	:ref:`InferenceEngine::MemoryBlob::Ptr <doxid-class_inference_engine_1_1_memory_blob_1a294bf7449b6181f29ac05636a5968e1d>` minput1 = InferenceEngine::as<InferenceEngine::MemoryBlob>(input_blob1);
	if (minput1) {
	    // locked memory holder should be alive all time while access to its
	    // buffer happens
	    auto minputHolder = minput1->wmap();
	    // Original I64 precision was converted to I32
	    auto data = minputHolder.as<:ref:`InferenceEngine::PrecisionTrait\<InferenceEngine::Precision::I32>::value_type <doxid-struct_inference_engine_1_1_precision_trait>`\*>();
	    // Fill data ...
	}

	:ref:`InferenceEngine::Blob::Ptr <doxid-class_inference_engine_1_1_blob_1abb6c4f89181e2dd6d8a29ada2dfb4060>` input_blob2 = infer_request.GetBlob("data2");
	// fill first blob
	:ref:`InferenceEngine::MemoryBlob::Ptr <doxid-class_inference_engine_1_1_memory_blob_1a294bf7449b6181f29ac05636a5968e1d>` minput2 = InferenceEngine::as<InferenceEngine::MemoryBlob>(input_blob2);
	if (minput2) {
	    // locked memory holder should be alive all time while access to its
	    // buffer happens
	    auto minputHolder = minput2->wmap();
	    // Original I64 precision was converted to I32
	    auto data = minputHolder.as<:ref:`InferenceEngine::PrecisionTrait\<InferenceEngine::Precision::I32>::value_type <doxid-struct_inference_engine_1_1_precision_trait>`\*>();
	    // Fill data ...
	}





.. raw:: html

   </div>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="Python">





.. ref-code-block:: cpp

	infer_request = exec_network.requests[0]
	# Get input blobs mapped to input layers names
	input_blobs = infer_request.input_blobs
	data = input_blobs["data1"].buffer
	# Original I64 precision was converted to I32
	assert data.dtype == np.int32
	# Fill the first blob ...





.. raw:: html

   </div>







.. raw:: html

   </div>







.. raw:: html

   </div>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="IR v11">







.. raw:: html

   <div class='sphinxtabset'>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="C++">





.. ref-code-block:: cpp

	:ref:`InferenceEngine::Blob::Ptr <doxid-class_inference_engine_1_1_blob_1abb6c4f89181e2dd6d8a29ada2dfb4060>` input_blob1 = infer_request.GetBlob(inputs.begin()->first);
	// fill first blob
	:ref:`InferenceEngine::MemoryBlob::Ptr <doxid-class_inference_engine_1_1_memory_blob_1a294bf7449b6181f29ac05636a5968e1d>` minput1 = InferenceEngine::as<InferenceEngine::MemoryBlob>(input_blob1);
	if (minput1) {
	    // locked memory holder should be alive all time while access to its
	    // buffer happens
	    auto minputHolder = minput1->wmap();
	    // Original I64 precision was converted to I32
	    auto data = minputHolder.as<:ref:`InferenceEngine::PrecisionTrait\<InferenceEngine::Precision::I32>::value_type <doxid-struct_inference_engine_1_1_precision_trait>`\*>();
	    // Fill data ...
	}

	:ref:`InferenceEngine::Blob::Ptr <doxid-class_inference_engine_1_1_blob_1abb6c4f89181e2dd6d8a29ada2dfb4060>` input_blob2 = infer_request.GetBlob("data2");
	// fill first blob
	:ref:`InferenceEngine::MemoryBlob::Ptr <doxid-class_inference_engine_1_1_memory_blob_1a294bf7449b6181f29ac05636a5968e1d>` minput2 = InferenceEngine::as<InferenceEngine::MemoryBlob>(input_blob2);
	if (minput2) {
	    // locked memory holder should be alive all time while access to its
	    // buffer happens
	    auto minputHolder = minput2->wmap();
	    // Original I64 precision was converted to I32
	    auto data = minputHolder.as<:ref:`InferenceEngine::PrecisionTrait\<InferenceEngine::Precision::I32>::value_type <doxid-struct_inference_engine_1_1_precision_trait>`\*>();
	    // Fill data ...
	}





.. raw:: html

   </div>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="Python">





.. ref-code-block:: cpp

	infer_request = exec_network.requests[0]
	# Get input blobs mapped to input layers names
	input_blobs = infer_request.input_blobs
	data = input_blobs["data1"].buffer
	# Original I64 precision was converted to I32
	assert data.dtype == np.int32
	# Fill the first blob ...





.. raw:: html

   </div>







.. raw:: html

   </div>







.. raw:: html

   </div>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="ONNX">







.. raw:: html

   <div class='sphinxtabset'>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="C++">





.. ref-code-block:: cpp

	:ref:`InferenceEngine::Blob::Ptr <doxid-class_inference_engine_1_1_blob_1abb6c4f89181e2dd6d8a29ada2dfb4060>` input_blob1 = infer_request.GetBlob(inputs.begin()->first);
	// fill first blob
	:ref:`InferenceEngine::MemoryBlob::Ptr <doxid-class_inference_engine_1_1_memory_blob_1a294bf7449b6181f29ac05636a5968e1d>` minput1 = InferenceEngine::as<InferenceEngine::MemoryBlob>(input_blob1);
	if (minput1) {
	    // locked memory holder should be alive all time while access to its
	    // buffer happens
	    auto minputHolder = minput1->wmap();
	    // Original I64 precision was converted to I32
	    auto data = minputHolder.as<:ref:`InferenceEngine::PrecisionTrait\<InferenceEngine::Precision::I32>::value_type <doxid-struct_inference_engine_1_1_precision_trait>`\*>();
	    // Fill data ...
	}

	:ref:`InferenceEngine::Blob::Ptr <doxid-class_inference_engine_1_1_blob_1abb6c4f89181e2dd6d8a29ada2dfb4060>` input_blob2 = infer_request.GetBlob("data2");
	// fill first blob
	:ref:`InferenceEngine::MemoryBlob::Ptr <doxid-class_inference_engine_1_1_memory_blob_1a294bf7449b6181f29ac05636a5968e1d>` minput2 = InferenceEngine::as<InferenceEngine::MemoryBlob>(input_blob2);
	if (minput2) {
	    // locked memory holder should be alive all time while access to its
	    // buffer happens
	    auto minputHolder = minput2->wmap();
	    // Original I64 precision was converted to I32
	    auto data = minputHolder.as<:ref:`InferenceEngine::PrecisionTrait\<InferenceEngine::Precision::I32>::value_type <doxid-struct_inference_engine_1_1_precision_trait>`\*>();
	    // Fill data ...
	}





.. raw:: html

   </div>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="Python">





.. ref-code-block:: cpp

	infer_request = exec_network.requests[0]
	# Get input blobs mapped to input layers names
	input_blobs = infer_request.input_blobs
	data = input_blobs["data1"].buffer
	# Original I64 precision was converted to I32
	assert data.dtype == np.int32
	# Fill the first blob ...





.. raw:: html

   </div>







.. raw:: html

   </div>







.. raw:: html

   </div>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="Model created in code">







.. raw:: html

   <div class='sphinxtabset'>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="C++">





.. ref-code-block:: cpp

	:ref:`InferenceEngine::Blob::Ptr <doxid-class_inference_engine_1_1_blob_1abb6c4f89181e2dd6d8a29ada2dfb4060>` input_blob1 = infer_request.GetBlob(inputs.begin()->first);
	// fill first blob
	:ref:`InferenceEngine::MemoryBlob::Ptr <doxid-class_inference_engine_1_1_memory_blob_1a294bf7449b6181f29ac05636a5968e1d>` minput1 = InferenceEngine::as<InferenceEngine::MemoryBlob>(input_blob1);
	if (minput1) {
	    // locked memory holder should be alive all time while access to its
	    // buffer happens
	    auto minputHolder = minput1->wmap();
	    // Original I64 precision was converted to I32
	    auto data = minputHolder.as<:ref:`InferenceEngine::PrecisionTrait\<InferenceEngine::Precision::I32>::value_type <doxid-struct_inference_engine_1_1_precision_trait>`\*>();
	    // Fill data ...
	}

	:ref:`InferenceEngine::Blob::Ptr <doxid-class_inference_engine_1_1_blob_1abb6c4f89181e2dd6d8a29ada2dfb4060>` input_blob2 = infer_request.GetBlob("data2");
	// fill first blob
	:ref:`InferenceEngine::MemoryBlob::Ptr <doxid-class_inference_engine_1_1_memory_blob_1a294bf7449b6181f29ac05636a5968e1d>` minput2 = InferenceEngine::as<InferenceEngine::MemoryBlob>(input_blob2);
	if (minput2) {
	    // locked memory holder should be alive all time while access to its
	    // buffer happens
	    auto minputHolder = minput2->wmap();
	    // Original I64 precision was converted to I32
	    auto data = minputHolder.as<:ref:`InferenceEngine::PrecisionTrait\<InferenceEngine::Precision::I32>::value_type <doxid-struct_inference_engine_1_1_precision_trait>`\*>();
	    // Fill data ...
	}





.. raw:: html

   </div>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="Python">





.. ref-code-block:: cpp

	infer_request = exec_network.requests[0]
	# Get input blobs mapped to input layers names
	input_blobs = infer_request.input_blobs
	data = input_blobs["data1"].buffer
	# Original I64 precision was converted to I32
	assert data.dtype == np.int32
	# Fill the first blob ...





.. raw:: html

   </div>







.. raw:: html

   </div>







.. raw:: html

   </div>







.. raw:: html

   </div>



**API 2.0**

API 2.0 fills inputs with data of the ``I64`` precision (aligned with the original model):

.. _start-inference:

.. raw:: html

   <div class='sphinxtabset'>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="IR v10">







.. raw:: html

   <div class='sphinxtabset'>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="C++">





.. ref-code-block:: cpp

	// Get input tensor by index
	:ref:`ov::Tensor <doxid-classov_1_1_tensor>` input_tensor1 = infer_request.:ref:`get_input_tensor <doxid-classov_1_1_infer_request_1a5f0bc1ab40de6a7a12136b4a4e6a8b54>`(0);
	// IR v10 works with converted precisions (i64 -> i32)
	auto data1 = input_tensor1.:ref:`data <doxid-classov_1_1_tensor_1aaf6d1cd69a759b31c65fed8b3e7d66fb>`<int32_t>();
	// Fill first data ...

	// Get input tensor by tensor name
	:ref:`ov::Tensor <doxid-classov_1_1_tensor>` input_tensor2 = infer_request.:ref:`get_tensor <doxid-classov_1_1_infer_request_1a75b8da7c6b00686bede600dddceaffc4>`("data2_t");
	// IR v10 works with converted precisions (i64 -> i32)
	auto data2 = input_tensor1.:ref:`data <doxid-classov_1_1_tensor_1aaf6d1cd69a759b31c65fed8b3e7d66fb>`<int32_t>();
	// Fill first data ...





.. raw:: html

   </div>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="Python">





.. ref-code-block:: cpp

	# Get input tensor by index
	input_tensor1 = infer_request.get_input_tensor(0)
	# IR v10 works with converted precisions (i64 -> i32)
	assert input_tensor1.data.dtype == np.int32
	# Fill the first data ...
	
	# Get input tensor by tensor name
	input_tensor2 = infer_request.get_tensor("data2_t")
	# IR v10 works with converted precisions (i64 -> i32)
	assert input_tensor2.data.dtype == np.int32
	# Fill the second data ..





.. raw:: html

   </div>







.. raw:: html

   </div>







.. raw:: html

   </div>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="IR v11">







.. raw:: html

   <div class='sphinxtabset'>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="C++">





.. ref-code-block:: cpp

	// Get input tensor by index
	:ref:`ov::Tensor <doxid-classov_1_1_tensor>` input_tensor1 = infer_request.:ref:`get_input_tensor <doxid-classov_1_1_infer_request_1a5f0bc1ab40de6a7a12136b4a4e6a8b54>`(0);
	// Element types, names and layouts are aligned with framework
	auto data1 = input_tensor1.:ref:`data <doxid-classov_1_1_tensor_1aaf6d1cd69a759b31c65fed8b3e7d66fb>`<int64_t>();
	// Fill first data ...

	// Get input tensor by tensor name
	:ref:`ov::Tensor <doxid-classov_1_1_tensor>` input_tensor2 = infer_request.:ref:`get_tensor <doxid-classov_1_1_infer_request_1a75b8da7c6b00686bede600dddceaffc4>`("data2_t");
	// Element types, names and layouts are aligned with framework
	auto data2 = input_tensor1.:ref:`data <doxid-classov_1_1_tensor_1aaf6d1cd69a759b31c65fed8b3e7d66fb>`<int64_t>();
	// Fill first data ...





.. raw:: html

   </div>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="Python">





.. ref-code-block:: cpp

	# Get input tensor by index
	input_tensor1 = infer_request.get_input_tensor(0)
	# Element types, names and layouts are aligned with framework
	assert input_tensor1.data.dtype == np.int64
	# Fill the first data ...
	
	# Get input tensor by tensor name
	input_tensor2 = infer_request.get_tensor("data2_t")
	assert input_tensor2.data.dtype == np.int64
	# Fill the second data ...





.. raw:: html

   </div>







.. raw:: html

   </div>







.. raw:: html

   </div>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="ONNX">







.. raw:: html

   <div class='sphinxtabset'>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="C++">





.. ref-code-block:: cpp

	// Get input tensor by index
	:ref:`ov::Tensor <doxid-classov_1_1_tensor>` input_tensor1 = infer_request.:ref:`get_input_tensor <doxid-classov_1_1_infer_request_1a5f0bc1ab40de6a7a12136b4a4e6a8b54>`(0);
	// Element types, names and layouts are aligned with framework
	auto data1 = input_tensor1.:ref:`data <doxid-classov_1_1_tensor_1aaf6d1cd69a759b31c65fed8b3e7d66fb>`<int64_t>();
	// Fill first data ...

	// Get input tensor by tensor name
	:ref:`ov::Tensor <doxid-classov_1_1_tensor>` input_tensor2 = infer_request.:ref:`get_tensor <doxid-classov_1_1_infer_request_1a75b8da7c6b00686bede600dddceaffc4>`("data2_t");
	// Element types, names and layouts are aligned with framework
	auto data2 = input_tensor1.:ref:`data <doxid-classov_1_1_tensor_1aaf6d1cd69a759b31c65fed8b3e7d66fb>`<int64_t>();
	// Fill first data ...





.. raw:: html

   </div>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="Python">





.. ref-code-block:: cpp

	# Get input tensor by index
	input_tensor1 = infer_request.get_input_tensor(0)
	# Element types, names and layouts are aligned with framework
	assert input_tensor1.data.dtype == np.int64
	# Fill the first data ...
	
	# Get input tensor by tensor name
	input_tensor2 = infer_request.get_tensor("data2_t")
	assert input_tensor2.data.dtype == np.int64
	# Fill the second data ...





.. raw:: html

   </div>







.. raw:: html

   </div>







.. raw:: html

   </div>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="Model created in code">







.. raw:: html

   <div class='sphinxtabset'>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="C++">





.. ref-code-block:: cpp

	// Get input tensor by index
	:ref:`ov::Tensor <doxid-classov_1_1_tensor>` input_tensor1 = infer_request.:ref:`get_input_tensor <doxid-classov_1_1_infer_request_1a5f0bc1ab40de6a7a12136b4a4e6a8b54>`(0);
	// Element types, names and layouts are aligned with framework
	auto data1 = input_tensor1.:ref:`data <doxid-classov_1_1_tensor_1aaf6d1cd69a759b31c65fed8b3e7d66fb>`<int64_t>();
	// Fill first data ...

	// Get input tensor by tensor name
	:ref:`ov::Tensor <doxid-classov_1_1_tensor>` input_tensor2 = infer_request.:ref:`get_tensor <doxid-classov_1_1_infer_request_1a75b8da7c6b00686bede600dddceaffc4>`("data2_t");
	// Element types, names and layouts are aligned with framework
	auto data2 = input_tensor1.:ref:`data <doxid-classov_1_1_tensor_1aaf6d1cd69a759b31c65fed8b3e7d66fb>`<int64_t>();
	// Fill first data ...





.. raw:: html

   </div>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="Python">





.. ref-code-block:: cpp

	# Get input tensor by index
	input_tensor1 = infer_request.get_input_tensor(0)
	# Element types, names and layouts are aligned with framework
	assert input_tensor1.data.dtype == np.int64
	# Fill the first data ...
	
	# Get input tensor by tensor name
	input_tensor2 = infer_request.get_tensor("data2_t")
	assert input_tensor2.data.dtype == np.int64
	# Fill the second data ...





.. raw:: html

   </div>







.. raw:: html

   </div>







.. raw:: html

   </div>







.. raw:: html

   </div>





6. Start Inference
~~~~~~~~~~~~~~~~~~

**Inference Engine API**

.. raw:: html

   <div class='sphinxtabset'>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="Sync">







.. raw:: html

   <div class='sphinxtabset'>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="C++">





.. ref-code-block:: cpp

	infer_request.Infer();





.. raw:: html

   </div>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="Python">





.. ref-code-block:: cpp

	results = infer_request.infer()





.. raw:: html

   </div>







.. raw:: html

   </div>







.. raw:: html

   </div>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="Async">







.. raw:: html

   <div class='sphinxtabset'>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="C++">





.. ref-code-block:: cpp

	// NOTE: For demonstration purposes we are trying to set callback
	// which restarts inference inside one more time, so two inferences happen here

	// Start inference without blocking current thread
	auto restart_once = true;
	infer_request.SetCompletionCallback<:ref:`std::function <doxid-namespacengraph_1_1runtime_1_1reference_1a4bbb4f04db61c605971a3eb4c1553b6e>`<void(:ref:`InferenceEngine::InferRequest <doxid-class_inference_engine_1_1_infer_request>`, :ref:`InferenceEngine::StatusCode <doxid-namespace_inference_engine_1a2ce897aa6a353c071958fe379f5d6421>`)>>(
	    [&, restart_once](:ref:`InferenceEngine::InferRequest <doxid-class_inference_engine_1_1_infer_request>` request, :ref:`InferenceEngine::StatusCode <doxid-namespace_inference_engine_1a2ce897aa6a353c071958fe379f5d6421>` status) mutable {
	        if (status != :ref:`InferenceEngine::OK <doxid-namespace_inference_engine_1a2ce897aa6a353c071958fe379f5d6421a084fcaf510851d3281e7bd45db802c6a>`) {
	            // Process error code
	        } else {
	            // Extract inference result
	            :ref:`InferenceEngine::Blob::Ptr <doxid-class_inference_engine_1_1_blob_1abb6c4f89181e2dd6d8a29ada2dfb4060>` output_blob = request.GetBlob(outputs.begin()->first);
	            // Restart inference if needed
	            if (restart_once) {
	                request.StartAsync();
	                restart_once = false;
	            }
	        }
	    });
	infer_request.StartAsync();
	// Get inference status immediately
	:ref:`InferenceEngine::StatusCode <doxid-namespace_inference_engine_1a2ce897aa6a353c071958fe379f5d6421>` status = infer_request.Wait(:ref:`InferenceEngine::InferRequest::STATUS_ONLY <doxid-class_inference_engine_1_1_infer_request_1ac52c77df62b93f2f40b47ea232fde45aa50110aaf0c2f26c0cc71acf022d91698>`);
	// Wait for 1 milisecond
	status = infer_request.Wait(1);
	// Wait for inference completion
	infer_request.Wait(:ref:`InferenceEngine::InferRequest::RESULT_READY <doxid-class_inference_engine_1_1_infer_request_1ac52c77df62b93f2f40b47ea232fde45aaa71f7b3aaba799f92c75c52ac56897d8>`);





.. raw:: html

   </div>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="Python">





.. ref-code-block:: cpp

	# Start async inference on a single infer request
	infer_request.async_infer()
	# Wait for 1 milisecond
	infer_request.wait(1)
	# Wait for inference completion
	infer_request.wait()
	
	# Demonstrates async pipeline using ExecutableNetwork
	
	results = []
	
	# Callback to process inference results
	def callback(output_blobs, _):
	    # Copy the data from output blobs to numpy array
	    results_copy = {out_name: out_blob.buffer[:] for out_name, out_blob in output_blobs.items()}
	    results.append(process_results(results_copy))
	
	# Setting callback for each infer requests
	for infer_request in exec_network.requests:
	    infer_request.set_completion_callback(callback, py_data=infer_request.output_blobs)
	
	# Async pipline is managed by ExecutableNetwork
	total_frames = 100
	for _ in :ref:`range <doxid-namespacengraph_1_1runtime_1_1reference_1ad38dec78131946cded583cc1154a406d>`(total_frames):
	    # Wait for at least one free request
	    exec_network.wait(num_request=1)
	    # Get idle id
	    idle_id = exec_network.get_idle_request_id()
	    # Start asynchronous inference on idle request
	    exec_network.start_async(request_id=idle_id, inputs=next(input_data))
	# Wait for all requests to complete
	exec_network.wait()





.. raw:: html

   </div>







.. raw:: html

   </div>







.. raw:: html

   </div>







.. raw:: html

   </div>



**API 2.0**

.. _process-results:

.. raw:: html

   <div class='sphinxtabset'>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="Sync">







.. raw:: html

   <div class='sphinxtabset'>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="C++">





.. ref-code-block:: cpp

	infer_request.:ref:`infer <doxid-classov_1_1_infer_request_1abcb7facc9f7c4b9226a1fd343e56958d>`();





.. raw:: html

   </div>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="Python">





.. ref-code-block:: cpp

	results = infer_request.infer()





.. raw:: html

   </div>







.. raw:: html

   </div>







.. raw:: html

   </div>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="Async">







.. raw:: html

   <div class='sphinxtabset'>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="C++">





.. ref-code-block:: cpp

	// NOTE: For demonstration purposes we are trying to set callback
	// which restarts inference inside one more time, so two inferences happen here

	auto restart_once = true;
	infer_request.:ref:`set_callback <doxid-classov_1_1_infer_request_1afba2a10162ab356728ec8901973e8f02>`([&, restart_once](std::exception_ptr exception_ptr) mutable {
	    if (exception_ptr) {
	        // procces exception or rethrow it.
	        std::rethrow_exception(exception_ptr);
	    } else {
	        // Extract inference result
	        :ref:`ov::Tensor <doxid-classov_1_1_tensor>` output_tensor = infer_request.:ref:`get_output_tensor <doxid-classov_1_1_infer_request_1a350159a8d967022db46633eed50d073a>`();
	        // Restart inference if needed
	        if (restart_once) {
	            infer_request.:ref:`start_async <doxid-classov_1_1_infer_request_1a5a05ae4352f804c865e11f5d68b983d5>`();
	            restart_once = false;
	        }
	    }
	});
	// Start inference without blocking current thread
	infer_request.:ref:`start_async <doxid-classov_1_1_infer_request_1a5a05ae4352f804c865e11f5d68b983d5>`();
	// Get inference status immediately
	bool status = infer_request.:ref:`wait_for <doxid-classov_1_1_infer_request_1a94d6d52e03d2ad20310a1e0fdd807e9e>`(std::chrono::milliseconds{0});
	// Wait for one milisecond
	status = infer_request.:ref:`wait_for <doxid-classov_1_1_infer_request_1a94d6d52e03d2ad20310a1e0fdd807e9e>`(std::chrono::milliseconds{1});
	// Wait for inference completion
	infer_request.:ref:`wait <doxid-classov_1_1_infer_request_1ab0e0739da45789d816f8b5584a0b5691>`();





.. raw:: html

   </div>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="Python">





.. ref-code-block:: cpp

	# Start async inference on a single infer request
	infer_request.start_async()
	# Wait for 1 milisecond
	infer_request.wait_for(1)
	# Wait for inference completion
	infer_request.wait()
	
	# Demonstrates async pipeline using AsyncInferQueue
	
	results = []
	
	def callback(request, frame_id):
	    # Copy the data from output tensors to numpy array and process it
	    results_copy = {output: data[:] for output, data in request.results.items()}
	    results.append(process_results(results_copy, frame_id))
	
	# Create AsyncInferQueue with 4 infer requests
	infer_queue = ov.AsyncInferQueue(compiled_model, jobs=4)
	# Set callback for each infer request in the queue
	infer_queue.set_callback(callback)
	
	total_frames = 100
	for i in :ref:`range <doxid-namespacengraph_1_1runtime_1_1reference_1ad38dec78131946cded583cc1154a406d>`(total_frames):
	    # Wait for at least one available infer request and start asynchronous inference
	    infer_queue.start_async(next(input_data), userdata=i)
	# Wait for all requests to complete
	infer_queue.wait_all()





.. raw:: html

   </div>







.. raw:: html

   </div>







.. raw:: html

   </div>







.. raw:: html

   </div>





7. Process the Inference Results
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Inference Engine API**

The Inference Engine API processes outputs as they are of the ``I32`` precision (**not** aligned with the original model):

.. raw:: html

   <div class='sphinxtabset'>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="IR v10">







.. raw:: html

   <div class='sphinxtabset'>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="C++">





.. ref-code-block:: cpp

	:ref:`InferenceEngine::Blob::Ptr <doxid-class_inference_engine_1_1_blob_1abb6c4f89181e2dd6d8a29ada2dfb4060>` output_blob = infer_request.GetBlob(outputs.begin()->first);
	:ref:`InferenceEngine::MemoryBlob::Ptr <doxid-class_inference_engine_1_1_memory_blob_1a294bf7449b6181f29ac05636a5968e1d>` moutput = InferenceEngine::as<InferenceEngine::MemoryBlob>(output_blob);
	if (moutput) {
	    // locked memory holder should be alive all time while access to its
	    // buffer happens
	    auto minputHolder = moutput->rmap();
	    // Original I64 precision was converted to I32
	    auto data =
	        minputHolder.as<const :ref:`InferenceEngine::PrecisionTrait\<InferenceEngine::Precision::I32>::value_type <doxid-struct_inference_engine_1_1_precision_trait>`\*>();
	    // process output data
	}





.. raw:: html

   </div>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="Python">





.. ref-code-block:: cpp

	# Get output blobs mapped to output layers names
	output_blobs = infer_request.output_blobs
	data = output_blobs["out1"].buffer
	# Original I64 precision was converted to I32
	assert data.dtype == np.int32
	# Process output data





.. raw:: html

   </div>







.. raw:: html

   </div>







.. raw:: html

   </div>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="IR v11">







.. raw:: html

   <div class='sphinxtabset'>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="C++">





.. ref-code-block:: cpp

	:ref:`InferenceEngine::Blob::Ptr <doxid-class_inference_engine_1_1_blob_1abb6c4f89181e2dd6d8a29ada2dfb4060>` output_blob = infer_request.GetBlob(outputs.begin()->first);
	:ref:`InferenceEngine::MemoryBlob::Ptr <doxid-class_inference_engine_1_1_memory_blob_1a294bf7449b6181f29ac05636a5968e1d>` moutput = InferenceEngine::as<InferenceEngine::MemoryBlob>(output_blob);
	if (moutput) {
	    // locked memory holder should be alive all time while access to its
	    // buffer happens
	    auto minputHolder = moutput->rmap();
	    // Original I64 precision was converted to I32
	    auto data =
	        minputHolder.as<const :ref:`InferenceEngine::PrecisionTrait\<InferenceEngine::Precision::I32>::value_type <doxid-struct_inference_engine_1_1_precision_trait>`\*>();
	    // process output data
	}





.. raw:: html

   </div>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="Python">





.. ref-code-block:: cpp

	# Get output blobs mapped to output layers names
	output_blobs = infer_request.output_blobs
	data = output_blobs["out1"].buffer
	# Original I64 precision was converted to I32
	assert data.dtype == np.int32
	# Process output data





.. raw:: html

   </div>







.. raw:: html

   </div>







.. raw:: html

   </div>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="ONNX">







.. raw:: html

   <div class='sphinxtabset'>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="C++">





.. ref-code-block:: cpp

	:ref:`InferenceEngine::Blob::Ptr <doxid-class_inference_engine_1_1_blob_1abb6c4f89181e2dd6d8a29ada2dfb4060>` output_blob = infer_request.GetBlob(outputs.begin()->first);
	:ref:`InferenceEngine::MemoryBlob::Ptr <doxid-class_inference_engine_1_1_memory_blob_1a294bf7449b6181f29ac05636a5968e1d>` moutput = InferenceEngine::as<InferenceEngine::MemoryBlob>(output_blob);
	if (moutput) {
	    // locked memory holder should be alive all time while access to its
	    // buffer happens
	    auto minputHolder = moutput->rmap();
	    // Original I64 precision was converted to I32
	    auto data =
	        minputHolder.as<const :ref:`InferenceEngine::PrecisionTrait\<InferenceEngine::Precision::I32>::value_type <doxid-struct_inference_engine_1_1_precision_trait>`\*>();
	    // process output data
	}





.. raw:: html

   </div>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="Python">





.. ref-code-block:: cpp

	# Get output blobs mapped to output layers names
	output_blobs = infer_request.output_blobs
	data = output_blobs["out1"].buffer
	# Original I64 precision was converted to I32
	assert data.dtype == np.int32
	# Process output data





.. raw:: html

   </div>







.. raw:: html

   </div>







.. raw:: html

   </div>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="Model created in code">







.. raw:: html

   <div class='sphinxtabset'>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="C++">





.. ref-code-block:: cpp

	:ref:`InferenceEngine::Blob::Ptr <doxid-class_inference_engine_1_1_blob_1abb6c4f89181e2dd6d8a29ada2dfb4060>` output_blob = infer_request.GetBlob(outputs.begin()->first);
	:ref:`InferenceEngine::MemoryBlob::Ptr <doxid-class_inference_engine_1_1_memory_blob_1a294bf7449b6181f29ac05636a5968e1d>` moutput = InferenceEngine::as<InferenceEngine::MemoryBlob>(output_blob);
	if (moutput) {
	    // locked memory holder should be alive all time while access to its
	    // buffer happens
	    auto minputHolder = moutput->rmap();
	    // Original I64 precision was converted to I32
	    auto data =
	        minputHolder.as<const :ref:`InferenceEngine::PrecisionTrait\<InferenceEngine::Precision::I32>::value_type <doxid-struct_inference_engine_1_1_precision_trait>`\*>();
	    // process output data
	}





.. raw:: html

   </div>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="Python">





.. ref-code-block:: cpp

	# Get output blobs mapped to output layers names
	output_blobs = infer_request.output_blobs
	data = output_blobs["out1"].buffer
	# Original I64 precision was converted to I32
	assert data.dtype == np.int32
	# Process output data





.. raw:: html

   </div>







.. raw:: html

   </div>







.. raw:: html

   </div>







.. raw:: html

   </div>



**API 2.0**

API 2.0 processes outputs:

* as they are of the ``I32`` precision (**not** aligned with the original model) for OpenVINO IR v10 models, to match the `old behavior <openvino_2_0_transition_guide#differences-api20-ie>`__.

* as they are of the ``I64`` precision (aligned with the original model) for OpenVINO IR v11, ONNX, :ref:`ov::Model <doxid-classov_1_1_model>` and PaddlePaddle models, to match the `new behavior <openvino_2_0_transition_guide#differences-api20-ie>`__.

.. raw:: html

   <div class='sphinxtabset'>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="IR v10">







.. raw:: html

   <div class='sphinxtabset'>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="C++">





.. ref-code-block:: cpp

	// model has only one output
	:ref:`ov::Tensor <doxid-classov_1_1_tensor>` output_tensor = infer_request.:ref:`get_output_tensor <doxid-classov_1_1_infer_request_1a350159a8d967022db46633eed50d073a>`();
	// IR v10 works with converted precisions (i64 -> i32)
	auto out_data = output_tensor.:ref:`data <doxid-classov_1_1_tensor_1aaf6d1cd69a759b31c65fed8b3e7d66fb>`<int32_t>();
	// process output data





.. raw:: html

   </div>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="Python">





.. ref-code-block:: cpp

	# Model has only one output
	output_tensor = infer_request.get_output_tensor()
	# IR v10 works with converted precisions (i64 -> i32)
	assert output_tensor.data.dtype == np.int32
	# process output data ...





.. raw:: html

   </div>







.. raw:: html

   </div>







.. raw:: html

   </div>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="IR v11">







.. raw:: html

   <div class='sphinxtabset'>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="C++">





.. ref-code-block:: cpp

	// model has only one output
	:ref:`ov::Tensor <doxid-classov_1_1_tensor>` output_tensor = infer_request.:ref:`get_output_tensor <doxid-classov_1_1_infer_request_1a350159a8d967022db46633eed50d073a>`();
	// Element types, names and layouts are aligned with framework
	auto out_data = output_tensor.:ref:`data <doxid-classov_1_1_tensor_1aaf6d1cd69a759b31c65fed8b3e7d66fb>`<int64_t>();
	// process output data





.. raw:: html

   </div>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="Python">





.. ref-code-block:: cpp

	# Model has only one output
	output_tensor = infer_request.get_output_tensor()
	# Element types, names and layouts are aligned with framework
	assert output_tensor.data.dtype == np.int64
	# process output data ...





.. raw:: html

   </div>







.. raw:: html

   </div>







.. raw:: html

   </div>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="ONNX">







.. raw:: html

   <div class='sphinxtabset'>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="C++">





.. ref-code-block:: cpp

	// model has only one output
	:ref:`ov::Tensor <doxid-classov_1_1_tensor>` output_tensor = infer_request.:ref:`get_output_tensor <doxid-classov_1_1_infer_request_1a350159a8d967022db46633eed50d073a>`();
	// Element types, names and layouts are aligned with framework
	auto out_data = output_tensor.:ref:`data <doxid-classov_1_1_tensor_1aaf6d1cd69a759b31c65fed8b3e7d66fb>`<int64_t>();
	// process output data





.. raw:: html

   </div>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="Python">





.. ref-code-block:: cpp

	# Model has only one output
	output_tensor = infer_request.get_output_tensor()
	# Element types, names and layouts are aligned with framework
	assert output_tensor.data.dtype == np.int64
	# process output data ...





.. raw:: html

   </div>







.. raw:: html

   </div>







.. raw:: html

   </div>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="Model created in code">







.. raw:: html

   <div class='sphinxtabset'>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="C++">





.. ref-code-block:: cpp

	// model has only one output
	:ref:`ov::Tensor <doxid-classov_1_1_tensor>` output_tensor = infer_request.:ref:`get_output_tensor <doxid-classov_1_1_infer_request_1a350159a8d967022db46633eed50d073a>`();
	// Element types, names and layouts are aligned with framework
	auto out_data = output_tensor.:ref:`data <doxid-classov_1_1_tensor_1aaf6d1cd69a759b31c65fed8b3e7d66fb>`<int64_t>();
	// process output data





.. raw:: html

   </div>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="Python">





.. ref-code-block:: cpp

	# Model has only one output
	output_tensor = infer_request.get_output_tensor()
	# Element types, names and layouts are aligned with framework
	assert output_tensor.data.dtype == np.int64
	# process output data ...





.. raw:: html

   </div>







.. raw:: html

   </div>







.. raw:: html

   </div>







.. raw:: html

   </div>

