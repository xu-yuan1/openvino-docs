.. index:: pair: page; Converting an ONNX Mask R-CNN Model
.. _doxid-openvino_docs__m_o__d_g_prepare_model_convert_model_onnx_specific__convert__mask__r_c_n_n:


Converting an ONNX Mask R-CNN Model
===================================

:target:`doxid-openvino_docs__m_o__d_g_prepare_model_convert_model_onnx_specific__convert__mask__r_c_n_n_1md_openvino_docs_mo_dg_prepare_model_convert_model_onnx_specific_convert_mask_rcnn` The instructions below are applicable **only** to the Mask R-CNN model converted to the ONNX file format from the `maskrcnn-benchmark model <https://github.com/facebookresearch/maskrcnn-benchmark>`__.

#. Download the pretrained model file from `onnx/models <https://github.com/onnx/models/tree/master/vision/object_detection_segmentation/mask-rcnn>`__ :
   
   * commit-SHA: 8883e49e68de7b43e263d56b9ed156dfa1e03117.

#. Generate the Intermediate Representation of the model by changing your current working directory to the Model Optimizer installation directory and running Model Optimizer with the following parameters:
   
   .. ref-code-block:: cpp
   
   	 mo \
   	--input_model mask_rcnn_R_50_FPN_1x.onnx \
   	--input "0:2" \
   	--input_shape [1,3,800,800] \
   	--mean_values [102.9801,115.9465,122.7717] \
   	--transformations_config front/onnx/mask_rcnn.json

Be aware that the height and width specified with the ``input_shape`` command line parameter could be different. For more information about supported input image dimensions and required pre- and post-processing steps, refer to the `documentation <https://github.com/onnx/models/tree/master/vision/object_detection_segmentation/mask-rcnn>`__.

#. Interpret the outputs of the generated IR file: masks, class indices, probabilities and box coordinates.
   
   * masks.
   
   * class indices.
   
   * probabilities.
   
   * box coordinates.

The first one is a layer with the name ``6849/sink_port_0``, and rest are outputs from the ``DetectionOutput`` layer.

