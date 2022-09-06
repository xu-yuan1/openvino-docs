.. index:: pair: page; Converting TensorFlow Object Detection API Models
.. _doxid-openvino_docs__m_o__d_g_prepare_model_convert_model_tf_specific__convert__object__detection__a_p_i__models:


Converting TensorFlow Object Detection API Models
=================================================

:target:`doxid-openvino_docs__m_o__d_g_prepare_model_convert_model_tf_specific__convert__object__detection__a_p_i__models_1md_openvino_docs_mo_dg_prepare_model_convert_model_tf_specific_convert_object_detection_api_models`	**NOTES** :

* Starting with the 2022.1 release, Model Optimizer can convert the TensorFlow Object Detection API Faster and Mask RCNNs topologies differently. By default, Model Optimizer adds operation "Proposal" to the generated IR. This operation needs an additional input to the model with name "image_info" which should be fed with several values describing the preprocessing applied to the input image (refer to the :ref:`Proposal <doxid-openvino_docs_ops_detection__proposal_4>` operation specification for more information). However, this input is redundant for the models trained and inferred with equal size images. Model Optimizer can generate IR for such models and insert operation :ref:`DetectionOutput <doxid-openvino_docs_ops_detection__detection_output_1>` instead of ``Proposal``. The ``DetectionOutput`` operation does not require additional model input "image_info". Moreover, for some models the produced inference results are closer to the original TensorFlow model. In order to trigger new behavior, the attribute "operation_to_add" in the corresponding JSON transformation configuration file should be set to value "DetectionOutput" instead of default one "Proposal".

* Starting with the 2021.1 release, Model Optimizer converts the TensorFlow Object Detection API SSDs, Faster and Mask RCNNs topologies keeping shape-calculating sub-graphs by default, so topologies can be re-shaped in the OpenVINO Runtime using dedicated reshape API. Refer to the :ref:`Using Shape Inference <deploy_infer__shape_inference>` guide for more information on how to use this feature. It is possible to change the both spatial dimensions of the input image and batch size.

* To generate IRs for TF 1 SSD topologies, Model Optimizer creates a number of ``PriorBoxClustered`` operations instead of a constant node with prior boxes calculated for the particular input image size. This change allows you to reshape the topology in the OpenVINO Runtime using dedicated API. The reshaping is supported for all SSD topologies except FPNs, which contain hardcoded shapes for some operations preventing from changing topology input shape.



Converting a Model
~~~~~~~~~~~~~~~~~~

You can download TensorFlow Object Detection API models from the `TensorFlow 1 Detection Model Zoo <https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/tf1_detection_zoo.md>`__ or `TensorFlow 2 Detection Model Zoo <https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/tf2_detection_zoo.md>`__.

.. note::

   Before converting, make sure you have configured Model Optimizer. 
   For configuration steps, refer to the 
   :ref:`Configuring Model Optimizer <conv_prep__conv_with_model_optimizer>`.



To convert a TensorFlow Object Detection API model, run the ``mo`` command with the following required parameters:

* ``--input_model <path_to_frozen.pb>`` File with a pretrained model (binary or text .pb file after freezing) OR ``--saved_model_dir <path_to_saved_model>`` for the TensorFlow 2 models

