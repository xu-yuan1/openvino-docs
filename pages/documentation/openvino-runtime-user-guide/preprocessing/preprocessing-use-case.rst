.. index:: pair: page; Use Case - Integrate and Save Preprocessing Steps Into IR
.. _doxid-openvino_docs__o_v__u_g__preprocess__usecase_save:


Use Case - Integrate and Save Preprocessing Steps Into IR
=========================================================

:target:`doxid-openvino_docs__o_v__u_g__preprocess__usecase_save_1md_openvino_docs_ov_runtime_ug_preprocessing_usecase_save`

Previous sections covered the topic of the :ref:`preprocessing steps <doxid-openvino_docs__o_v__u_g__preprocessing__details>` and the overview of :ref:`Layout <doxid-openvino_docs__o_v__u_g__layout__overview>` API.

For many applications, it is also important to minimize read/load time of a model. Therefore, performing integration of preprocessing steps every time on application startup, after ``ov::runtime::Core::read_model``, may seem inconvenient. In such cases, once pre and postprocessing steps have been added, it can be useful to store new execution model to OpenVINO Intermediate Representation (OpenVINO IR, ``.xml`` format).

Most available preprocessing steps can also be performed via command-line options, using Model Optimizer. For details on such command-line options, refer to the :ref:`Optimizing Preprocessing Computation <doxid-openvino_docs__m_o__d_g__additional__optimization__use__cases>`.

Code example - Saving Model with Preprocessing to OpenVINO IR
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When some preprocessing steps cannot be integrated into the execution graph using Model Optimizer command-line options (for example, ``YUV`` -> ``RGB`` color space conversion, ``Resize``, etc.), it is possible to write a simple code which:

* Reads the original model (OpenVINO IR, ONNX, PaddlePaddle).

* Adds the preprocessing/postprocessing steps.

* Saves resulting model as IR (``.xml`` and ``.bin``).

Consider the example, where an original ONNX model takes one ``float32`` input with the ``{1, 3, 224, 224}`` shape, the ``RGB`` channel order, and mean/scale values applied. In contrast, the application provides ``BGR`` image buffer with a non-fixed size and input images as batches of two. Below is the model conversion code that can be applied in the model preparation script for such a case.

* Includes / Imports

.. raw:: html

   <div class='sphinxtabset'>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="C++">





.. ref-code-block:: cpp

	#include <openvino/runtime/core.hpp>
	#include <openvino/core/preprocess/pre_post_process.hpp>
	#include <openvino/pass/serialize.hpp>

.. raw:: html

   </div>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="Python">





.. ref-code-block:: cpp

	from openvino.preprocess import PrePostProcessor, ColorFormat, ResizeAlgorithm
	from openvino.runtime import Core, Layout, Type, set_batch
	from openvino.runtime.passes import Manager

.. raw:: html

   </div>







.. raw:: html

   </div>





* Preprocessing & Saving to the OpenVINO IR code.

.. raw:: html

   <div class='sphinxtabset'>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="C++">





.. ref-code-block:: cpp

	// ========  Step 0: read original model =========
	:ref:`ov::Core <doxid-classov_1_1_core>` core;
	std::shared_ptr<ov::Model> :ref:`model <doxid-group__ov__runtime__cpp__prop__api_1ga461856fdfb6d7533dc53355aec9e9fad>` = core.:ref:`read_model <doxid-classov_1_1_core_1ae0576a95f841c3a6f5e46e4802716981>`("/path/to/some_model.onnx");

	// ======== Step 1: Preprocessing ================
	:ref:`ov::preprocess::PrePostProcessor <doxid-classov_1_1preprocess_1_1_pre_post_processor>` prep(:ref:`model <doxid-group__ov__runtime__cpp__prop__api_1ga461856fdfb6d7533dc53355aec9e9fad>`);
	// Declare section of desired application's input format
	prep.input().tensor()
	       .set_element_type(:ref:`ov::element::u8 <doxid-group__ov__element__cpp__api_1gaaf60c536d3e295285f6a899eb3d29e2f>`)
	       .set_layout("NHWC")
	       .set_color_format(:ref:`ov::preprocess::ColorFormat::BGR <doxid-namespaceov_1_1preprocess_1ab027f26e58038e454e1b50a5243f1707a2ad5640ebdec72fc79531d1778c6c2dc>`)
	       .set_spatial_dynamic_shape();
	// Specify actual model layout
	prep.input().model()
	       .set_layout("NCHW");
	// Explicit preprocessing steps. Layout conversion will be done automatically as last step
	prep.input().preprocess()
	       .convert_element_type()
	       .convert_color(:ref:`ov::preprocess::ColorFormat::RGB <doxid-namespaceov_1_1preprocess_1ab027f26e58038e454e1b50a5243f1707a889574aebacda6bfd3e534e2b49b8028>`)
	       .resize(:ref:`ov::preprocess::ResizeAlgorithm::RESIZE_LINEAR <doxid-namespaceov_1_1preprocess_1a8665e295e222dc2120be3550e04db8f3a8803101bcf6d2ec700e6e7358217db68>`)
	       .mean({123.675, 116.28, 103.53}) // Subtract mean after color conversion
	       .scale({58.624, 57.12, 57.375});
	// Dump preprocessor
	std::cout << "Preprocessor: " << prep << std::endl;
	:ref:`model <doxid-group__ov__runtime__cpp__prop__api_1ga461856fdfb6d7533dc53355aec9e9fad>` = prep.build();

	// ======== Step 2: Change batch size ================
	// In this example we also want to change batch size to increase throughput
	:ref:`ov::set_batch <doxid-namespaceov_1a3314e2ff91fcc9ffec05b1a77c37862b>`(:ref:`model <doxid-group__ov__runtime__cpp__prop__api_1ga461856fdfb6d7533dc53355aec9e9fad>`, 2);

	// ======== Step 3: Save the model ================
	std::string xml = "/path/to/some_model_saved.xml";
	std::string bin = "/path/to/some_model_saved.bin";
	:ref:`ov::serialize <doxid-namespaceov_1a9eb5ed541b9130617bfee541a9679464>`(:ref:`model <doxid-group__ov__runtime__cpp__prop__api_1ga461856fdfb6d7533dc53355aec9e9fad>`, xml, bin);

