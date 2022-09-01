.. index:: pair: page; Dynamic Shapes
.. _deploy_infer__dynamic_shapes:

.. meta::
   :description: The Reshape method in OpenVINO Runtime API can handle dynamic 
                 shapes of models that support changing input shapes before 
                 model compilation.
   :keywords: OpenVINO, OpenVINO Runtime API, inference, model inference, model 
              shape, input shape, dynamic shape, dynamic dimensions, sequence 
              length, ov::Dimension, ov.Dimension, lower bounds, upper bounds, 
              reshape model, reshape method, compile_model method, spatial dimensions, 
              batch dimension, undefined dimensions, OpenVINO IR, model optimizer, 
              get_input_tensor, set_input_tensor, set_shape, tensor, partial shape, 
              partial_shape, get_partial_shape

Dynamic Shapes
==============

:target:`deploy_infer__dynamic_shapes_1md_openvino_docs_ov_runtime_ug_ov_dynamic_shapes`

.. toctree::
   :maxdepth: 1
   :hidden:

   ./dynamic-shapes/dynamic-shapes-not-applicable

As it was demonstrated in the :ref:`Changing Input Shapes <deploy_infer__shape_inference>` article, there are models that support changing input shapes before model compilation in ``Core::compile_model``. Reshaping models provides an ability to customize the model input shape for the exact size required in the end application. This article explains how the ability of model to reshape can further be leveraged in more dynamic scenarios.

Applying Dynamic Shapes
~~~~~~~~~~~~~~~~~~~~~~~

Conventional "static" model reshaping works well when it can be done once per many model inference calls with the same shape. However, this approach does not perform efficiently if the input tensor shape is changed on every inference call. Calling the ``:ref:`reshape() <doxid-namespacengraph_1_1builder_1_1opset1_1ad5b09acfb63fe54b85b33d6e22ccdc72>``` and ``compile_model()`` methods each time a new size comes is extremely time-consuming. A popular example would be inference of natural language processing models (like BERT) with arbitrarily-sized user input sequences. In this case, the sequence length cannot be predicted and may change every time inference is called. Dimensions that can be frequently changed are called *dynamic dimensions*. Dynamic shapes should be considered, when a real shape of input is not known at the time of the ``compile_model()`` method call.

Below are several examples of dimensions that can be naturally dynamic:

* Sequence length dimension for various sequence processing models, like BERT

* Spatial dimensions in segmentation and style transfer models

* Batch dimension

* Arbitrary number of detections in object detection models output

There are various methods to address input dynamic dimensions through combining multiple pre-reshaped models and input data padding. The methods are sensitive to model internals, do not always give optimal performance and are cumbersome. For a short overview of the methods, refer to the :ref:`When Dynamic Shapes API is Not Applicable <deploy_infer__no_dynamic_shapes>` page. Apply those methods only if native dynamic shape API described in the following sections does not work or does not perform as expected.

The decision about using dynamic shapes should be based on proper benchmarking of a real application with real data. Unlike statically shaped models, dynamically shaped ones require different inference time, depending on input data shape or input tensor content. Furthermore, using the dynamic shapes can bring more overheads in memory and running time of each inference call depending on hardware plugin and model used.

Handling Dynamic Shapes Natively
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This section describes how to handle dynamically shaped models natively with OpenVINO Runtime API version 2022.1 and higher. There are three main parts in the flow that differ from static shapes:

* Configure the model.

* Prepare data for inference.

* Read resulting data after inference.

Configuring the Model
---------------------

To avoid the methods mentioned in the previous section, there is a way to specify one or multiple dimensions to be dynamic, directly in the model inputs. This is achieved with the same reshape method that is used for alternating static shape of inputs. Dynamic dimensions are specified as ``-1`` or the ``:ref:`ov::Dimension() <doxid-classov_1_1_dimension>``` instead of a positive number used for static dimensions:

.. raw:: html

   <div class='sphinxtabset'>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="C++">