* ``--transformations_config <path_to_subgraph_replacement_configuration_file.json>`` A subgraph replacement configuration file with transformations description. For the models downloaded from the TensorFlow Object Detection API zoo, you can find the configuration files in the ``<PYTHON_SITE_PACKAGES>/openvino/tools/mo/front/tf`` directory. Use:
  
  * ``ssd_v2_support.json`` for frozen SSD topologies from the models zoo version up to 1.13.X inclusively
  
  * ``ssd_support_api_v.1.14.json`` for SSD topologies trained using the TensorFlow Object Detection API version 1.14 up to 1.14.X inclusively
  
  * ``ssd_support_api_v.1.15.json`` for SSD topologies trained using the TensorFlow Object Detection API version 1.15 up to 2.0
  
  * ``ssd_support_api_v.2.0.json`` for SSD topologies trained using the TensorFlow Object Detection API version 2.0 up to 2.3.X inclusively
  
  * ``ssd_support_api_v.2.4.json`` for SSD topologies trained using the TensorFlow Object Detection API version 2.4 or higher
  
  * ``efficient_det_support_api_v.2.0.json`` for EfficientDet topologies trained using the TensorFlow Object Detection API version 2.0 up to 2.3.X inclusively
  
  * ``efficient_det_support_api_v.2.4.json`` for EfficientDet topologies trained using the TensorFlow Object Detection API version 2.4 or higher
  
  * ``faster_rcnn_support.json`` for Faster R-CNN topologies from the TF 1.X models zoo trained with TensorFlow version up to 1.6.X inclusively
  
  * ``faster_rcnn_support_api_v1.7.json`` for Faster R-CNN topologies trained using the TensorFlow Object Detection API version 1.7.0 up to 1.9.X inclusively
  
  * ``faster_rcnn_support_api_v1.10.json`` for Faster R-CNN topologies trained using the TensorFlow Object Detection API version 1.10.0 up to 1.12.X inclusively
  
  * ``faster_rcnn_support_api_v1.13.json`` for Faster R-CNN topologies trained using the TensorFlow Object Detection API version 1.13.X
  
  * ``faster_rcnn_support_api_v1.14.json`` for Faster R-CNN topologies trained using the TensorFlow Object Detection API version 1.14.0 up to 1.14.X inclusively
  
  * ``faster_rcnn_support_api_v1.15.json`` for Faster R-CNN topologies trained using the TensorFlow Object Detection API version 1.15.0 up to 2.0
  
  * ``faster_rcnn_support_api_v2.0.json`` for Faster R-CNN topologies trained using the TensorFlow Object Detection API version 2.0 up to 2.3.X inclusively
  
  * ``faster_rcnn_support_api_v2.4.json`` for Faster R-CNN topologies trained using the TensorFlow Object Detection API version 2.4 or higher
  
  * ``mask_rcnn_support.json`` for Mask R-CNN topologies from the TF 1.X models zoo trained with TensorFlow version 1.9.0 or lower.
  
  * ``mask_rcnn_support_api_v1.7.json`` for Mask R-CNN topologies trained using the TensorFlow Object Detection API version 1.7.0 up to 1.9.X inclusively
  
  * ``mask_rcnn_support_api_v1.11.json`` for Mask R-CNN topologies trained using the TensorFlow Object Detection API version 1.11.0 up to 1.12.X inclusively
  
  * ``mask_rcnn_support_api_v1.13.json`` for Mask R-CNN topologies trained using the TensorFlow Object Detection API version 1.13.0 up to 1.13.X inclusively
  
  * ``mask_rcnn_support_api_v1.14.json`` for Mask R-CNN topologies trained using the TensorFlow Object Detection API version 1.14.0 up to 1.14.X inclusively
  
  * ``mask_rcnn_support_api_v1.15.json`` for Mask R-CNN topologies trained using the TensorFlow Object Detection API version 1.15.0 up to 2.0
  
  * ``mask_rcnn_support_api_v2.0.json`` for Mask R-CNN topologies trained using the TensorFlow Object Detection API version 2.0 up to 2.3.X inclusively
  
  * ``mask_rcnn_support_api_v2.4.json`` for Mask R-CNN topologies trained using the TensorFlow Object Detection API version 2.4 or higher
  
  * ``rfcn_support.json`` for RFCN topology from the models zoo trained with TensorFlow version up to 1.9.X inclusively
  
  * ``rfcn_support_api_v1.10.json`` for RFCN topology from the models zoo frozen with TensorFlow version 1.10.0 up to 1.12.X inclusively
  
  * ``rfcn_support_api_v1.13.json`` for RFCN topology from the models zoo frozen with TensorFlow version 1.13.X
  
  * ``rfcn_support_api_v1.14.json`` for RFCN topology from the models zoo frozen with TensorFlow version 1.14.0 or higher

* ``--tensorflow_object_detection_api_pipeline_config <path_to_pipeline.config>`` A special configuration file that describes the topology hyper-parameters and structure of the TensorFlow Object Detection API model. For the models downloaded from the TensorFlow Object Detection API zoo, the configuration file is named ``pipeline.config``. If you plan to train a model yourself, you can find templates for these files in the `models repository <https://github.com/tensorflow/models/tree/master/research/object_detection/samples/configs>`__.

* ``--input_shape`` (optional) A custom input image shape. For more information how the ``--input_shape`` parameter is handled for the TensorFlow Object Detection API models, refer to the `Custom Input Shape <#custom-input-shape>`__ guide.

.. note::

   The color channel order (RGB or BGR) of an input data should match the channel order 
   of the model training dataset. If they are different, perform the ``RGB<->BGR`` conversion 
   specifying the command-line parameter: ``--reverse_input_channels``. Otherwise, 
   inference results may be incorrect. If you convert a TensorFlow Object Detection API model 
   to use with the OpenVINO sample applications, you must specify the ``--reverse_input_channels`` 
   parameter. For more information about the parameter, refer to the **When to Reverse Input Channels** 
   section of the :ref:`Converting a Model to Intermediate Representation (IR) <conv_prep__set_input_shapes>` guide.



