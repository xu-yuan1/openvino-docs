.. index:: pair: page; Post-training Optimization Tool API Examples
.. _pot_api_examples:

.. meta::
   :description: The examples demonstrate how to use Post-training Optimization 
                 Tool API to quantize models from different domains.
   :keywords: Post-training Optimization Tool, Post-training Optimization Tool API,
              POT, POT API, quantizing models, post-training quantization,
              3D segmentation model, Brain Tumor Segmentation, Tensorflow,
              Pytorch, Medical Segmentation Decathlon BRATS 2017, segmentation model,
              Kaldi, Caffe, image classification model, object detection model, 
              cascaded model, quantizing cascaded model, quantizing for GNA, GNA,
              OpenVino Intermediate Representation (IR), OpenVINO IR, 
              DefaultQuantization, AccuracyAwareQuantization

POT API Examples
================

:target:`pot_api_examples_1md_openvino_tools_pot_openvino_tools_pot_api_samples_readme`


.. toctree::
   :maxdepth: 1
   :hidden:

   ./api-examples/quantizing-image-classification-model
   ./api-examples/quantizing-with-accuracy-control
   ./api-examples/quantizing-face-detection-model
   ./api-examples/quantizing-segmentation-model
   ./api-examples/quantizing-3d-segmentation-model
   ./api-examples/quantizing-for-gna-device

The Post-training Optimization Tool contains multiple examples that demonstrate 
how to use its :ref:`API <pot_api_reference>` to optimize 
DL models. All available examples can be found on 
`GitHub <https://github.com/openvinotoolkit/openvino/tree/master/tools/pot/openvino/tools/pot/api/samples>`__.

The following examples demonstrate the implementation of ``Engine``, 
``Metric``, and ``DataLoader`` interfaces for various use cases:

#. :ref:`Quantizing Image Classification model <pot_api_example_classification>`

   * Uses single ``MobilenetV2`` model from TensorFlow

   * Implements ``DataLoader`` to load .JPEG images and annotations of 
     Imagenet database

   * Implements ``Metric`` interface to calculate Accuracy at top-1 metric

   * Uses DefaultQuantization algorithm for quantization model

#. :ref:`Quantizing Object Detection Model with Accuracy Control <pot_api_example_accuracy>`

   * Uses single ``MobileNetV1 FPN`` model from TensorFlow

   * Implements ``Dataloader`` to load images of COCO database

   * Implements ``Metric`` interface to calculate mAP@[.5:.95] metric

   * Uses ``AccuracyAwareQuantization`` algorithm for quantization model

#. :ref:`Quantizing Semantic Segmentation Model <pot_api_example_segmentation>`

   * Uses single ``DeepLabV3`` model from TensorFlow

   * Implements ``DataLoader`` to load .JPEG images and annotations of Pascal 
     VOC 2012 database

   * Implements ``Metric`` interface to calculate Mean Intersection Over Union metric

   * Uses DefaultQuantization algorithm for quantization model

#. :ref:`Quantizing 3D Segmentation Model <pot_api_example_3d_segmentation>`

   * Uses single ``Brain Tumor Segmentation`` model from PyTorch

   * Implements ``DataLoader`` to load images in NIfTI format from Medical 
     Segmentation Decathlon BRATS 2017 database

   * Implements ``Metric`` interface to calculate Dice Index metric

   * Demonstrates how to use image metadata obtained during data loading to 
     post-process the raw model output

   * Uses DefaultQuantization algorithm for quantization model

#. :ref:`Quantizing Cascaded model <pot_api_example_face_detection>`

   * Uses cascaded (composite) ``MTCNN`` model from Caffe that consists of 
     three separate models in an OpenVino Intermediate Representation (IR)

   * Implements ``Dataloader`` to load .jpg images of WIDER FACE database

   * Implements ``Metric`` interface to calculate Recall metric

   * Implements ``Engine`` class that is inherited from ``IEEngine`` to 
     create a complex staged pipeline to sequentially execute each of the 
     three stages of the MTCNN model, represented by multiple models in IR. 
     It uses engine helpers to set model in OpenVino Inference Engine and 
     process raw model output for the correct statistics collection

   * Uses DefaultQuantization algorithm for quantization model

#. :ref:`Quantizing for GNA Device <pot_api_example_gna>`

   * Uses models from Kaldi

   * Implements ``DataLoader`` to data in .ark format

   * Uses DefaultQuantization algorithm for quantization model

After execution of each example above the quantized model is placed into the 
folder ``optimized``. The accuracy validation of the quantized model is 
performed right after the quantization.
