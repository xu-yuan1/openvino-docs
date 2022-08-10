.. index:: pair: page; Preprocessing API - details
.. _doxid-openvino_docs__o_v__u_g__preprocessing__details:


Preprocessing API - details
===========================

:target:`doxid-openvino_docs__o_v__u_g__preprocessing__details_1md_openvino_docs_ov_runtime_ug_preprocessing_details` The purpose of this article is to present details on preprocessing API, such as its capabilities and post-processing.

Pre-processing Capabilities
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Below is a full list of pre-processing API capabilities:

Addressing Particular Input/Output
----------------------------------

If the model has only one input, then simple ``:ref:`ov::preprocess::PrePostProcessor::input() <doxid-classov_1_1preprocess_1_1_pre_post_processor_1a611b930e59cd16176f380d21e755cda1>``` will get a reference to pre-processing builder for this input (a tensor, the steps, a model):

.. raw:: html

   <div class='sphinxtabset'>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="C++">





.. ref-code-block:: cpp

	ppp.input() // no index/name is needed if model has one input
	  .preprocess().scale(50.f);
	
	ppp.output()   // same for output
	  .postprocess().convert_element_type(:ref:`ov::element::u8 <doxid-group__ov__element__cpp__api_1gaaf60c536d3e295285f6a899eb3d29e2f>`);

.. raw:: html

   </div>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="Python">





.. ref-code-block:: cpp

	# no index/name is needed if model has one input
	ppp.input().preprocess().scale(50.)
	
	# same for output
	ppp.output() \
	    .postprocess().convert_element_type(Type.u8)

.. raw:: html

   </div>







.. raw:: html

   </div>

In general, when a model has multiple inputs/outputs, each one can be addressed by a tensor name.

.. raw:: html

   <div class='sphinxtabset'>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="C++">





.. ref-code-block:: cpp

	auto &input_image = ppp.input("image");
	auto &output_result = ppp.output("result");

.. raw:: html

   </div>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="Python">





.. ref-code-block:: cpp

	ppp.input('image')
	ppp.output('result')

.. raw:: html

   </div>







.. raw:: html

   </div>

Or by it's index.

.. raw:: html

   <div class='sphinxtabset'>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="C++">





.. ref-code-block:: cpp

	auto &input_1 = ppp.input(1); // Gets 2nd input in a model
	auto &output_1 = ppp.output(2); // Get output with index=2 (3rd one) in a model

.. raw:: html

   </div>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="Python">





.. ref-code-block:: cpp

	ppp.input(1) # Gets 2nd input in a model
	ppp.output(2) # Gets output with index=2 (3rd one) in a model

.. raw:: html

   </div>







.. raw:: html

   </div>



C++ references:

* ``:ref:`ov::preprocess::InputTensorInfo <doxid-classov_1_1preprocess_1_1_input_tensor_info>```

* ``:ref:`ov::preprocess::OutputTensorInfo <doxid-classov_1_1preprocess_1_1_output_tensor_info>```

* ``:ref:`ov::preprocess::PrePostProcessor <doxid-classov_1_1preprocess_1_1_pre_post_processor>```

Supported Pre-processing Operations
-----------------------------------

C++ references:

* ``:ref:`ov::preprocess::PreProcessSteps <doxid-classov_1_1preprocess_1_1_pre_process_steps>```

Mean/Scale Normalization
++++++++++++++++++++++++

Typical data normalization includes 2 operations for each data item: subtract mean value and divide to standard deviation. This can be done with the following code:

.. raw:: html

   <div class='sphinxtabset'>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="C++">





.. ref-code-block:: cpp

	ppp.input("input").preprocess().mean(128).scale(127);

.. raw:: html

   </div>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="Python">





.. ref-code-block:: cpp

	ppp.input('input').preprocess().:ref:`mean <doxid-namespacengraph_1_1builder_1_1opset1_1a06c7367d66f6e48931cbdf49c696d8c9>`(128).scale(127)

.. raw:: html

   </div>







.. raw:: html

   </div>