.. ref-code-block:: cpp

	:ref:`ov::Core <doxid-classov_1_1_core>` core;
	auto :ref:`model <doxid-group__ov__runtime__cpp__prop__api_1ga461856fdfb6d7533dc53355aec9e9fad>` = core.:ref:`read_model <doxid-classov_1_1_core_1ae0576a95f841c3a6f5e46e4802716981>`("model.xml");
	
	// Set one static dimension (= 1) and another dynamic dimension (= Dimension())
	:ref:`model <doxid-group__ov__runtime__cpp__prop__api_1ga461856fdfb6d7533dc53355aec9e9fad>`->reshape({{1, :ref:`ov::Dimension <doxid-classov_1_1_dimension>`()}});  // {1,?}
	
	// The same as above
	:ref:`model <doxid-group__ov__runtime__cpp__prop__api_1ga461856fdfb6d7533dc53355aec9e9fad>`->reshape({{1, -1}}); // {1,?}
	
	// Or set both dimensions as dynamic if both are going to be changed dynamically
	:ref:`model <doxid-group__ov__runtime__cpp__prop__api_1ga461856fdfb6d7533dc53355aec9e9fad>`->reshape({{:ref:`ov::Dimension <doxid-classov_1_1_dimension>`(), :ref:`ov::Dimension <doxid-classov_1_1_dimension>`()}});  // {?,?}
	
	// The same as above
	:ref:`model <doxid-group__ov__runtime__cpp__prop__api_1ga461856fdfb6d7533dc53355aec9e9fad>`->reshape({{-1, -1}});  // {?,?}

.. raw:: html

   </div>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="Python">





.. ref-code-block:: cpp

	core = :ref:`ov.Core <doxid-classov_1_1_core>`()
	model = core.read_model("model.xml")
	
	# Set one static dimension (= 1) and another dynamic dimension (= Dimension())
	model.reshape([1, :ref:`ov.Dimension <doxid-classov_1_1_dimension>`()])
	
	# The same as above
	model.reshape([1, -1])
	
	# The same as above
	model.reshape("1, ?")
	
	# Or set both dimensions as dynamic if both are going to be changed dynamically
	model.reshape([:ref:`ov.Dimension <doxid-classov_1_1_dimension>`(), :ref:`ov.Dimension <doxid-classov_1_1_dimension>`()])
	
	# The same as above
	model.reshape([-1, -1])
	
	# The same as above
	model.reshape("?, ?")





.. raw:: html

   </div>







.. raw:: html

   </div>



To simplify the code, the examples assume that the model has a single input and single output. However, there are no limitations on the number of inputs and outputs to apply dynamic shapes.

Undefined Dimensions "Out Of the Box"
-------------------------------------

Dynamic dimensions may appear in the input model without calling the ``reshape`` method. Many DL frameworks support undefined dimensions. If such a model is converted with Model Optimizer or read directly by the ``Core::read_model``, undefined dimensions are preserved. Such dimensions are automatically treated as dynamic ones. Therefore, there is no need to call the ``reshape`` method, if undefined dimensions are already configured in the original or the IR model.

If the input model has undefined dimensions that will not change during inference. It is recommended to set them to static values, using the same ``reshape`` method of the model. From the API perspective, any combination of dynamic and static dimensions can be configured.

Model Optimizer provides identical capability to reshape the model during the conversion, including specifying dynamic dimensions. Use this capability to save time on calling ``reshape`` method in the end application. To get information about setting input shapes using Model Optimizer, refer to :ref:`Setting Input Shapes <doxid-openvino_docs__m_o__d_g_prepare_model_convert_model__converting__model>`.

Dimension Bounds
----------------

Apart from a dynamic dimension, the lower and/or upper bounds can also be specified. They define a range of allowed values for the dimension. The bounds are coded as arguments for the ``:ref:`ov::Dimension <doxid-classov_1_1_dimension>``` :

.. raw:: html

   <div class='sphinxtabset'>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="C++">





.. ref-code-block:: cpp

	// Both dimensions are dynamic, first has a size within 1..10 and the second has a size within 8..512
	:ref:`model <doxid-group__ov__runtime__cpp__prop__api_1ga461856fdfb6d7533dc53355aec9e9fad>`->reshape({{:ref:`ov::Dimension <doxid-classov_1_1_dimension>`(1, 10), :ref:`ov::Dimension <doxid-classov_1_1_dimension>`(8, 512)}});  // {1..10,8..512}
	
	// Both dimensions are dynamic, first doesn't have bounds, the second is in the range of 8..512
	:ref:`model <doxid-group__ov__runtime__cpp__prop__api_1ga461856fdfb6d7533dc53355aec9e9fad>`->reshape({{-1, :ref:`ov::Dimension <doxid-classov_1_1_dimension>`(8, 512)}});   // {?,8..512}

