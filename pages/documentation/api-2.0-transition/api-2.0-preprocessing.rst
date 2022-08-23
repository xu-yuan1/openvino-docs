.. index:: pair: page; Preprocessing
.. _doxid-openvino_2_0_preprocessing:


Preprocessing
=============

:target:`doxid-openvino_2_0_preprocessing_1md_openvino_docs_ov_runtime_ug_migration_ov_2_0_preprocessing` This guide introduces how preprocessing works in API 2.0 by a comparison with preprocessing in the previous Inference Engine API. It also demonstrates how to migrate preprocessing scenarios from Inference Engine to API 2.0 via code samples.

How Preprocessing Works in API 2.0
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Inference Engine API contains preprocessing capabilities in the ``:ref:`InferenceEngine::CNNNetwork <doxid-class_inference_engine_1_1_c_n_n_network>``` class. Such preprocessing information is not a part of the main inference graph executed by :ref:`OpenVINO devices <doxid-openvino_docs__o_v__u_g__working_with_devices>`. Therefore, it is stored and executed separately before the inference stage:

* Preprocessing operations are executed on the CPU for most OpenVINO inference plugins. Thus, instead of occupying accelerators, they keep the CPU busy with computational tasks.

* Preprocessing information stored in ``:ref:`InferenceEngine::CNNNetwork <doxid-class_inference_engine_1_1_c_n_n_network>``` is lost when saving back to the OpenVINO IR file format.

API 2.0 introduces a :ref:`new way of adding preprocessing operations to the model <doxid-openvino_docs__o_v__u_g__preprocessing__overview>` - each preprocessing or post-processing operation is integrated directly into the model and compiled together with the inference graph:

* API 2.0 first adds preprocessing operations by using ``:ref:`ov::preprocess::PrePostProcessor <doxid-classov_1_1preprocess_1_1_pre_post_processor>```,

* and then compiles the model on the target by using ``:ref:`ov::Core::compile_model <doxid-classov_1_1_core_1a46555f0803e8c29524626be08e7f5c5a>```.

Having preprocessing operations as a part of an OpenVINO opset makes it possible to read and serialize a preprocessed model as the OpenVINO™ IR file format.

More importantly, API 2.0 does not assume any default layouts as Inference Engine did. For example, both ``{ 1, 224, 224, 3 }`` and ``{ 1, 3, 224, 224 }`` shapes are supposed to be in the ``NCHW`` layout, while only the latter is. Therefore, some preprocessing capabilities in the API require layouts to be set explicitly. To learn how to do it, refer to the :ref:`Layout overview <doxid-openvino_docs__o_v__u_g__layout__overview>`. For example, to perform image scaling by partial dimensions ``H`` and ``W``, preprocessing needs to know what dimensions ``H`` and ``W`` are.

.. note:: Use Model Optimizer preprocessing capabilities to insert preprocessing operations in your model for optimization. Thus, the application does not need to read the model and set preprocessing repeatedly. You can use the :ref:`model caching feature <model_caching_overview>` to improve the time-to-inference.



The following sections demonstrate how to migrate preprocessing scenarios from Inference Engine API to API 2.0. The snippets assume that you need to preprocess a model input with the ``tensor_name`` in Inference Engine API, using ``operation_name`` to address the data.

Preparation: Import Preprocessing in Python
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In order to utilize preprocessing, the following imports must be added.

**Inference Engine API**

.. ref-code-block:: cpp

	import openvino.inference_engine as ie

**API 2.0**

.. ref-code-block:: cpp

	from openvino.runtime import Core, Layout, Type
	from openvino.preprocess import ColorFormat, PrePostProcessor, ResizeAlgorithm

There are two different namespaces:

* ``runtime``, which contains API 2.0 classes;

* and ``preprocess``, which provides Preprocessing API.

Using Mean and Scale Values
~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Inference Engine API**

.. raw:: html

   <div class='sphinxtabset'>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="C++">





.. ref-code-block:: cpp

	auto preProcess = network.getInputsInfo()[operation_name]->getPreProcess();
	preProcess.init(3);
	preProcess[0]->meanValue = 116.78f;
	preProcess[1]->meanValue = 116.78f;
	preProcess[2]->meanValue = 116.78f;
	preProcess[0]->stdScale = 57.21f;
	preProcess[1]->stdScale = 57.45f;
	preProcess[2]->stdScale = 57.73f;
	preProcess.setVariant(:ref:`InferenceEngine::MEAN_VALUE <doxid-namespace_inference_engine_1a02a50369bd2f3354578072f5e4e98161a782a36934a315c43f504c04924ca5f26>`);

.. raw:: html

   </div>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="Python">