In Computer Vision area normalization is usually done separately for R, G, B values. To do this, :ref:`layout with 'C' dimension <doxid-openvino_docs__o_v__u_g__layout__overview>` shall be defined. Example:

.. raw:: html

   <div class='sphinxtabset'>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="C++">





.. ref-code-block:: cpp

	// Suppose model's shape is {1, 3, 224, 224}
	ppp.input("input").model().set_layout("NCHW"); // N=1, C=3, H=224, W=224
	// Mean/Scale has 3 values which matches with C=3
	ppp.input("input").preprocess()
	  .mean({103.94, 116.78, 123.68}).scale({57.21, 57.45, 57.73});

.. raw:: html

   </div>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="Python">





.. ref-code-block:: cpp

	# Suppose model's shape is {1, 3, 224, 224}
	# N=1, C=3, H=224, W=224
	ppp.input('input').:ref:`model <doxid-group__ov__runtime__cpp__prop__api_1ga461856fdfb6d7533dc53355aec9e9fad>`().:ref:`set_layout <doxid-group__ov__layout__cpp__api_1ga18464fb8ed029acb5fdc2bb1737358d9>`(:ref:`Layout <doxid-namespace_inference_engine_1a246d143abc5ca07da8d2cadeeb88fdb8>`('NCHW'))
	# Mean/Scale has 3 values which matches with C=3
	ppp.input('input').preprocess() \
	    .:ref:`mean <doxid-namespacengraph_1_1builder_1_1opset1_1a06c7367d66f6e48931cbdf49c696d8c9>`([103.94, 116.78, 123.68]).scale([57.21, 57.45, 57.73])

.. raw:: html

   </div>







.. raw:: html

   </div>



C++ references:

* ``:ref:`ov::preprocess::PreProcessSteps::mean() <doxid-classov_1_1preprocess_1_1_pre_process_steps_1aef1bb8c1fc5eb0014b07b78749c432dc>```

* ``:ref:`ov::preprocess::PreProcessSteps::scale() <doxid-classov_1_1preprocess_1_1_pre_process_steps_1aeacaf406d72a238e31a359798ebdb3b7>```

Converting Precision
++++++++++++++++++++

In Computer Vision, the image is represented by an array of unsigned 8-bit integer values (for each color), but the model accepts floating point tensors.

To integrate precision conversion into an execution graph as a pre-processing step:

.. raw:: html

   <div class='sphinxtabset'>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="C++">





.. ref-code-block:: cpp

	// First define data type for your tensor
	ppp.input("input").tensor().set_element_type(:ref:`ov::element::u8 <doxid-group__ov__element__cpp__api_1gaaf60c536d3e295285f6a899eb3d29e2f>`);
	
	// Then define preprocessing step
	ppp.input("input").preprocess().convert_element_type(:ref:`ov::element::f32 <doxid-group__ov__element__cpp__api_1gadc8a5dda3244028a5c0b024897215d43>`);
	
	// If conversion is needed to `model's` element type, 'f32' can be omitted
	ppp.input("input").preprocess().convert_element_type();

.. raw:: html

   </div>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="Python">





.. ref-code-block:: cpp

	# First define data type for your tensor
	ppp.input('input').tensor().set_element_type(Type.u8)
	
	# Then define preprocessing step
	ppp.input('input').preprocess().convert_element_type(Type.f32)
	
	# If conversion is needed to `model's` element type, 'f32' can be omitted
	ppp.input('input').preprocess().convert_element_type()

.. raw:: html

   </div>







.. raw:: html

   </div>



C++ references:

* ``:ref:`ov::preprocess::InputTensorInfo::set_element_type() <doxid-classov_1_1preprocess_1_1_input_tensor_info_1a98fb73ff9178c8c71d809ddf8927faf5>```

* ``:ref:`ov::preprocess::PreProcessSteps::convert_element_type() <doxid-classov_1_1preprocess_1_1_pre_process_steps_1aac6316155a1690609eb320637c193d50>```

Converting layout (transposing)
+++++++++++++++++++++++++++++++

Transposing of matrices/tensors is a typical operation in Deep Learning - you may have a BMP image 640x480, which is an array of ``{480, 640, 3}`` elements, but Deep Learning model can require input with shape ``{1, 3, 480, 640}``.