Additionally to the mandatory parameters listed above you can use optional conversion parameters if needed. A full list of parameters is available in the :ref:`Converting a TensorFlow Model <conv_prep__conv_from_tensorflow>` guide.

For example, if you downloaded the pre-trained `SSD InceptionV2 topology <http://download.tensorflow.org/models/object_detection/ssd_inception_v2_coco_2018_01_28.tar.gz>`__ and extracted archive to the directory ``/tmp/ssd_inception_v2_coco_2018_01_28``, the sample command line to convert the model looks as follows:

.. ref-code-block:: cpp

	mo --input_model=/tmp/ssd_inception_v2_coco_2018_01_28/frozen_inference_graph.pb --transformations_config front/tf/ssd_v2_support.json --tensorflow_object_detection_api_pipeline_config /tmp/ssd_inception_v2_coco_2018_01_28/pipeline.config --reverse_input_channels

OpenVINO™ Toolkit Samples and Open Model Zoo Demos
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

OpenVINO comes with a number of samples to demonstrate use of OpenVINO Runtime API. Additionally, Open Model Zoo provides set of demo applications to show implementation of close to real life applications, based on deep learning in various tasks, including Image Classification, Visual Object Detection, Text Recognition, Speech Recognition, Natural Language Processing and others. Refer to the links below for more details.

* :ref:`OpenVINO Samples <get_started__samples_overview>`

* Open Model Zoo Demos

Feeding Input Images to the Samples
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

There are several important notes about feeding input images to the samples:

#. OpenVINO samples stretch input image to the size of the input operation without preserving aspect ratio. This behavior is usually correct for most topologies (including SSDs), but incorrect for other models like Faster R-CNN, Mask R-CNN and R-FCN. These models usually use keeps aspect ratio resizer. The type of preprocessing is defined in the pipeline configuration file in the section ``image_resizer``. If keeping aspect ratio is used, then it is necessary to resize image before passing it to the sample and optionally pad the resized image with 0s (if the attribute "pad_to_max_dimension" in the pipeline.config is equal to "true").

#. TensorFlow implementation of image resize may be different from the one implemented in the sample. Even reading input image from compressed format (like ``.jpg``) could give different results in the sample and TensorFlow. If it is necessary to compare accuracy between the TensorFlow and the OpenVINO, it is recommended to pass pre-resized input image in a non-compressed format (like ``.bmp``).

#. If you want to infer the model with the OpenVINO samples, convert the model specifying the ``--reverse_input_channels`` command line parameter. The samples load images in BGR channels order, while TensorFlow models were trained with images in RGB order. When the ``--reverse_input_channels`` command line parameter is specified, Model Optimizer performs first convolution or other channel dependent operation weights modification so the output will be like the image is passed with RGB channels order.

#. Read carefully the messages printed by Model Optimizer during a model conversion. They contain important instructions on how to prepare input data before running the inference and how to interpret the output.

:target:`doxid-openvino_docs__m_o__d_g_prepare_model_convert_model_tf_specific__convert__object__detection__a_p_i__models_1custom-input-shape`

Custom Input Shape
~~~~~~~~~~~~~~~~~~

Model Optimizer handles the command line parameter ``--input_shape`` for TensorFlow Object Detection API models in a special way depending on the image resizer type defined in the ``pipeline.config`` file. TensorFlow Object Detection API generates different ``Preprocessor`` sub-graph based on the image resizer type. Model Optimizer supports two types of image resizer:

* ``fixed_shape_resizer`` *Stretches* input image to the specific height and width. The ``pipeline.config`` snippet below shows a ``fixed_shape_resizer`` sample definition:
  
  .. ref-code-block:: cpp
  
  	image_resizer {
  	  fixed_shape_resizer {
  	    height: 300
  	    width: 300
  	  }
  	}

* ``keep_aspect_ratio_resizer`` Resizes the input image *keeping aspect ratio* to satisfy the minimum and maximum size constraints. The ``pipeline.config`` snippet below shows a ``keep_aspect_ratio_resizer`` sample definition:
  
  .. ref-code-block:: cpp
  
  	image_resizer {
  	  keep_aspect_ratio_resizer {
  	    min_dimension: 600
  	    max_dimension: 1024
  	  }
  	}
  
  If an additional parameter "pad_to_max_dimension" is equal to "true", then the resized image will be padded with 0s to the square image of size "max_dimension".

Fixed Shape Resizer Replacement
-------------------------------

* If the ``--input_shape`` command line parameter is not specified, Model Optimizer generates an input operation with the height and width as defined in the ``pipeline.config``.

