.. index:: pair: page; Converting an ONNX Faster R-CNN Model
.. _doxid-openvino_docs__m_o__d_g_prepare_model_convert_model_onnx_specific__convert__faster__r_c_n_n:


Converting an ONNX Faster R-CNN Model
=====================================

:target:`doxid-openvino_docs__m_o__d_g_prepare_model_convert_model_onnx_specific__convert__faster__r_c_n_n_1md_openvino_docs_mo_dg_prepare_model_convert_model_onnx_specific_convert_faster_rcnn` The instructions below are applicable **only** to the Faster R-CNN model converted to the ONNX file format from the `maskrcnn-benchmark model <https://github.com/facebookresearch/maskrcnn-benchmark>`__ :

#. Download the pretrained model file from `onnx/models <https://github.com/onnx/models/tree/master/vision/object_detection_segmentation/faster-rcnn>`__ :
   
   * (commit-SHA: 8883e49e68de7b43e263d56b9ed156dfa1e03117).

#. Generate the Intermediate Representation of the model, by changing your current working directory to the Model Optimizer installation directory, and running Model Optimizer with the following parameters:
   
   .. ref-code-block:: cpp
   
   	 mo \
   	--input_model FasterRCNN-10.onnx \
   	--input_shape [1,3,800,800] \
   	--input 0:2 \
   	--mean_values [102.9801,115.9465,122.7717] \
   	--transformations_config front/onnx/faster_rcnn.json

Be aware that the height and width specified with the ``input_shape`` command line parameter could be different. For more information about supported input image dimensions and required pre- and post-processing steps, refer to the `Faster R-CNN article <https://github.com/onnx/models/tree/master/vision/object_detection_segmentation/faster-rcnn>`__.

#. Interpret the outputs of the generated IR: class indices, probabilities and box coordinates. Below are the outputs from the "DetectionOutput" layer:
   
   * class indices.
   
   * probabilities.
   
   * box coordinates.