.. ref-code-block:: cpp

	preProcess = network.getInputsInfo()[operation_name].getPreProcess()
	preProcess.init(3)
	preProcess[0].meanValue = 116.78
	preProcess[1].meanValue = 116.78
	preProcess[2].meanValue = 116.78
	preProcess[0].stdScale = 57.21
	preProcess[1].stdScale = 57.45
	preProcess[2].stdScale = 57.73
	preProcess.setVariant(ie.MEAN_VALUE)

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

	:ref:`ov::preprocess::PrePostProcessor <doxid-classov_1_1preprocess_1_1_pre_post_processor>` ppp(:ref:`model <doxid-group__ov__runtime__cpp__prop__api_1ga461856fdfb6d7533dc53355aec9e9fad>`);
	:ref:`ov::preprocess::InputInfo <doxid-classov_1_1preprocess_1_1_input_info>`& input = ppp.input(tensor_name);
	// we only need to know where is C dimension
	input.:ref:`model <doxid-classov_1_1preprocess_1_1_input_info_1a7a1ddc0dea4daa83998995e491adf667>`().:ref:`set_layout <doxid-classov_1_1preprocess_1_1_input_model_info_1af309bac02af20d048e349a2d421c1169>`("...C");
	// specify scale and mean values, order of operations is important
	input.:ref:`preprocess <doxid-classov_1_1preprocess_1_1_input_info_1afaeba871501b27522b96f39a3d91f35e>`().:ref:`mean <doxid-classov_1_1preprocess_1_1_pre_process_steps_1aef1bb8c1fc5eb0014b07b78749c432dc>`(116.78f).:ref:`scale <doxid-classov_1_1preprocess_1_1_pre_process_steps_1aeacaf406d72a238e31a359798ebdb3b7>`({ 57.21f, 57.45f, 57.73f });
	// insert preprocessing operations to the 'model'
	:ref:`model <doxid-group__ov__runtime__cpp__prop__api_1ga461856fdfb6d7533dc53355aec9e9fad>` = ppp.build();

.. raw:: html

   </div>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="Python">





.. ref-code-block:: cpp

	ppp = PrePostProcessor(model)
	input = ppp.input(tensor_name)
	# we only need to know where is C dimension
	input.model().:ref:`set_layout <doxid-group__ov__layout__cpp__api_1ga18464fb8ed029acb5fdc2bb1737358d9>`(:ref:`Layout <doxid-namespace_inference_engine_1a246d143abc5ca07da8d2cadeeb88fdb8>`('...C'))
	# specify scale and mean values, order of operations is important
	input.preprocess().:ref:`mean <doxid-namespacengraph_1_1builder_1_1opset1_1a06c7367d66f6e48931cbdf49c696d8c9>`([116.78]).scale([57.21, 57.45, 57.73])
	# insert preprocessing operations to the 'model'
	model = ppp.build()

.. raw:: html

   </div>







.. raw:: html

   </div>





Converting Precision and Layout
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Inference Engine API**

.. raw:: html

   <div class='sphinxtabset'>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="C++">





.. ref-code-block:: cpp

	auto inputInfo = network.getInputsInfo()[operation_name];
	inputInfo->setPrecision(:ref:`InferenceEngine::Precision::U8 <doxid-class_inference_engine_1_1_precision_1ade75bd7073b4aa966c0dda4025bcd0f5a046eaf31a4345f526ed54271c9fcd39c>`);
	inputInfo->setLayout(:ref:`InferenceEngine::Layout::NHWC <doxid-namespace_inference_engine_1a246d143abc5ca07da8d2cadeeb88fdb8aa5bfc87d4f0e3d8d55738659e9f54a0f>`);
	// model input layout is always NCHW in Inference Engine
	// for shapes with 4 dimensions

.. raw:: html

   </div>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="Python">