.. raw:: html

   </div>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="Python">





.. ref-code-block:: cpp

	# Both dimensions are dynamic, first has a size within 1..10 and the second has a size within 8..512
	model.reshape([:ref:`ov.Dimension <doxid-classov_1_1_dimension>`(1, 10), :ref:`ov.Dimension <doxid-classov_1_1_dimension>`(8, 512)])
	
	# The same as above
	model.reshape([(1, 10), (8, 512)])
	
	# The same as above
	model.reshape("1..10, 8..512")
	
	# Both dimensions are dynamic, first doesn't have bounds, the second is in the range of 8..512
	model.reshape([-1, (8, 512)])





.. raw:: html

   </div>







.. raw:: html

   </div>



Information about bounds gives an opportunity for the inference plugin to apply additional optimizations. Using dynamic shapes assumes the plugins apply more flexible optimization approach during model compilation. It may require more time/memory for model compilation and inference. Therefore, providing any additional information, like bounds, can be beneficial. For the same reason, it is not recommended to leave dimensions as undefined, without the real need.

When specifying bounds, the lower bound is not as important as the upper one. The upper bound allows inference devices to allocate memory for intermediate tensors more precisely. It also allows using a fewer number of tuned kernels for different sizes. More precisely, benefits of specifying the lower or upper bound is device dependent. Depending on the plugin, specifying the upper bounds can be required. For information about dynamic shapes support on different devices, refer to the :ref:`Features Support Matrix <deploy_infer__working_with_devices_1features_support_matrix>`.

If the lower and upper bounds for a dimension are known, it is recommended to specify them, even if a plugin can execute a model without the bounds.

Setting Input Tensors
---------------------

Preparing a model with the ``reshape`` method is the first step. The second step is passing a tensor with an appropriate shape to infer request. This is similar to the :ref:`regular steps <deploy_infer__integrate_application>`. However, tensors can now be passed with different shapes for the same executable model and even for the same inference request:

.. raw:: html

   <div class='sphinxtabset'>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="C++">





.. ref-code-block:: cpp

	// The first inference call
	
	// Create tensor compatible with the model input
	// Shape {1, 128} is compatible with any reshape statements made in previous examples
	auto input_tensor_1 = :ref:`ov::Tensor <doxid-classov_1_1_tensor>`(:ref:`model <doxid-group__ov__runtime__cpp__prop__api_1ga461856fdfb6d7533dc53355aec9e9fad>`->input().get_element_type(), {1, 128});
	// ... write values to input_tensor_1
	
	// Set the tensor as an input for the infer request
	infer_request.set_input_tensor(input_tensor_1);
	
	// Do the inference
	infer_request.infer();
	
	// Retrieve a tensor representing the output data
	:ref:`ov::Tensor <doxid-classov_1_1_tensor>` output_tensor = infer_request.get_output_tensor();
	
	// For dynamic models output shape usually depends on input shape,
	// that means shape of output tensor is initialized after the first inference only
	// and has to be queried after every infer request
	auto output_shape_1 = output_tensor.:ref:`get_shape <doxid-classov_1_1_tensor_1a706163e01fb555eb9ccdfb5204cf7834>`();
	
	// Take a pointer of an appropriate type to tensor data and read elements according to the shape
	// Assuming model output is f32 data type
	auto data_1 = output_tensor.:ref:`data <doxid-classov_1_1_tensor_1aaf6d1cd69a759b31c65fed8b3e7d66fb>`<float>();
	// ... read values
	
	// The second inference call, repeat steps:
	
	// Create another tensor (if the previous one cannot be utilized)
	// Notice, the shape is different from input_tensor_1
	auto input_tensor_2 = :ref:`ov::Tensor <doxid-classov_1_1_tensor>`(:ref:`model <doxid-group__ov__runtime__cpp__prop__api_1ga461856fdfb6d7533dc53355aec9e9fad>`->input().get_element_type(), {1, 200});
	// ... write values to input_tensor_2
	
	infer_request.set_input_tensor(input_tensor_2);
	
	infer_request.infer();
	
	// No need to call infer_request.get_output_tensor() again
	// output_tensor queried after the first inference call above is valid here.
	// But it may not be true for the memory underneath as shape changed, so re-take a pointer:
	auto data_2 = output_tensor.:ref:`data <doxid-classov_1_1_tensor_1aaf6d1cd69a759b31c65fed8b3e7d66fb>`<float>();
	
	// and new shape as well
	auto output_shape_2 = output_tensor.:ref:`get_shape <doxid-classov_1_1_tensor_1a706163e01fb555eb9ccdfb5204cf7834>`();
	
	// ... read values in data_2 according to the shape output_shape_2

