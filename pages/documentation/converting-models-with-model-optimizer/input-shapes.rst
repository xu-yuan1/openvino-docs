.. index:: pair: page; Setting Input Shapes
.. _conv_prep__set_input_shapes:

.. meta:: 
   :description: When provided an additional shape definition with --input_shape 
                 and --static_shape parameters, Model Optimizer can increase 
                 efficiency of a model.
   :keywords: Model Optimizer, deep learning model, convert a model, set input shape, 
              --input_shape parameter, --static_shape parameter, dynamic input shapes, 
              undefined dimensions, infer a model, model inference, --input_model 
              parameter, TensorFlow, input shape, dynamic shapes, boundaries of 
              dimensions, non-reshape-able models, reshape method, OpenVINO, 
              OpenVINO Intermediate Representation, OpenVINO IR, static shapes, 
              command-line parameter, OpenVINO Runtime API


Setting Input Shapes
====================

:target:`conv_prep__set_input_shapes_1md_openvino_docs_mo_dg_prepare_model_convert_model_converting_model` 

With Model Optimizer you can increase your model's efficiency by providing an additional shape definition, with these two parameters: ``--input_shape`` and ``--static_shape``.

:target:`conv_prep__set_input_shapes_when_to_specify_input_shapes`

Specifying input_shape Command-line Parameter
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Model Optimizer supports conversion of models with dynamic input shapes that contain undefined dimensions. However, if the shape of data is not going to change from one inference request to another, it is recommended to set up static shapes (when all dimensions are fully defined) for the inputs. Doing it at this stage, instead of during inference in runtime, can be beneficial in terms of performance and memory consumption. To set up static shapes, Model Optimizer provides the ``--input_shape`` parameter. For more information on input shapes under runtime, refer to the :ref:`Changing input shapes <deploy_infer__shape_inference>` guide. To learn more about dynamic shapes in runtime, refer to the :ref:`Dynamic Shapes <deploy_infer__dynamic_shapes>` guide.

The OpenVINO Runtime API may present certain limitations in inferring models with undefined dimensions on some hardware. See the :ref:`Features support matrix <deploy_infer__working_with_devices>` for reference. In this case, the ``--input_shape`` parameter and the :ref:`reshape method <deploy_infer__shape_inference>` can help to resolve undefined dimensions.

Sometimes, Model Optimizer is unable to convert models out-of-the-box (only the ``--input_model`` parameter is specified). Such problem can relate to models with inputs of undefined ranks and a case of cutting off parts of a model. In this case, input shapes must be specified explicitly with the ``--input_shape`` parameter.

For example, run Model Optimizer for the TensorFlow MobileNet model with the single input and specify the input shape of ``[2,300,300,3]`` :

.. ref-code-block:: cpp

	mo --input_model MobileNet.pb --input_shape [2,300,300,3]

If a model has multiple inputs, ``--input_shape`` must be used in conjunction with ``--input`` parameter. The ``--input`` parameter contains a list of input names, for which shapes in the same order are defined via ``--input_shape``. For example, launch Model Optimizer for the ONNX OCR model with a pair of inputs ``data`` and ``seq_len`` and specify shapes ``[3,150,200,1]`` and ``[3]`` for them:

.. ref-code-block:: cpp

	mo --input_model ocr.onnx --input data,seq_len --input_shape [3,150,200,1],[3]

Alternatively, specify input shapes, using the ``--input`` parameter as follows:

.. ref-code-block:: cpp

	mo --input_model ocr.onnx --input data[3 150 200 1],seq_len[3]

The ``--input_shape`` parameter allows overriding original input shapes to ones compatible with a given model. Dynamic shapes, i.e. with dynamic dimensions, can be replaced in the original model with static shapes for the converted model, and vice versa. The dynamic dimension can be marked in Model Optimizer command-line as ``-1`` \* or \* ``?``. For example, launch Model Optimizer for the ONNX OCR model and specify dynamic batch dimension for inputs:

.. ref-code-block:: cpp

	mo --input_model ocr.onnx --input data,seq_len --input_shape [-1,150,200,1],[-1]

To optimize memory consumption for models with undefined dimensions in run-time, Model Optimizer provides the capability to define boundaries of dimensions. The boundaries of undefined dimension can be specified with ellipsis. For example, launch Model Optimizer for the ONNX OCR model and specify a boundary for the batch dimension:

.. ref-code-block:: cpp

	mo --input_model ocr.onnx --input data,seq_len --input_shape [1..3,150,200,1],[1..3]

Practically, some models are not ready for input shapes change. In this case, a new input shape cannot be set via Model Optimizer. For more information about shape follow the :ref:`inference troubleshooting <deploy_infer__shape_inference_1troubleshooting_reshape_errors>` and :ref:`ways to relax shape inference flow <deploy_infer__shape_inference_1how-to-fix-non-reshape-able-model>` guides.

Specifying static_shape Command-line Parameter
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Model Optimizer provides the ``--static_shape`` parameter that allows evaluating shapes of all operations in the model for fixed input shapes and folding shape computing sub-graphs into constants. The resulting IR may be more compact in size and the loading time for such IR may decrease. However, the resulting IR will not be reshape-able with the help of the :ref:`reshape method <deploy_infer__shape_inference>` from OpenVINO Runtime API. It is worth noting that the ``--input_shape`` parameter does not affect reshapeability of the model.

For example, launch Model Optimizer for the ONNX OCR model using ``--static_shape`` :

.. ref-code-block:: cpp

	mo --input_model ocr.onnx --input data[3 150 200 1],seq_len[3] --static_shape

Additional Resources
~~~~~~~~~~~~~~~~~~~~

* :ref:`Introduction to converting models with Model Optimizer <conv_prep__conv_with_model_optimizer>`

* :ref:`Cutting Off Parts of a Model <doxid-openvino_docs__m_o__d_g_prepare_model_convert_model__cutting__model>`

