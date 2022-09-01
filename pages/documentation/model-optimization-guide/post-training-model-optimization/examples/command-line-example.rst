.. index:: pair: page; End-to-end Command-line Interface Example
.. _pot_cli_example:

.. meta::
   :description: The example of post-training quantization with DefaultQuantization 
                 algorithm for a MobileNet v2 model from Pytorch framework and 
                 running performance benchmark.
   :keywords: Post-training Optimization Tool, Post-training Optimization Tool Command-Line Interface,
              POT, POT CLI, DefaultQuantization, default quantization, quantizing models, 
              OpenVINO IR, OpenVINO Intermediate Representation, IR, Pytorch, Pytorch 
              framework, benchmark_app, performance benchmark, converting model, 
              Model Downloader, Open Model Zoo, accuracy checker, full-precision model,
              post-training quantization, Model Converter


Command-line Interface Example
==============================

:target:`pot_cli_example_1md_openvino_tools_pot_docs_e2eexample` 

This tutorial describes an example of running post-training quantization for 
**MobileNet v2 model from PyTorch** framework, particularly by the 
DefaultQuantization algorithm. The example covers the following steps:

* Environment setup

* Model preparation and converting it to the OpenVINO™ Intermediate 
  Representation (IR) format

* Performance benchmarking of the original full-precision model

* Dataset preparation

* Accuracy validation of the full-precision model in the IR format

* Model quantization by the DefaultQuantization algorithm and accuracy 
  validation of the quantized model

* Performance benchmarking of the quantized model

All the steps are based on the tools and samples of configuration files 
distributed with the Intel Distribution of OpenVINO toolkit.

The example has been verified in Ubuntu 18.04 Operating System with 
Python 3.6 installed.

In case of issues while running the example, refer to 
:ref:`POT Frequently Asked Questions <pot_faq>` 
for help.

Model Preparation
~~~~~~~~~~~~~~~~~

#. Navigate to ``<EXAMPLE_DIR>``.

#. Download the MobileNet v2 PyTorch model using `Model Downloader <https://github.com/openvinotoolkit/open_model_zoo/blob/master/tools/model_tools/README.md>`__ 
   tool from the Open Model Zoo repository:

   .. ref-code-block:: cpp

      omz_downloader --name mobilenet-v2-pytorch

   After that the original full-precision model is located in 
   ``<EXAMPLE_DIR>/public/mobilenet-v2-pytorch/``.

#. Convert the model to the OpenVINO™ Intermediate Representation (IR) format 
   using `Model Converter <https://github.com/openvinotoolkit/open_model_zoo/blob/master/tools/model_tools/README.md#model-converter-usage>`__ 
   tool:

   .. ref-code-block:: cpp

      omz_converter --name mobilenet-v2-pytorch

   After that the full-precision model in the IR format is located in 
   ``<EXAMPLE_DIR>/public/mobilenet-v2-pytorch/FP32/``.

For more information about the Model Optimizer, refer to its 
:ref:`documentation <doxid-openvino_docs__m_o__d_g__deep__learning__model__optimizer__dev_guide>`.

Performance Benchmarking of Full-Precision Models
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Check the performance of the full-precision model in the IR format using 
:ref:`Deep Learning Benchmark <doxid-openvino_inference_engine_tools_benchmark_tool__r_e_a_d_m_e>` 
tool:

.. ref-code-block:: cpp

   benchmark_app -m <EXAMPLE_DIR>/public/mobilenet-v2-pytorch/FP32/mobilenet-v2-pytorch.xml

Note that the results might be different dependently on characteristics of 
your machine. On a machine with Intel Core i9-10920X CPU @ 3.50GHz it is like:

.. ref-code-block:: cpp

   Latency:    4.14 ms
   Throughput: 1436.55 FPS

Dataset Preparation
~~~~~~~~~~~~~~~~~~~

To perform the accuracy validation as well as quantization of a model, the 
dataset should be prepared. This example uses a real dataset called ImageNet.

To download images:

#. Go to the `ImageNet <http://www.image-net.org/>`__ homepage.

#. If you do not have an account, click the ``Signup`` button in the right 
   upper corner, provide your data, and wait for a confirmation email.

#. Log in after receiving the confirmation email or if you already have an 
   account. Go to the ``Download`` tab.

#. Select ``Download Original Images``.

#. You will be redirected to the ``Terms of Access`` page. If you agree to the 
   Terms, continue by clicking ``Agree and Sign``.

#. Click one of the links in the ``Download as one tar file`` section.

#. Unpack the downloaded archive into ``<EXAMPLE_DIR>/ImageNet/``.

Note that the registration process might be quite long.

Note that the ImageNet size is 50 000 images and takes around 6.5 GB of 
the disk space.

To download the annotation file:

#. Download `archive <http://dl.caffe.berkeleyvision.org/caffe_ilsvrc12.tar.gz>`__.

#. Unpack ``val.txt`` from the archive into ``<EXAMPLE_DIR>/ImageNet/``.

After that the ``<EXAMPLE_DIR>/ImageNet/`` dataset folder should have a lot of 
image files like ``ILSVRC2012_val_00000001.JPEG`` and the ``val.txt`` annotation file.

Accuracy Validation of Full-Precision Model in IR Format
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. Create a new file in ``<EXAMPLE_DIR>`` and name it ``mobilenet_v2_pytorch.yaml``. 
   This is the Accuracy Checker configuration file.

#. Put the following text into ``mobilenet_v2_pytorch.yaml`` :

   .. ref-code-block:: cpp

      models:
        - name: mobilenet-v2-pytorch

          launchers:
            - framework: dlsdk
              device: CPU
              adapter: classification

          datasets:
            - name: classification_dataset
              data_source: ./ImageNet
              annotation_conversion:
                converter: imagenet
                annotation_file: ./ImageNet/val.txt
              reader: pillow_imread

              preprocessing:
                - type: resize
                  size: 256
                  aspect_ratio_scale: greater
                  use_pillow: True
                - type: crop
                  size: 224
                  use_pillow: True
                - type: bgr_to_rgb

              metrics:
                - name: accuracy@top1
                  type: accuracy
                  top_k: 1

                - name: accuracy@top5
                  type: accuracy
                  top_k: 5

   where ``data_source: ./ImageNet`` is the dataset and 
   ``annotation_file: ./ImageNet/val.txt`` is the annotation file prepared on 
   the previous step. For more information about the Accuracy Checker 
   configuration file refer to Accuracy Checker Tool documentation.

#. Evaluate the accuracy of the full-precision model in the IR format by 
   executing the following command in ``<EXAMPLE_DIR>`` :

   .. ref-code-block:: cpp

      accuracy_check -c mobilenet_v2_pytorch.yaml -m ./public/mobilenet-v2-pytorch/FP32/

   The actual result should be like **71.81** % of the accuracy top-1 metric on VNNI based CPU.

   Note that the results might be different on CPUs with different instruction sets.

Model Quantization
~~~~~~~~~~~~~~~~~~

#. Create a new file in ``<EXAMPLE_DIR>`` and name it 
   ``mobilenet_v2_pytorch_int8.json``. This is the POT configuration file.

#. Put the following text into ``mobilenet_v2_pytorch_int8.json`` :

   .. ref-code-block:: cpp

      {
          "model": {
              "model_name": "mobilenet-v2-pytorch",
              "model": "./public/mobilenet-v2-pytorch/FP32/mobilenet-v2-pytorch.xml",
              "weights": "./public/mobilenet-v2-pytorch/FP32/mobilenet-v2-pytorch.bin"
          },
          "engine": {
              "config": "./mobilenet_v2_pytorch.yaml"
          },
          "compression": {
              "algorithms": [
                  {
                      "name": "DefaultQuantization",
                      "params": {
                          "preset": "mixed",
                          "stat_subset_size": 300
                      }
                  }
              ]
          }
      }

   where ``"model": "./public/mobilenet-v2-pytorch/FP32/mobilenet-v2-pytorch.xml"`` 
   and ``"weights": "./public/mobilenet-v2-pytorch/FP32/mobilenet-v2-pytorch.bin"`` 
   specify the full-precision model in the IR format, ``"config": "./mobilenet_v2_pytorch.yaml"`` 
   is the Accuracy Checker configuration file, and ``"name": "DefaultQuantization"`` 
   is the algorithm name.

#. Perform model quantization by executing the following command in ``<EXAMPLE_DIR>``:

   .. ref-code-block:: cpp

      pot -c mobilenet_v2_pytorch_int8.json -e

   The quantized model is placed into the subfolder with your current date and 
   time in the name under the ``./results/mobilenetv2_DefaultQuantization/`` 
   directory. The accuracy validation of the quantized model is performed right 
   after the quantization. The actual result should be like **71.556** % of 
   the accuracy top-1 metric on VNNI based CPU.

   Note that the results might be different on CPUs with different instruction sets.

Performance Benchmarking of Quantized Model
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Check the performance of the quantized model using 
:ref:`Deep Learning Benchmark <doxid-openvino_inference_engine_tools_benchmark_tool__r_e_a_d_m_e>` 
tool:

.. ref-code-block:: cpp

   benchmark_app -m <INT8_MODEL>

where ``<INT8_MODEL>`` is the path to the quantized model.

Note that the results might be different dependently on characteristics of your 
machine. On a machine with Intel Core i9-10920X CPU @ 3.50GHz it is like:

.. ref-code-block:: cpp

   Latency:    1.54 ms
   Throughput: 3814.18 FPS