.. raw:: html

   </div>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="Python">





.. ref-code-block:: cpp

	# The first inference call
	
	# Create tensor compatible to the model input
	# Shape {1, 128} is compatible with any reshape statements made in previous examples
	input_tensor1 = :ref:`ov.Tensor <doxid-classov_1_1_tensor>`(model.input().element_type, [1, 128])
	# ... write values to input_tensor_1
	
	# Set the tensor as an input for the infer request
	infer_request.set_input_tensor(input_tensor1)
	
	# Do the inference
	infer_request.infer()
	
	# Or pass a tensor in infer to set the tensor as a model input and make the inference
	infer_request.infer([input_tensor1])
	
	# Or pass the numpy array to set inputs of the infer request
	input_data = np.ones(shape=[1, 128])
	infer_request.infer([input_data])
	
	# Retrieve a tensor representing the output data
	output_tensor = infer_request.get_output_tensor()
	
	# Copy data from tensor to numpy array
	data1 = output_tensor.data[:]
	
	# The second inference call, repeat steps:
	
	# Create another tensor (if the previous one cannot be utilized)
	# Notice, the shape is different from input_tensor_1
	input_tensor2 = :ref:`ov.Tensor <doxid-classov_1_1_tensor>`(model.input().element_type, [1, 200])
	# ... write values to input_tensor_2
	
	infer_request.infer([input_tensor2])
	
	# No need to call infer_request.get_output_tensor() again
	# output_tensor queried after the first inference call above is valid here.
	# But it may not be true for the memory underneath as shape changed, so re-take an output data:
	data2 = output_tensor.data[:]





.. raw:: html

   </div>







.. raw:: html

   </div>



In the example above, the ``set_input_tensor`` is used to specify input tensors. The real dimension of the tensor is always static, because it is a particular tensor and it does not have any dimension variations in contrast to model inputs.

Similar to static shapes, ``get_input_tensor`` can be used instead of ``set_input_tensor``. In contrast to static input shapes, when using ``get_input_tensor`` for dynamic inputs, the ``set_shape`` method for the returned tensor should be called to define the shape and allocate memory. Without doing so, the tensor returned by ``get_input_tensor`` is an empty tensor. The shape of the tensor is not initialized and memory is not allocated, because infer request does not have information about the real shape that will be provided. Setting shape for an input tensor is required when the corresponding input has at least one dynamic dimension, regardless of the bounds. Contrary to previous example, the following one shows the same sequence of two infer requests, using ``get_input_tensor`` instead of ``set_input_tensor`` :

.. raw:: html

   <div class='sphinxtabset'>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="C++">





.. ref-code-block:: cpp

	// The first inference call
	
	// Get the tensor; shape is not initialized
	auto input_tensor = infer_request.get_input_tensor();
	
	// Set shape is required
	input_tensor.set_shape({1, 128});
	// ... write values to input_tensor
	
	infer_request.infer();
	:ref:`ov::Tensor <doxid-classov_1_1_tensor>` output_tensor = infer_request.get_output_tensor();
	auto output_shape_1 = output_tensor.:ref:`get_shape <doxid-classov_1_1_tensor_1a706163e01fb555eb9ccdfb5204cf7834>`();
	auto data_1 = output_tensor.:ref:`data <doxid-classov_1_1_tensor_1aaf6d1cd69a759b31c65fed8b3e7d66fb>`<float>();
	// ... read values
	
	// The second inference call, repeat steps:
	
	// Set a new shape, may reallocate tensor memory
	input_tensor.set_shape({1, 200});
	// ... write values to input_tensor memory
	
	infer_request.infer();
	auto data_2 = output_tensor.:ref:`data <doxid-classov_1_1_tensor_1aaf6d1cd69a759b31c65fed8b3e7d66fb>`<float>();
	auto output_shape_2 = output_tensor.:ref:`get_shape <doxid-classov_1_1_tensor_1a706163e01fb555eb9ccdfb5204cf7834>`();
	// ... read values in data_2 according to the shape output_shape_2

.. raw:: html

   </div>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="Python">