Conversion can be done implicitly, using the :ref:`layout <doxid-openvino_docs__o_v__u_g__layout__overview>` of a user's tensor and the layout of an original model.

.. raw:: html

   <div class='sphinxtabset'>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="C++">





.. ref-code-block:: cpp

	// First define layout for your tensor
	ppp.input("input").tensor().set_layout("NHWC");
	
	// Then define layout of model
	ppp.input("input").model().set_layout("NCHW");
	
	std::cout << ppp; // Will print 'implicit layout conversion step'

.. raw:: html

   </div>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="Python">





.. ref-code-block:: cpp

	# First define layout for your tensor
	ppp.input('input').tensor().:ref:`set_layout <doxid-group__ov__layout__cpp__api_1ga18464fb8ed029acb5fdc2bb1737358d9>`(:ref:`Layout <doxid-namespace_inference_engine_1a246d143abc5ca07da8d2cadeeb88fdb8>`('NHWC'))
	
	# Then define layout of model
	ppp.input('input').:ref:`model <doxid-group__ov__runtime__cpp__prop__api_1ga461856fdfb6d7533dc53355aec9e9fad>`().:ref:`set_layout <doxid-group__ov__layout__cpp__api_1ga18464fb8ed029acb5fdc2bb1737358d9>`(:ref:`Layout <doxid-namespace_inference_engine_1a246d143abc5ca07da8d2cadeeb88fdb8>`('NCHW'))
	
	print(ppp)  # Will print 'implicit layout conversion step'

.. raw:: html

   </div>







.. raw:: html

   </div>

For a manual transpose of axes without the use of a :ref:`layout <doxid-openvino_docs__o_v__u_g__layout__overview>` in the code:

.. raw:: html

   <div class='sphinxtabset'>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="C++">





.. ref-code-block:: cpp

	ppp.input("input").tensor().set_shape({1, 480, 640, 3});
	// Model expects shape {1, 3, 480, 640}
	ppp.input("input").preprocess().convert_layout({0, 3, 1, 2});
	// 0 -> 0; 3 -> 1; 1 -> 2; 2 -> 3

.. raw:: html

   </div>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="Python">





.. ref-code-block:: cpp

	ppp.input('input').tensor().set_shape([1, 480, 640, 3])
	
	# Model expects shape {1, 3, 480, 640}
	ppp.input('input').preprocess()\
	    .convert_layout([0, 3, 1, 2])
	# 0 -> 0; 3 -> 1; 1 -> 2; 2 -> 3

.. raw:: html

   </div>







.. raw:: html

   </div>



It performs the same transpose. However, the approach where source and destination layout are used can be easier to read and understand.

C++ references:

* ``:ref:`ov::preprocess::PreProcessSteps::convert_layout() <doxid-classov_1_1preprocess_1_1_pre_process_steps_1a0f65fdadca32e90f5ef3a323b640b978>```

* ``:ref:`ov::preprocess::InputTensorInfo::set_layout() <doxid-classov_1_1preprocess_1_1_input_tensor_info_1a6f70eb97d02e90a30cd748573abd7b4b>```

* ``:ref:`ov::preprocess::InputModelInfo::set_layout() <doxid-classov_1_1preprocess_1_1_input_model_info_1af309bac02af20d048e349a2d421c1169>```

* ``:ref:`ov::Layout <doxid-classov_1_1_layout>```

Resizing Image
++++++++++++++

Resizing an image is a typical pre-processing step for computer vision tasks. With pre-processing API, this step can also be integrated into an execution graph and performed on a target device.

To resize the input image, it is needed to define ``H`` and ``W`` dimensions of the :ref:`layout <doxid-openvino_docs__o_v__u_g__layout__overview>`

.. raw:: html

   <div class='sphinxtabset'>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="C++">





.. ref-code-block:: cpp

	ppp.input("input").tensor().set_shape({1, 3, 960, 1280});
	ppp.input("input").model().set_layout("??HW");
	ppp.input("input").preprocess().resize(:ref:`ov::preprocess::ResizeAlgorithm::RESIZE_LINEAR <doxid-namespaceov_1_1preprocess_1a8665e295e222dc2120be3550e04db8f3a8803101bcf6d2ec700e6e7358217db68>`, 480, 640);