.. ref-code-block:: cpp

	inputInfo = network.getInputsInfo()[operation_name]
	inputInfo.setPrecision(ie.Precision.U8)
	inputInfo.setLayout(ie.Layout.NHWC)
	# model input layout is always NCHW in Inference Engine
	# for shapes with 4 dimensions

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

	:ref:`ov::preprocess::PrePostProcessor <doxid-classov_1_1preprocess_1_1_pre_post_processor>` ppp(:ref:`model <doxid-group__ov__runtime__cpp__prop__api_1ga461856fdfb6d7533dc53355aec9e9fad>`);
	:ref:`ov::preprocess::InputInfo <doxid-classov_1_1preprocess_1_1_input_info>`& input = ppp.input(tensor_name);
	input.:ref:`tensor <doxid-classov_1_1preprocess_1_1_input_info_1a7385ef9e3f1c61a87ddee256684638ae>`().:ref:`set_layout <doxid-classov_1_1preprocess_1_1_input_tensor_info_1a6f70eb97d02e90a30cd748573abd7b4b>`("NHWC").:ref:`set_element_type <doxid-classov_1_1preprocess_1_1_input_tensor_info_1a98fb73ff9178c8c71d809ddf8927faf5>`(:ref:`ov::element::u8 <doxid-group__ov__element__cpp__api_1gaaf60c536d3e295285f6a899eb3d29e2f>`);
	input.:ref:`model <doxid-classov_1_1preprocess_1_1_input_info_1a7a1ddc0dea4daa83998995e491adf667>`().:ref:`set_layout <doxid-classov_1_1preprocess_1_1_input_model_info_1af309bac02af20d048e349a2d421c1169>`("NCHW");
	// layout and precision conversion is inserted automatically,
	// because tensor format != model input format
	:ref:`model <doxid-group__ov__runtime__cpp__prop__api_1ga461856fdfb6d7533dc53355aec9e9fad>` = ppp.build();

.. raw:: html

   </div>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="Python">





.. ref-code-block:: cpp

	ppp = PrePostProcessor(model)
	input = ppp.input(tensor_name)
	input.tensor().:ref:`set_layout <doxid-group__ov__layout__cpp__api_1ga18464fb8ed029acb5fdc2bb1737358d9>`(:ref:`Layout <doxid-namespace_inference_engine_1a246d143abc5ca07da8d2cadeeb88fdb8>`('NCHW')).set_element_type(Type.u8)
	input.model().:ref:`set_layout <doxid-group__ov__layout__cpp__api_1ga18464fb8ed029acb5fdc2bb1737358d9>`(:ref:`Layout <doxid-namespace_inference_engine_1a246d143abc5ca07da8d2cadeeb88fdb8>`('NCHW'))
	# layout and precision conversion is inserted automatically,
	# because tensor format != model input format
	model = ppp.build()

.. raw:: html

   </div>







.. raw:: html

   </div>





Using Image Scaling
~~~~~~~~~~~~~~~~~~~

**Inference Engine API**

.. raw:: html

   <div class='sphinxtabset'>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="C++">





.. ref-code-block:: cpp

	auto preProcess = network.getInputsInfo()[operation_name]->getPreProcess();
	// Inference Engine supposes input for resize is always in NCHW layout
	// while for OpenVINO Runtime API 2.0 `H` and `W` dimensions must be specified
	// Also, current code snippet supposed resize from dynamic shapes
	preProcess.setResizeAlgorithm(:ref:`InferenceEngine::ResizeAlgorithm::RESIZE_BILINEAR <doxid-namespace_inference_engine_1a805a09efb0e7b327ffa078f8d02222e9a069d0555eb598a08d5540adb10b759c5>`);

.. raw:: html

   </div>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="Python">





.. ref-code-block:: cpp

	preProcess = network.getInputsInfo()[operation_name].getPreProcess()
	# Inference Engine supposes input for resize is always in NCHW layout
	# while for OpenVINO Runtime API 2.0 `H` and `W` dimensions must be specified
	# Also, current code snippet supposed resize from dynamic shapes
	preProcess.setResizeAlgorithm(ie.ResizeAlgorithm.RESIZE_BILINEAR)

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

	:ref:`ov::preprocess::PrePostProcessor <doxid-classov_1_1preprocess_1_1_pre_post_processor>` ppp(:ref:`model <doxid-group__ov__runtime__cpp__prop__api_1ga461856fdfb6d7533dc53355aec9e9fad>`);
	:ref:`ov::preprocess::InputInfo <doxid-classov_1_1preprocess_1_1_input_info>`& input = ppp.input(tensor_name);
	// scale from the specified tensor size
	input.:ref:`tensor <doxid-classov_1_1preprocess_1_1_input_info_1a7385ef9e3f1c61a87ddee256684638ae>`().:ref:`set_spatial_static_shape <doxid-classov_1_1preprocess_1_1_input_tensor_info_1a6f203e0b267549c1ee59bdb5606ef9d1>`(448, 448);
	// need to specify H and W dimensions in model, others are not important
	input.:ref:`model <doxid-classov_1_1preprocess_1_1_input_info_1a7a1ddc0dea4daa83998995e491adf667>`().:ref:`set_layout <doxid-classov_1_1preprocess_1_1_input_model_info_1af309bac02af20d048e349a2d421c1169>`("??HW");
	// scale to model shape
	input.:ref:`preprocess <doxid-classov_1_1preprocess_1_1_input_info_1afaeba871501b27522b96f39a3d91f35e>`().:ref:`resize <doxid-classov_1_1preprocess_1_1_pre_process_steps_1a40dab78be1222fee505ed6a13400efe6>`(:ref:`ov::preprocess::ResizeAlgorithm::RESIZE_LINEAR <doxid-namespaceov_1_1preprocess_1a8665e295e222dc2120be3550e04db8f3a8803101bcf6d2ec700e6e7358217db68>`);
	// and insert operations to the model
	:ref:`model <doxid-group__ov__runtime__cpp__prop__api_1ga461856fdfb6d7533dc53355aec9e9fad>` = ppp.build();

