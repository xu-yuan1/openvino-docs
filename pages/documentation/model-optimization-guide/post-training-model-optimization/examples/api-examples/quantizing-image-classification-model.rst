.. index:: pair: page; Quantizing Image Classification Model
.. _optim_perf__pot_api_example_classification:

.. meta::
   :description: The example demonstrates how to use Post-training Optimization 
                 Tool API to quantize MobilenetV2 image classification model 
                 from Tensorflow framework.
   :keywords: Post-training Optimization Tool, Post-training Optimization Tool API,
              POT, POT API, quantizing models, post-training quantization, Model Downloader,
              Open Model Zoo, Model Converter, omz_converter, omz_downloader, 
              OpenVINO IR, OpenVINO Intermediate Representation, converting models,
              image classification, image classification model, MobileNetV2, Tensorflow,
              ImageNet

Quantizing Image Classification Model
=====================================

:target:`optim_perf__pot_api_example_classification_1md_openvino_tools_pot_openvino_tools_pot_api_samples_classification_readme` 

This example demonstrates the use of the 
:ref:`Post-training Optimization Tool API <optim_perf__pot_api>` 
for the task of quantizing a classification model. The 
`MobilenetV2 <https://github.com/openvinotoolkit/open_model_zoo/blob/master/models/public/mobilenet-v2-1.0-224/mobilenet-v2-1.0-224.md>`__ 
model from TensorFlow is used for this purpose. A custom ``DataLoader`` is 
created to load the `ImageNet <http://www.image-net.org/>`__ classification 
dataset and the implementation of Accuracy at top-1 metric is used for the 
model evaluation. The code of the example is available on 
`GitHub <https://github.com/openvinotoolkit/openvino/tree/master/tools/pot/openvino/tools/pot/api/samples/classification>`__.

How to prepare the data
~~~~~~~~~~~~~~~~~~~~~~~

To run this example, you need to `download <http://www.image-net.org/download-faq>`__ 
the validation part of the ImageNet image database and place it in a separate 
folder, which will be later referred as ``<IMAGES_DIR>``. Annotations to images 
should be stored in a separate .txt file (``<IMAGENET_ANNOTATION_FILE>``) in 
the ``image_name label`` format.

How to Run the example
~~~~~~~~~~~~~~~~~~~~~~

#. Launch `Model Downloader <https://github.com/openvinotoolkit/open_model_zoo/blob/master/tools/model_tools/README.md>`__ 
   tool to download ``mobilenet-v2-1.0-224`` model from the Open Model Zoo repository.

   .. ref-code-block:: cpp

      omz_downloader --name mobilenet-v2-1.0-224

#. Launch `Model Converter <https://github.com/openvinotoolkit/open_model_zoo/blob/master/tools/model_tools/README.md#model-converter-usage>`__ 
   tool to generate Intermediate Representation (IR) files for the model:

   .. ref-code-block:: cpp

      omz_converter --name mobilenet-v2-1.0-224 --mo <PATH_TO_MODEL_OPTIMIZER>/mo.py

#. Launch the example script from the example directory:

   .. ref-code-block:: cpp

      python3 ./classification_example.py -m <PATH_TO_IR_XML> -a <IMAGENET_ANNOTATION_FILE> -d <IMAGES_DIR>

   Optional: you can specify .bin file of IR directly using the 
   ``-w``, ``--weights`` options.