.. ref-code-block:: cpp

	# Get the tensor, shape is not initialized
	input_tensor = infer_request.get_input_tensor()
	
	# Set shape is required
	input_tensor.shape = [1, 128]
	# ... write values to input_tensor
	
	infer_request.infer()
	output_tensor = infer_request.get_output_tensor()
	data1 = output_tensor.data[:]
	
	# The second inference call, repeat steps:
	
	# Set a new shape, may reallocate tensor memory
	input_tensor.shape = [1, 200]
	# ... write values to input_tensor
	
	infer_request.infer()
	data2 = output_tensor.data[:]





.. raw:: html

   </div>







.. raw:: html

   </div>





Dynamic Shapes in Outputs
-------------------------

Examples above are valid approaches when dynamic dimensions in output may be implied by propagation of dynamic dimension from the inputs. For example, batch dimension in an input shape is usually propagated through the whole model and appears in the output shape. It also applies to other dimensions, like sequence length for NLP models or spatial dimensions for segmentation models, that are propagated through the entire network.

Whether the output has dynamic dimensions or not can be verified by querying the output partial shape after the model is read or reshaped. The same applies to inputs. For example:

.. raw:: html

   <div class='sphinxtabset'>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="C++">





.. ref-code-block:: cpp

	// Print output partial shape
	std::cout << :ref:`model <doxid-group__ov__runtime__cpp__prop__api_1ga461856fdfb6d7533dc53355aec9e9fad>`->output().get_partial_shape() << "\n";
	
	// Print input partial shape
	std::cout << :ref:`model <doxid-group__ov__runtime__cpp__prop__api_1ga461856fdfb6d7533dc53355aec9e9fad>`->input().get_partial_shape() << "\n";

.. raw:: html

   </div>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="Python">





.. ref-code-block:: cpp

	# Print output partial shape
	print(model.output().partial_shape)
	
	# Print input partial shape
	print(model.input().partial_shape)





.. raw:: html

   </div>







.. raw:: html

   </div>



When there are dynamic dimensions in corresponding inputs or outputs, the ``?`` or ranges like ``1..10`` appear.

It can also be verified in a more programmatic way:

.. raw:: html

   <div class='sphinxtabset'>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="C++">





.. ref-code-block:: cpp

	auto :ref:`model <doxid-group__ov__runtime__cpp__prop__api_1ga461856fdfb6d7533dc53355aec9e9fad>` = core.:ref:`read_model <doxid-classov_1_1_core_1ae0576a95f841c3a6f5e46e4802716981>`("model.xml");
	
	if (:ref:`model <doxid-group__ov__runtime__cpp__prop__api_1ga461856fdfb6d7533dc53355aec9e9fad>`->input(0).get_partial_shape().is_dynamic()) {
	    // input is dynamic
	}
	
	if (:ref:`model <doxid-group__ov__runtime__cpp__prop__api_1ga461856fdfb6d7533dc53355aec9e9fad>`->output(0).get_partial_shape().is_dynamic()) {
	    // output is dynamic
	}
	
	if (:ref:`model <doxid-group__ov__runtime__cpp__prop__api_1ga461856fdfb6d7533dc53355aec9e9fad>`->output(0).get_partial_shape()[1].is_dynamic()) {
	    // 1-st dimension of output is dynamic
	}

.. raw:: html

   </div>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="Python">





.. ref-code-block:: cpp

	model = core.read_model("model.xml")
	
	if model.input(0).partial_shape.is_dynamic():
	    # input is dynamic
	    pass
	
	if model.output(0).partial_shape.is_dynamic():
	    # output is dynamic
	    pass
	
	if model.output(0).partial_shape[1].is_dynamic():
	    # 1-st dimension of output is dynamic
	    pass





.. raw:: html

   </div>







.. raw:: html

   </div>

If at least one dynamic dimension exists in an output of a model, a shape of the corresponding output tensor will be set as the result of inference call. Before the first inference, memory for such a tensor is not allocated and has the ``[0]`` shape. If the ``set_output_tensor`` method is called with a pre-allocated tensor, the inference will call the ``set_shape`` internally, and the initial shape is replaced by the calculated shape. Therefore, setting a shape for output tensors in this case is useful only when pre-allocating enough memory for output tensor. Normally, the ``set_shape`` method of a ``Tensor`` re-allocates memory only if a new shape requires more storage.
