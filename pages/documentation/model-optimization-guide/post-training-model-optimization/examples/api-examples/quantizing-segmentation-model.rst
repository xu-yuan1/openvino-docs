.. index:: pair: page; Quantizing Semantic Segmentation Model
.. _optim_perf__pot_api_example_segment:

.. meta::
   :description: The example demonstrates how to use Post-training Optimization 
                 Tool API to quantize a DeepLabV3 segmentation model 
                 from Tensorflow framework.
   :keywords: Post-training Optimization Tool, Post-training Optimization Tool API,
              POT, POT API, quantizing models, post-training quantization, Model Downloader,
              Open Model Zoo, Model Converter, omz_converter, omz_downloader, 
              OpenVINO IR, OpenVINO Intermediate Representation, converting models,
              segmentation, segmentation model, DeepLabV3, Tensorflow, Pascal VOC 2012


Quantizing Semantic Segmentation Model
======================================

:target:`optim_perf__pot_api_example_segment_1md_openvino_tools_pot_openvino_tools_pot_api_samples_segmentation_readme` 

This example demonstrates the use of the 
:ref:`Post-training Optimization Tool API <optim_perf__pot_api>` 
for the task of quantizing a segmentation model. The 
`DeepLabV3 <https://github.com/openvinotoolkit/open_model_zoo/blob/master/models/public/deeplabv3/deeplabv3.md>`__ 
model from TensorFlow is used for this purpose. A custom ``DataLoader`` is 
created to load the `Pascal VOC 2012 <http://host.robots.ox.ac.uk/pascal/VOC/voc2012/>`__ 
dataset for semantic segmentation task and the implementation of Mean 
Intersection Over Union metric is used for the model evaluation. The code of 
the example is available on 
`GitHub <https://github.com/openvinotoolkit/openvino/tree/master/tools/pot/openvino/tools/pot/api/samples/segmentation>`__.

How to prepare the data
~~~~~~~~~~~~~~~~~~~~~~~

To run this example, you will need to download the validation part of the 
Pascal VOC 2012 image database `http://host.robots.ox.ac.uk/pascal/VOC/voc2012/#data <http://host.robots.ox.ac.uk/pascal/VOC/voc2012/#data>`__. 
Images are placed in the ``JPEGImages`` folder, ImageSet file with the list of 
image names for the segmentation task can be found at 
``ImageSets/Segmentation/val.txt`` and segmentation masks are kept in the 
``SegmentationClass`` directory.

How to Run the example
~~~~~~~~~~~~~~~~~~~~~~

#. Launch `Model Downloader <https://github.com/openvinotoolkit/open_model_zoo/blob/master/tools/model_tools/README.md>`__ 
   tool to download ``deeplabv3`` model from the Open Model Zoo repository.

   .. ref-code-block:: cpp

      omz_downloader --name deeplabv3

#. Launch `Model Converter <https://github.com/openvinotoolkit/open_model_zoo/blob/master/tools/model_tools/README.md#model-converter-usage>`__ 
   tool to generate Intermediate Representation (IR) files for the model:

   .. ref-code-block:: cpp

      omz_converter --name deeplabv3 --mo <PATH_TO_MODEL_OPTIMIZER>/mo.py

#. Launch the example script from the example directory:

   .. ref-code-block:: cpp

      python3 ./segmentation_example.py -m <PATH_TO_IR_XML> -d <VOCdevkit/VOC2012/JPEGImages> --imageset-file <VOCdevkit/VOC2012/ImageSets/Segmentation/val.txt> --mask-dir <VOCdevkit/VOC2012/SegmentationClass>

   Optional: you can specify .bin file of IR directly using the 
   ``-w``, ``--weights`` options.
