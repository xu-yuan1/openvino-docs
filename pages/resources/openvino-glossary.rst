.. index:: pair: page; Glossary
.. _doxid-openvino_docs__o_v__glossary:


Glossary
========

:target:`doxid-openvino_docs__o_v__glossary_1md_openvino_docs_glossary`

Acronyms and Abbreviations
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
    :header-rows: 1

    * - Abbreviation
      - Description
    * - API
      - Application Programming Interface
    * - AVX
      - Advanced Vector Extensions
    * - clDNN
      - Compute Library for Deep Neural Networks
    * - CLI
      - Command Line Interface
    * - CNN
      - Convolutional Neural Network
    * - CPU
      - Central Processing Unit
    * - CV
      - Computer Vision
    * - DL
      - Deep Learning
    * - DLL
      - Dynamic Link Library
    * - DNN
      - Deep Neural Networks
    * - ELU
      - Exponential Linear rectification Unit
    * - FCN
      - Fully Convolutional Network
    * - FP
      - Floating Point
    * - GCC
      - GNU Compiler Collection
    * - GPU
      - Graphics Processing Unit
    * - HD
      - High Definition
    * - IR
      - Intermediate Representation
    * - JIT
      - Just In Time
    * - JTAG
      - Joint Test Action Group
    * - LPR
      - License-Plate Recognition
    * - LRN
      - Local Response Normalization
    * - mAP
      - Mean Average Precision
    * - Intel(R) OneDNN
      - Intel(R) OneAPI Deep Neural Network Library
    * - MO
      - Model Optimizer
    * - MVN
      - Mean Variance Normalization
    * - NCDHW
      - Number of images, Channels, Depth, Height, Width
    * - NCHW
      - Number of images, Channels, Height, Width
    * - NHWC
      - Number of images, Height, Width, Channels
    * - NMS
      - Non-Maximum Suppression
    * - NN
      - Neural Network
    * - NST
      - Neural Style Transfer
    * - OD
      - Object Detection
    * - OS
      - Operating System
    * - PCI
      - Peripheral Component Interconnect
    * - PReLU
      - Parametric Rectified Linear Unit
    * - PSROI
      - Position Sensitive Region Of Interest
    * - RCNN, R-CNN
      - Region-based Convolutional Neural Network
    * - ReLU
      - Rectified Linear Unit
    * - ROI
      - Region Of Interest
    * - SDK
      - Software Development Kit
    * - SSD
      - Single Shot multibox Detector
    * - SSE
      - Streaming SIMD Extensions
    * - USB
      - Universal Serial Bus
    * - VGG
      - Visual Geometry Group
    * - VOC
      - Visual Object Classes
    * - WINAPI
      - Windows Application Programming Interface

Terms
~~~~~

Glossary of terms used in the OpenVINO™

.. list-table::
    :header-rows: 1

    * - Term
      - Description
    * - Batch
      - Number of images to analyze during one call of infer. Maximum batch size is a property of the model and it is set before compiling of the model by the device. In NHWC, NCHW and NCDHW image data layout representation, the N refers to the number of images in the batch
    * - Tensor
      - Memory container used for storing inputs, outputs of the model, weights and biases of the operations
    * - Device (Affinitity)
      - A preferred Intel(R) hardware device to run the inference (CPU, GPU, GNA, etc.)
    * - Extensibility mechanism, Custom layers
      - The mechanism that provides you with capabilities to extend the OpenVINO™ Runtime and Model Optimizer so that they can work with models containing operations that are not yet supported
    * - ``:ref:`ov::Model <doxid-classov_1_1_model>```
      - A class of the Model that OpenVINO™ Runtime reads from IR or converts from ONNX, PaddlePaddle formats. Consists of model structure, weights and biases
    * - ``:ref:`ov::CompiledModel <doxid-classov_1_1_compiled_model>```
      - An instance of the compiled model which allows the OpenVINO™ Runtime to request (several) infer requests and perform inference synchronously or asynchronously
    * - ``:ref:`ov::InferRequest <doxid-classov_1_1_infer_request>```
      - A class that represents the end point of inference on the model compiled by the device and represented by a compiled model. Inputs are set here, outputs should be requested from this interface as well
    * - ``:ref:`ov::ProfilingInfo <doxid-structov_1_1_profiling_info>```
      - Represents basic inference profiling information per operation
    * - OpenVINO™ Runtime
      - A C++ library with a set of classes that you can use in your application to infer input tensors and get the results
    * - OpenVINO™ API
      - The basic default API for all supported devices, which allows you to load a model from Intermediate Representation or convert from ONNX, PaddlePaddle file formars, set input and output formats and execute the model on various devices
    * - OpenVINO™ ``Core``
      - OpenVINO™ Core is a software component that manages inference on certain Intel(R) hardware devices: CPU, GPU, MYRIAD, GNA, etc.
    * - ``:ref:`ov::Layout <doxid-classov_1_1_layout>```
      - Image data layout refers to the representation of images batch. Layout shows a sequence of 4D or 5D tensor data in memory. A typical NCHW format represents pixel in horizontal direction, rows by vertical dimension, planes by channel and images into batch. See also :ref:`Layout API Overview <doxid-openvino_docs__o_v__u_g__layout__overview>`
    * - ``:ref:`ov::element::Type <doxid-classov_1_1element_1_1_type>```
      - Represents data element type. For example, f32 is 32-bit floating point, f16 is 16-bit floating point.

See Also
~~~~~~~~

* :ref:`Available Operations Sets <doxid-openvino_docs_ops_opset>`

* :ref:`Terminology <doxid-openvino_docs__o_v__u_g_supported_plugins__supported__devices>`