* If the ``--input_shape [1, H, W, 3]`` command line parameter is specified, Model Optimizer sets the input operation height to ``H`` and width to ``W`` and convert the model. However, the conversion may fail because of the following reasons:
  
  * The model is not reshape-able, meaning that it's not possible to change the size of the model input image. For example, SSD FPN models have ``Reshape`` operations with hard-coded output shapes, but the input size to these ``Reshape`` instances depends on the input image size. In this case, Model Optimizer shows an error during the shape inference phase. Run Model Optimizer with ``--log_level DEBUG`` to see the inferred operations output shapes to see the mismatch.
  
  * Custom input shape is too small. For example, if you specify ``--input_shape [1,100,100,3]`` to convert a SSD Inception V2 model, one of convolution or pooling nodes decreases input tensor spatial dimensions to non-positive values. In this case, Model Optimizer shows error message like this: '[ ERROR ] Shape [ 1 -1 -1 256] is not fully defined for output X of "node_name".'

Keeping Aspect Ratio Resizer Replacement
----------------------------------------

* If the ``--input_shape`` command line parameter is not specified, Model Optimizer generates an input operation with both height and width equal to the value of parameter ``min_dimension`` in the ``keep_aspect_ratio_resizer``.

* If the ``--input_shape [1, H, W, 3]`` command line parameter is specified, Model Optimizer scales the specified input image height ``H`` and width ``W`` to satisfy the ``min_dimension`` and ``max_dimension`` constraints defined in the ``keep_aspect_ratio_resizer``. The following function calculates the input operation height and width:

.. ref-code-block:: cpp

	def calculate_shape_keeping_aspect_ratio(H: int, W: int, min_dimension: int, max_dimension: int):
	    ratio_min = min_dimension / :ref:`min <doxid-namespacengraph_1_1runtime_1_1reference_1abc42885cb896b121ab5ac214cbf60935>`(H, W)
	    ratio_max = max_dimension / :ref:`max <doxid-namespacengraph_1_1runtime_1_1reference_1a92cfabd79e866544fb35d44884e7adfd>`(H, W)
	    ratio = :ref:`min <doxid-namespacengraph_1_1runtime_1_1reference_1abc42885cb896b121ab5ac214cbf60935>`(ratio_min, ratio_max)
	    return int(:ref:`round <doxid-namespacengraph_1_1runtime_1_1reference_1a8ea383ca6ce01d26eabe1c27a0e1bd37>`(H \* ratio)), int(:ref:`round <doxid-namespacengraph_1_1runtime_1_1reference_1a8ea383ca6ce01d26eabe1c27a0e1bd37>`(W \* ratio))

The ``--input_shape`` command line parameter should be specified only if the "pad_to_max_dimension" does not exist of is set to "false" in the ``keep_aspect_ratio_resizer``.

Models with ``keep_aspect_ratio_resizer`` were trained to recognize object in real aspect ratio, in contrast with most of the classification topologies trained to recognize objects stretched vertically and horizontally as well. By default, Model Optimizer converts topologies with ``keep_aspect_ratio_resizer`` to consume a square input image. If the non-square image is provided as input, it is stretched without keeping aspect ratio that results to object detection quality decrease.

.. note::

   It is highly recommended to specify the ``--input_shape`` command line parameter 
   for the models with ``keep_aspect_ratio_resizer``, if the input image dimensions are known in advance.



Model Conversion Process in Detail
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This section is intended for users who want to understand how Model Optimizer performs Object Detection API models conversion in details. The information in this section is also useful for users having complex models that are not converted with Model Optimizer out of the box. It is highly recommended to read the **Graph Transformation Extensions** section in the :ref:`Model Optimizer Extensibility <extensibility__model_optimizer>` documentation first to understand sub-graph replacement concepts which are used here.

It is also important to open the model in the `TensorBoard <https://www.tensorflow.org/guide/summaries_and_tensorboard>`__ to see the topology structure. Model Optimizer can create an event file that can be then fed to the TensorBoard tool. Run Model Optimizer, providing two command line parameters:

* ``--input_model <path_to_frozen.pb>`` Path to the frozen model.

* ``--tensorboard_logdir`` Path to the directory where TensorBoard looks for the event files.

Implementation of the transformations for Object Detection API models is located in the file `https://github.com/openvinotoolkit/openvino/blob/releases/2022/1/tools/mo/openvino/tools/mo/front/tf/ObjectDetectionAPI.py <https://github.com/openvinotoolkit/openvino/blob/releases/2022/1/tools/mo/openvino/tools/mo/front/tf/ObjectDetectionAPI.py>`__. Refer to the code in this file to understand the details of the conversion process.