.. raw:: html

   </div>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="Python">





.. ref-code-block:: cpp

	# ========  Step 0: read original model =========
	core = Core()
	model = core.read_model(model='/path/to/some_model.onnx')
	
	# ======== Step 1: Preprocessing ================
	ppp = PrePostProcessor(model)
	# Declare section of desired application's input format
	ppp.input().tensor() \
	    .set_element_type(Type.u8) \
	    .set_spatial_dynamic_shape() \
	    .:ref:`set_layout <doxid-group__ov__layout__cpp__api_1ga18464fb8ed029acb5fdc2bb1737358d9>`(:ref:`Layout <doxid-namespace_inference_engine_1a246d143abc5ca07da8d2cadeeb88fdb8>`('NHWC')) \
	    .set_color_format(ColorFormat.BGR)
	
	# Specify actual model layout
	ppp.input().:ref:`model <doxid-group__ov__runtime__cpp__prop__api_1ga461856fdfb6d7533dc53355aec9e9fad>`().:ref:`set_layout <doxid-group__ov__layout__cpp__api_1ga18464fb8ed029acb5fdc2bb1737358d9>`(:ref:`Layout <doxid-namespace_inference_engine_1a246d143abc5ca07da8d2cadeeb88fdb8>`('NCHW'))
	
	# Explicit preprocessing steps. Layout conversion will be done automatically as last step
	ppp.input().preprocess() \
	    .convert_element_type() \
	    .convert_color(ColorFormat.RGB) \
	    .resize(ResizeAlgorithm.RESIZE_LINEAR) \
	    .:ref:`mean <doxid-namespacengraph_1_1builder_1_1opset1_1a06c7367d66f6e48931cbdf49c696d8c9>`([123.675, 116.28, 103.53]) \
	    .scale([58.624, 57.12, 57.375])
	
	# Dump preprocessor
	print(f'Dump preprocessor: {ppp}')
	model = ppp.build()
	
	# ======== Step 2: Change batch size ================
	# In this example we also want to change batch size to increase throughput
	:ref:`set_batch <doxid-namespaceov_1a3314e2ff91fcc9ffec05b1a77c37862b>`(model, 2)
	
	# ======== Step 3: Save the model ================
	:ref:`serialize <doxid-namespaceov_1a9eb5ed541b9130617bfee541a9679464>`(model, '/path/to/some_model_saved.xml', '/path/to/some_model_saved.bin')

.. raw:: html

   </div>







.. raw:: html

   </div>

Application Code - Load Model to Target Device
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

After this, the application code can load a saved file and stop preprocessing. In this case, enable :ref:`model caching <doxid-openvino_docs__o_v__u_g__model_caching_overview>` to minimize load time when the cached model is available.

.. raw:: html

   <div class='sphinxtabset'>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="C++">





.. ref-code-block:: cpp

	:ref:`ov::Core <doxid-classov_1_1_core>` core;
	core.:ref:`set_property <doxid-classov_1_1_core_1aa953cb0a1601dbc9a34ef6ba82b8476e>`(:ref:`ov::cache_dir <doxid-group__ov__runtime__cpp__prop__api_1ga3276fc4ed7cc7d0bbdcf0ae12063728d>`("/path/to/cache/dir"));

	// In case that no preprocessing is needed anymore, we can load model on target device directly
	// With cached model available, it will also save some time on reading original model
	:ref:`ov::CompiledModel <doxid-classov_1_1_compiled_model>` compiled_model = core.:ref:`compile_model <doxid-classov_1_1_core_1a46555f0803e8c29524626be08e7f5c5a>`("/path/to/some_model_saved.xml", "CPU");

.. raw:: html

   </div>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="Python">





.. ref-code-block:: cpp

	core = Core()
	core.set_property({'CACHE_DIR': '/path/to/cache/dir'})
	
	# In case that no preprocessing is needed anymore, we can load model on target device directly
	# With cached model available, it will also save some time on reading original model
	compiled_model = core.compile_model('/path/to/some_model_saved.xml', 'CPU')

.. raw:: html

   </div>







.. raw:: html

   </div>

Additional Resources
~~~~~~~~~~~~~~~~~~~~

* :ref:`Preprocessing Details <doxid-openvino_docs__o_v__u_g__preprocessing__details>`

* :ref:`Layout API overview <doxid-openvino_docs__o_v__u_g__layout__overview>`

* :ref:`Model Optimizer - Optimize Preprocessing Computation <doxid-openvino_docs__m_o__d_g__additional__optimization__use__cases>`

* :ref:`Model Caching Overview <doxid-openvino_docs__o_v__u_g__model_caching_overview>`

* The ``:ref:`ov::preprocess::PrePostProcessor <doxid-classov_1_1preprocess_1_1_pre_post_processor>``` C++ class documentation

* The ``:ref:`ov::pass::Serialize <doxid-classov_1_1pass_1_1_serialize>``` - pass to serialize model to XML/BIN

* The ``:ref:`ov::set_batch <doxid-namespaceov_1a3314e2ff91fcc9ffec05b1a77c37862b>``` - update batch dimension for a given model