.. raw:: html

   </div>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="Python">





.. ref-code-block:: cpp

	ppp.input('input').tensor().set_shape([1, 3, 960, 1280])
	ppp.input('input').:ref:`model <doxid-group__ov__runtime__cpp__prop__api_1ga461856fdfb6d7533dc53355aec9e9fad>`().:ref:`set_layout <doxid-group__ov__layout__cpp__api_1ga18464fb8ed029acb5fdc2bb1737358d9>`(:ref:`Layout <doxid-namespace_inference_engine_1a246d143abc5ca07da8d2cadeeb88fdb8>`('??HW'))
	ppp.input('input').preprocess()\
	    .resize(ResizeAlgorithm.RESIZE_LINEAR, 480, 640)

.. raw:: html

   </div>







.. raw:: html

   </div>



When original model has known spatial dimensions (``width`` + ``height``), target ``width`` / ``height`` can be omitted.

.. raw:: html

   <div class='sphinxtabset'>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="C++">





.. ref-code-block:: cpp

	ppp.input("input").tensor().set_shape({1, 3, 960, 1280});
	ppp.input("input").model().set_layout("??HW"); // Model accepts {1, 3, 480, 640} shape
	// Resize to model's dimension
	ppp.input("input").preprocess().resize(:ref:`ov::preprocess::ResizeAlgorithm::RESIZE_LINEAR <doxid-namespaceov_1_1preprocess_1a8665e295e222dc2120be3550e04db8f3a8803101bcf6d2ec700e6e7358217db68>`);

.. raw:: html

   </div>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="Python">





.. ref-code-block:: cpp

	ppp.input('input').tensor().set_shape([1, 3, 960, 1280])
	# Model accepts {1, 3, 480, 640} shape, thus last dimensions are 'H' and 'W'
	ppp.input('input').:ref:`model <doxid-group__ov__runtime__cpp__prop__api_1ga461856fdfb6d7533dc53355aec9e9fad>`().:ref:`set_layout <doxid-group__ov__layout__cpp__api_1ga18464fb8ed029acb5fdc2bb1737358d9>`(:ref:`Layout <doxid-namespace_inference_engine_1a246d143abc5ca07da8d2cadeeb88fdb8>`('??HW'))
	# Resize to model's dimension
	ppp.input('input').preprocess().resize(ResizeAlgorithm.RESIZE_LINEAR)

.. raw:: html

   </div>







.. raw:: html

   </div>



C++ references:

* ``:ref:`ov::preprocess::PreProcessSteps::resize() <doxid-classov_1_1preprocess_1_1_pre_process_steps_1a40dab78be1222fee505ed6a13400efe6>```

* ``:ref:`ov::preprocess::ResizeAlgorithm <doxid-namespaceov_1_1preprocess_1a8665e295e222dc2120be3550e04db8f3>```

Color Conversion
++++++++++++++++

Typical use case is to reverse color channels from ``RGB`` to ``BGR`` and vice versa. To do this, specify source color format in ``tensor`` section and perform ``convert_color`` pre-processing operation. In the example below, a ``BGR`` image needs to be converted to ``RGB`` as required for the model input.

.. raw:: html

   <div class='sphinxtabset'>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="C++">





.. ref-code-block:: cpp

	ppp.input("input").tensor().set_color_format(:ref:`ov::preprocess::ColorFormat::BGR <doxid-namespaceov_1_1preprocess_1ab027f26e58038e454e1b50a5243f1707a2ad5640ebdec72fc79531d1778c6c2dc>`);
	ppp.input("input").preprocess().convert_color(:ref:`ov::preprocess::ColorFormat::RGB <doxid-namespaceov_1_1preprocess_1ab027f26e58038e454e1b50a5243f1707a889574aebacda6bfd3e534e2b49b8028>`);

.. raw:: html

   </div>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="Python">





