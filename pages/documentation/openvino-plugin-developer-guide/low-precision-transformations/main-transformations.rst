.. index:: pair: page; Step 3. Main Transformations
.. _plugin_lpt__step3_main_transformations:

.. meta::
   :description: Step 3 of low precision transformations. Feature a list of transforamtions used to 
                 decomposition transformation and dequantization operations handling.
   :keywords: low precision transformations, lpt, Main Transformations, decomposition transformation,
              dequantization operation handling, AddTransformation, AvgPoolTransformation, 
              ClampTransformation, ConcatTransformation, ConvolutionTransformation, 
              ConvolutionBackpropDataTransformation, DepthToSpaceTransformation, 
              FakeQuantizeDecompositionTransformation, FakeQuantizeTransformation, InterpolateTransformation,
              GroupConvolutionTransformation, MatMulTransformation, MaxPoolTransformation, 
              MultiplyTransformation, MVNTransformation, NormalizeL2Transformation, PReluTransformation, 
              ReduceMaxTransformation, ReduceMeanTransformation, ReduceMinTransformation, ReduceSumTransformation, 
              ReluTransformation, ReshapeTransformation, SqueezeTransformation, ShuffleChannelsTransformation, 
              SplitTransformation, StridedSliceTransformation, TransposeTransformation, UnsqueezeTransformation, 
              VariadicSplitTransformation, FakeQuantize


Step 3. Main Transformations
============================

:target:`plugin_lpt__step3_main_transformations_1md_openvino_docs_ie_plugin_dg_plugin_transformation_pipeline_low_precision_transformations_pipeline_step3_main` Main transformations are the majority of low precision transformations. Transformations operate with dequantization operations. Main transformations include:

* :ref:`AddTransformation <lpt_transformations__add_transformation>`

* :ref:`AvgPoolTransformation <lpt_transformations__avg_pool_transformation>`

* :ref:`ClampTransformation <lpt_transformations__clamp_transformation>`

* :ref:`ConcatTransformation <lpt_transformations__concat_transformation>`

* :ref:`ConvolutionTransformation <lpt_transformations__convolution_transformation>`

* :ref:`ConvolutionBackpropDataTransformation <lpt_transformations__convolution_backprop_data_transformation>`

* :ref:`DepthToSpaceTransformation <lpt_transformations__depth_to_space_transformation>`

* :ref:`FakeQuantizeDecompositionTransformation <lpt_transformations__fake_quantize_decomposition_transformation>`

* :ref:`FakeQuantizeTransformation <lpt_transformations__fake_quantize_transformation>`

* :ref:`InterpolateTransformation <lpt_transformations__interpolate_transformation>`

* :ref:`GroupConvolutionTransformation <lpt_transformations__group_convolution_transformation>`

* :ref:`MatMulTransformation <lpt_transformations__mat_mul_transformation>`

* :ref:`MaxPoolTransformation <lpt_transformations__max_pool_transformation>`

* :ref:`MultiplyTransformation <lpt_transformations__multiply_transformation>`

* :ref:`MVNTransformation <lpt_transformations__mvn_transformation>`

* :ref:`NormalizeL2Transformation <lpt_transformations__normalize_l2_transformation>`

* :ref:`PReluTransformation <lpt_transformations__p_relu_transformation>`

* :ref:`ReduceMaxTransformation <lpt_transformations__reduce_max_transformation>`

* :ref:`ReduceMeanTransformation <lpt_transformations__reduce_mean_transformation>`

* :ref:`ReduceMinTransformation <lpt_transformations__reduce_min_transformation>`

* :ref:`ReduceSumTransformation <lpt_transformations__reduce_sum_transformation>`

* :ref:`ReluTransformation <lpt_transformations__relu_transformation>`

* :ref:`ReshapeTransformation <lpt_transformations__reshape_transformation>`

* :ref:`SqueezeTransformation <lpt_transformations__squeeze_transformation>`

* :ref:`ShuffleChannelsTransformation <lpt_transformations__shuffle_channels_transformation>`

* :ref:`SplitTransformation <lpt_transformations__split_transformation>`

* :ref:`StridedSliceTransformation <lpt_transformations__strided_slice_transformation>`

* :ref:`TransposeTransformation <lpt_transformations__transpose_transformation>`

* :ref:`UnsqueezeTransformation <lpt_transformations__unsqueeze_transformation>`

* :ref:`VariadicSplitTransformation <lpt_transformations__variadic_split_transformation>`

Let's explore some main transformations on the example model. Original model:

.. image:: ./_assets/step3_original.png
	:alt: Original model

Result model after main transformations:

.. image:: ./_assets/step3_transformed.png
	:alt: Original model

Changes in the example model after main transformation:

* All ``FakeQuantize`` operations (``fakeQuantize1``, ``fakeQuantize2`` and ``fakeQuantize3``) were decomposed:
  
  * original ``FakeQuantize`` operations were replaced with new operations with other output intervals and output port precision,
  
  * dequantization operations.

* Dequantization operations were moved via precision preserved (``concat1`` and ``concat2``) and quantized (``convolution2``) operations.

.. note::
   The left branch (branch #1) does not require per-tensor quantization. As a result, the ``fakeQuantize1`` output 
   interval is [0, 255]. But quantized ``convolution2`` requires per-tensor quantization on the right branch (branch #2). 
   Then all connected ``FakeQuantize`` interval operations (``fakeQuantize1`` and ``fakeQuantize2``) are aligned to have 
   per-tensor quantization after the concatenation (``concat2``) operation.