.. raw:: html

   </div>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="Python">





.. ref-code-block:: cpp

	ppp = PrePostProcessor(model)
	input = ppp.input(tensor_name)
	# need to specify H and W dimensions in model, others are not important
	input.model().:ref:`set_layout <doxid-group__ov__layout__cpp__api_1ga18464fb8ed029acb5fdc2bb1737358d9>`(:ref:`Layout <doxid-namespace_inference_engine_1a246d143abc5ca07da8d2cadeeb88fdb8>`('??HW'))
	# scale to model shape
	input.preprocess().resize(ResizeAlgorithm.RESIZE_LINEAR, 448, 448)
	# and insert operations to the model
	model = ppp.build()

.. raw:: html

   </div>







.. raw:: html

   </div>





Converting Color Space
----------------------

**Inference Engine API**

.. raw:: html

   <div class='sphinxtabset'>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="C++">





.. ref-code-block:: cpp

	auto preProcess = network.getInputsInfo()[operation_name]->getPreProcess();
	// Inference Engine supposes NV12 as two inputs which need to be passed
	// as InferenceEngine::NV12Blob composed of two Y and UV planes
	preProcess.setColorFormat(:ref:`InferenceEngine::NV12 <doxid-namespace_inference_engine_1a5ee5ca7708cc67a9a0becc2593d0558aa502b46f938a363e107246de8b1c90dc7>`);

.. raw:: html

   </div>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="Python">





.. ref-code-block:: cpp

	
	preProcess = network.getInputsInfo()[operation_name].getPreProcess()
	# Inference Engine supposes NV12 as two inputs which need to be passed
	# as InferenceEngine::NV12Blob composed of two Y and UV planes
	preProcess.setColorFormat(ie.NV12)

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

	:ref:`ov::preprocess::PrePostProcessor <doxid-classov_1_1preprocess_1_1_pre_post_processor>` ppp(:ref:`model <doxid-group__ov__runtime__cpp__prop__api_1ga461856fdfb6d7533dc53355aec9e9fad>`);
	:ref:`ov::preprocess::InputInfo <doxid-classov_1_1preprocess_1_1_input_info>`& input = ppp.input(tensor_name);
	input.:ref:`tensor <doxid-classov_1_1preprocess_1_1_input_info_1a7385ef9e3f1c61a87ddee256684638ae>`().:ref:`set_color_format <doxid-classov_1_1preprocess_1_1_input_tensor_info_1a3201ba0fab221038f87a5bca455e39d7>`(:ref:`ov::preprocess::ColorFormat::NV12_TWO_PLANES <doxid-namespaceov_1_1preprocess_1ab027f26e58038e454e1b50a5243f1707a54f60c652650de96e9d118187b3ba25f>`);
	// add NV12 to BGR conversion
	input.:ref:`preprocess <doxid-classov_1_1preprocess_1_1_input_info_1afaeba871501b27522b96f39a3d91f35e>`().:ref:`convert_color <doxid-classov_1_1preprocess_1_1_pre_process_steps_1a4f062246cc0082822346c97917903983>`(:ref:`ov::preprocess::ColorFormat::BGR <doxid-namespaceov_1_1preprocess_1ab027f26e58038e454e1b50a5243f1707a2ad5640ebdec72fc79531d1778c6c2dc>`);
	// and insert operations to the model
	:ref:`model <doxid-group__ov__runtime__cpp__prop__api_1ga461856fdfb6d7533dc53355aec9e9fad>` = ppp.build();

.. raw:: html

   </div>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="Python">





.. ref-code-block:: cpp

	ppp = PrePostProcessor(model)
	input = ppp.input(tensor_name)
	input.tensor().set_color_format(ColorFormat.NV12_TWO_PLANES)
	# add NV12 to BGR conversion
	input.preprocess().convert_color(ColorFormat.BGR)
	# and insert operations to the model
	model = ppp.build()

.. raw:: html

   </div>







.. raw:: html

   </div>

Additional Resources
~~~~~~~~~~~~~~~~~~~~

* :ref:`Preprocessing details <doxid-openvino_docs__o_v__u_g__preprocessing__details>`

* :ref:`NV12 classification sample <doxid-openvino_inference_engine_samples_hello_nv12_input_classification__r_e_a_d_m_e>`