.. ref-code-block:: cpp

	ppp.input('input').tensor().set_color_format(ColorFormat.BGR)
	
	ppp.input('input').preprocess().convert_color(ColorFormat.RGB)

.. raw:: html

   </div>







.. raw:: html

   </div>





Color Conversion - NV12/I420
++++++++++++++++++++++++++++

Pre-processing also supports YUV-family source color formats, i.e. NV12 and I420. In advanced cases, such YUV images can be split into separate planes, e.g., for NV12 images Y-component may come from one source and UV-component from another one. Concatenating such components in user's application manually is not a perfect solution from performance and device utilization perspectives. However, there is a way to use Pre-processing API. For such cases there are ``NV12_TWO_PLANES`` and ``I420_THREE_PLANES`` source color formats, which will split the original ``input`` into 2 or 3 inputs.

.. raw:: html

   <div class='sphinxtabset'>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="C++">





.. ref-code-block:: cpp

	// This will split original `input` to 2 separate inputs: `input/y' and 'input/uv'
	ppp.input("input").tensor().set_color_format(:ref:`ov::preprocess::ColorFormat::NV12_TWO_PLANES <doxid-namespaceov_1_1preprocess_1ab027f26e58038e454e1b50a5243f1707a54f60c652650de96e9d118187b3ba25f>`);
	ppp.input("input").preprocess().convert_color(:ref:`ov::preprocess::ColorFormat::RGB <doxid-namespaceov_1_1preprocess_1ab027f26e58038e454e1b50a5243f1707a889574aebacda6bfd3e534e2b49b8028>`);
	std::cout << ppp;  // Dump preprocessing steps to see what will happen

.. raw:: html

   </div>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="Python">





.. ref-code-block:: cpp

	# This will split original `input` to 2 separate inputs: `input/y' and 'input/uv'
	ppp.input('input').tensor()\
	    .set_color_format(ColorFormat.NV12_TWO_PLANES)
	
	ppp.input('input').preprocess()\
	    .convert_color(ColorFormat.RGB)
	print(ppp)  # Dump preprocessing steps to see what will happen

.. raw:: html

   </div>







.. raw:: html

   </div>



In this example, the original ``input`` is split to ``input/y`` and ``input/uv`` inputs. You can fill ``input/y`` from one source, and ``input/uv`` from another source. Color conversion to ``RGB`` will be performed, using these sources. It is more efficient as there will be no additional copies of NV12 buffers.

C++ references:

* ``:ref:`ov::preprocess::ColorFormat <doxid-namespaceov_1_1preprocess_1ab027f26e58038e454e1b50a5243f1707>```

* ``:ref:`ov::preprocess::PreProcessSteps::convert_color <doxid-classov_1_1preprocess_1_1_pre_process_steps_1a4f062246cc0082822346c97917903983>```

Custom Operations
-----------------

Pre-processing API also allows adding ``custom`` preprocessing steps into an execution graph. The ``custom`` function accepts the current ``input`` node, applies the defined preprocessing operations, and returns a new node.

**Note:** Custom pre-processing function should only insert node(s) after the input. It is done during model compilation. This function will NOT be called during the execution phase. This may appear to be complicated and require knowledge of :ref:`OpenVINO™ operations <doxid-openvino_docs_ops_opset>`.

If there is a need to insert additional operations to the execution graph right after the input, like some specific crops and/or resizes - Pre-processing API can be a good choice to implement this.

.. raw:: html

   <div class='sphinxtabset'>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="C++">





.. ref-code-block:: cpp

	ppp.input("input_image").preprocess()
	   .custom([](const :ref:`ov::Output\<ov::Node> <doxid-classov_1_1_output>`& node) {
	       // Custom nodes can be inserted as Pre-processing steps
	       return std::make_shared<ov::opset8::Abs>(node);
	   });

.. raw:: html

   </div>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="Python">





.. ref-code-block:: cpp

	# It is possible to insert some custom operations
	import openvino.runtime.opset8 as ops
	from openvino.runtime import Output
	from openvino.runtime.utils.decorators import custom_preprocess_function
	
	@custom_preprocess_function
	def custom_abs(output: Output):
	    # Custom nodes can be inserted as Preprocessing steps
	    return ops.abs(output)
	
	ppp.input("input_image").preprocess() \
	    .custom(custom_abs)

