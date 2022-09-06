.. index:: pair: page; Converting a PaddlePaddle Model
.. _conv_prep__conv_from_paddle:

.. meta:: 
   :description: Detailed instructions on how to convert a model from the 
                 PaddlePaddle format to the OpenVINO IR by using Model Optimizer. 
   :keywords: Model Optimizer, OpenVINO IR, OpenVINO Intermediate Representation, 
              OpenVINO Development Tools, convert model, model conversion, convert 
              from PaddlePaddle, convert a PaddlePaddle model, --input_model, 
              supported PaddlePaddle layers, --reverse_input_channels, convert to 
              OpenVINO IR

Converting a PaddlePaddle Model
===============================

:target:`conv_prep__conv_from_paddle_1md_openvino_docs_mo_dg_prepare_model_convert_model_convert_model_from_paddle` To convert a PaddlePaddle model, use the ``mo`` script and specify the path to the input ``.pdmodel`` model file:

.. ref-code-block:: cpp

	mo --input_model <INPUT_MODEL>.pdmodel

**For example,** this command converts a yolo v3 PaddlePaddle network to OpenVINO IR network:

.. ref-code-block:: cpp

	mo --input_model=yolov3.pdmodel --input=image,im_shape,scale_factor --input_shape=[1,3,608,608],[1,2],[1,2] --reverse_input_channels --output=save_infer_model/scale_0.tmp_1,save_infer_model/scale_1.tmp_1

Supported PaddlePaddle Layers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For the list of supported standard layers, refer to the :ref:`Supported Framework Layers <doxid-openvino_docs__m_o__d_g_prepare_model__supported__frameworks__layers>` page.

Officially Supported PaddlePaddle Models
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The following PaddlePaddle models have been officially validated and confirmed to work (as of OpenVINO 2022.1):

.. list-table::
   :widths: 20 25 55
   :header-rows: 1

   * - Model Name
     - Model Type
     - Description
   * - ppocr-det
     - optical character recognition
     - Models are exported from `PaddleOCR <https://github.com/PaddlePaddle/PaddleOCR/tree/release/2.1/>`_. Refer to `READ.md <https://github.com/PaddlePaddle/PaddleOCR/tree/release/2.1/#pp-ocr-20-series-model-listupdate-on-dec-15>`_.
   * - ppocr-rec
     - optical character recognition
     - Models are exported from `PaddleOCR <https://github.com/PaddlePaddle/PaddleOCR/tree/release/2.1/>`_. Refer to `READ.md <https://github.com/PaddlePaddle/PaddleOCR/tree/release/2.1/#pp-ocr-20-series-model-listupdate-on-dec-15>`_.
   * - ResNet-50
     - classification
     - Models are exported from `PaddleClas <https://github.com/PaddlePaddle/PaddleClas/tree/release/2.1/>`_. Refer to `getting_started_en.md <https://github.com/PaddlePaddle/PaddleClas/blob/release/2.1/docs/en/tutorials/getting_started_en.md#4-use-the-inference-model-to-predict>`_.
   * - MobileNet v2
     - classification
     - Models are exported from `PaddleClas <https://github.com/PaddlePaddle/PaddleClas/tree/release/2.1/>`_. Refer to `getting_started_en.md <https://github.com/PaddlePaddle/PaddleClas/blob/release/2.1/docs/en/tutorials/getting_started_en.md#4-use-the-inference-model-to-predict>`_.
   * - MobileNet v3
     - classification
     - Models are exported from `PaddleClas <https://github.com/PaddlePaddle/PaddleClas/tree/release/2.1/>`_. Refer to `getting_started_en.md <https://github.com/PaddlePaddle/PaddleClas/blob/release/2.1/docs/en/tutorials/getting_started_en.md#4-use-the-inference-model-to-predict>`_.
   * - BiSeNet v2
     - semantic segmentation
     - Models are exported from `PaddleSeg <https://github.com/PaddlePaddle/PaddleSeg/tree/release/2.1>`_. Refer to `model_export.md <https://github.com/PaddlePaddle/PaddleSeg/blob/release/2.1/docs/model_export.md#>`_.
   * - DeepLab v3 plus
     - semantic segmentation
     - Models are exported from `PaddleSeg <https://github.com/PaddlePaddle/PaddleSeg/tree/release/2.1>`_. Refer to `model_export.md <https://github.com/PaddlePaddle/PaddleSeg/blob/release/2.1/docs/model_export.md#>`_.
   * - Fast-SCNN
     - semantic segmentation
     - Models are exported from `PaddleSeg <https://github.com/PaddlePaddle/PaddleSeg/tree/release/2.1>`_. Refer to `model_export.md <https://github.com/PaddlePaddle/PaddleSeg/blob/release/2.1/docs/model_export.md#>`_.
   * - OCRNET
     - semantic segmentation
     - Models are exported from `PaddleSeg <https://github.com/PaddlePaddle/PaddleSeg/tree/release/2.1>`_. Refer to `model_export.md <https://github.com/PaddlePaddle/PaddleSeg/blob/release/2.1/docs/model_export.md#>`_.
   * - Yolo v3
     - detection
     - Models are exported from `PaddleDetection <https://github.com/PaddlePaddle/PaddleDetection/tree/release/2.1>`_. Refer to `EXPORT_MODEL.md <https://github.com/PaddlePaddle/PaddleDetection/blob/release/2.1/deploy/EXPORT_MODEL.md#>`_.
   * - ppyolo
     - detection
     - Models are exported from `PaddleDetection <https://github.com/PaddlePaddle/PaddleDetection/tree/release/2.1>`_. Refer to `EXPORT_MODEL.md <https://github.com/PaddlePaddle/PaddleDetection/blob/release/2.1/deploy/EXPORT_MODEL.md#>`_.
   * - MobileNetv3-SSD
     - detection
     - Models are exported from `PaddleDetection <https://github.com/PaddlePaddle/PaddleDetection/tree/release/2.2>`_. Refer to `EXPORT_MODEL.md <https://github.com/PaddlePaddle/PaddleDetection/blob/release/2.2/deploy/EXPORT_MODEL.md#>`_.
   * - U-Net
     - semantic segmentation
     - Models are exported from `PaddleSeg <https://github.com/PaddlePaddle/PaddleSeg/tree/release/2.3>`_. Refer to `model_export.md <https://github.com/PaddlePaddle/PaddleSeg/blob/release/2.3/docs/model_export.md#>`_.
   * - BERT
     - language representation
     -  Models are exported from `PaddleNLP <https://github.com/PaddlePaddle/PaddleNLP/tree/v2.1.1>`_. Refer to `README.md <https://github.com/PaddlePaddle/PaddleNLP/tree/develop/examples/language_model/bert#readme>`_.

Frequently Asked Questions (FAQ)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When Model Optimizer is unable to run to completion due to typographical errors, incorrectly used options, or other issues, it provides explanatory messages. They describe the potential cause of the problem and give a link to the :ref:`Model Optimizer FAQ <doxid-openvino_docs__m_o__d_g_prepare_model__model__optimizer__f_a_q>`, which provides instructions on how to resolve most issues. The FAQ also includes links to relevant sections in the Model Optimizer Developer Guide to help you understand what went wrong.

See Also
~~~~~~~~

:ref:`Model Conversion Tutorials <doxid-openvino_docs__m_o__d_g_prepare_model_convert_model_tutorials>`