.. raw:: html

   </div>







.. raw:: html

   </div>



C++ references:

* ``:ref:`ov::preprocess::PreProcessSteps::custom() <doxid-classov_1_1preprocess_1_1_pre_process_steps_1aa88ce522ef69253e4d978f10c3b566f1>```

* :ref:`Available Operations Sets <doxid-openvino_docs_ops_opset>`

Post-processing
~~~~~~~~~~~~~~~

Post-processing steps can be added to model outputs. As for pre-processing, these steps will be also integrated into a graph and executed on a selected device.

Pre-processing uses the following flow: **User tensor** -> **Steps** -> **Model input**.

Post-processing uses the reverse: **Model output** -> **Steps** -> **User tensor**.

Compared to pre-processing, there are not as many operations needed for the post-processing stage. Currently, only the following post-processing operations are supported:

* Convert a :ref:`layout <doxid-openvino_docs__o_v__u_g__layout__overview>`.

* Convert an element type.

* Customize operations.

Usage of these operations is similar to pre-processing. See the following example:

.. raw:: html

   <div class='sphinxtabset'>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="C++">





.. ref-code-block:: cpp

	// Model's output has 'NCHW' layout
	ppp.output("result_image").model().set_layout("NCHW");

	// Set target user's tensor to U8 type + 'NHWC' layout
	// Precision & layout conversions will be done implicitly
	ppp.output("result_image").tensor()
	   .set_layout("NHWC")
	   .set_element_type(:ref:`ov::element::u8 <doxid-group__ov__element__cpp__api_1gaaf60c536d3e295285f6a899eb3d29e2f>`);

	// Also it is possible to insert some custom operations
	ppp.output("result_image").postprocess()
	   .custom([](const :ref:`ov::Output\<ov::Node> <doxid-classov_1_1_output>`& node) {
	       // Custom nodes can be inserted as Post-processing steps
	       return std::make_shared<ov::opset8::Abs>(node);
	   });

.. raw:: html

   </div>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="Python">





.. ref-code-block:: cpp

	# Model's output has 'NCHW' layout
	ppp.output('result_image').:ref:`model <doxid-group__ov__runtime__cpp__prop__api_1ga461856fdfb6d7533dc53355aec9e9fad>`().:ref:`set_layout <doxid-group__ov__layout__cpp__api_1ga18464fb8ed029acb5fdc2bb1737358d9>`(:ref:`Layout <doxid-namespace_inference_engine_1a246d143abc5ca07da8d2cadeeb88fdb8>`('NCHW'))
	
	# Set target user's tensor to U8 type + 'NHWC' layout
	# Precision & layout conversions will be done implicitly
	ppp.output('result_image').tensor()\
	    .:ref:`set_layout <doxid-group__ov__layout__cpp__api_1ga18464fb8ed029acb5fdc2bb1737358d9>`(:ref:`Layout <doxid-namespace_inference_engine_1a246d143abc5ca07da8d2cadeeb88fdb8>`("NHWC"))\
	    .set_element_type(Type.u8)
	
	# Also it is possible to insert some custom operations
	import openvino.runtime.opset8 as ops
	from openvino.runtime import Output
	from openvino.runtime.utils.decorators import custom_preprocess_function
	
	@custom_preprocess_function
	def custom_abs(output: Output):
	    # Custom nodes can be inserted as Post-processing steps
	    return ops.abs(output)
	
	ppp.output("result_image").postprocess()\
	    .custom(custom_abs)

.. raw:: html

   </div>







.. raw:: html

   </div>



C++ references:

* ``:ref:`ov::preprocess::PostProcessSteps <doxid-classov_1_1preprocess_1_1_post_process_steps>```

* ``:ref:`ov::preprocess::OutputModelInfo <doxid-classov_1_1preprocess_1_1_output_model_info>```

* ``:ref:`ov::preprocess::OutputTensorInfo <doxid-classov_1_1preprocess_1_1_output_tensor_info>```

