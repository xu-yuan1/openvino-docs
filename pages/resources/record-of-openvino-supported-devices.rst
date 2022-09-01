.. index:: pair: page; Supported Devices
.. _doxid-openvino_docs__o_v__u_g_supported_plugins__supported__devices:


Supported Devices
=================

:target:`doxid-openvino_docs__o_v__u_g_supported_plugins__supported__devices_1md_openvino_docs_ov_runtime_ug_supported_plugins_supported_devices`

The OpenVINO Runtime can infer models in different formats with various input and output formats. This section provides supported and optimal configurations per device. In OpenVINO™ documentation, "device" refers to an Intel® processors used for inference, which can be a supported CPU, GPU, VPU (vision processing unit), or GNA (Gaussian neural accelerator coprocessor), or a combination of those devices.

.. note:: With OpenVINO™ 2020.4 release, Intel® Movidius™ Neural Compute Stick is no longer supported.



The OpenVINO Runtime provides unique capabilities to infer deep learning models on the following device types with corresponding plugins:

.. list-table::
    :header-rows: 1

    * - Plugin
      - Device types
    * - :ref:`GPU plugin <deploy_infer__gpu_device>`
      - Intel Processor Graphics, including Intel HD Graphics and Intel Iris Graphics
    * - :ref:`CPU plugin <deploy_infer__cpu_device>`
      - Intel Xeon with Intel® Advanced Vector Extensions 2 (Intel® AVX2), Intel® Advanced Vector Extensions 512 (Intel® AVX-512), and AVX512_BF16, Intel Core Processors with Intel AVX2, Intel Atom Processors with Intel® Streaming SIMD Extensions (Intel® SSE)
    * - :ref:`VPU plugins <deploy_infer__vpu_device>` (available in the Intel® Distribution of OpenVINO™ toolkit)
      - Intel® Neural Compute Stick 2 powered by the Intel® Movidius™ Myriad™ X, Intel® Vision Accelerator Design with Intel® Movidius™ VPUs
    * - :ref:`GNA plugin <deploy_infer__gna_device>` (available in the Intel® Distribution of OpenVINO™ toolkit)
      - Intel Speech Enabling Developer Kit, Amazon Alexa\* Premium Far-Field Developer Kit, Intel Pentium Silver J5005 Processor, Intel Pentium Silver N5000 Processor, Intel Celeron J4005 Processor, Intel Celeron J4105 Processor, Intel Celeron Processor N4100, Intel Celeron Processor N4000, Intel Core i3-8121U Processor, Intel Core i7-1065G7 Processor, Intel Core i7-1060G7 Processor, Intel Core i5-1035G4 Processor, Intel Core i5-1035G7 Processor, Intel Core i5-1035G1 Processor, Intel Core i5-1030G7 Processor, Intel Core i5-1030G4 Processor, Intel Core i3-1005G1 Processor, Intel Core i3-1000G1 Processor, Intel Core i3-1000G4 Processor
    * - :ref:`Arm® CPU plugin <deploy_infer__arm_cpu_device>` (unavailable in the Intel® Distribution of OpenVINO™ toolkit)
      - Raspberry Pi™ 4 Model B, Apple® Mac mini with M1 chip, NVIDIA® Jetson Nano™, Android™ devices
    * - :ref:`Multi-Device execution <deploy_infer__multi_plugin>`
      - Multi-Device execution enables simultaneous inference of the same model on several devices in parallel
    * - :ref:`Auto-Device plugin <deploy_infer__auto_plugin>`
      - Auto-Device plugin enables selecting Intel device for inference automatically
    * - :ref:`Heterogeneous plugin <deploy_infer__hetero_plugin>`
      - Heterogeneous execution enables automatic inference splitting between several devices (for example if a device doesn't `support certain operation <#supported-layers>`__ ).

Devices similar to the ones we have used for benchmarking can be accessed using `Intel® DevCloud for the Edge <https://devcloud.intel.com/edge/>`__, a remote development environment with access to Intel® hardware and the latest versions of the Intel® Distribution of the OpenVINO™ Toolkit. `Learn more <https://devcloud.intel.com/edge/get_started/devcloud/>`__ or `Register here <https://inteliot.force.com/DevcloudForEdge/s/>`__.

Supported Configurations
~~~~~~~~~~~~~~~~~~~~~~~~

The OpenVINO Runtime can inference models in different formats with various input and output formats. This page shows supported and optimal configurations for each plugin.

Terminology
-----------

.. list-table::
    :header-rows: 1

    * - Acronym/Term
      - Description
    * - FP32 format
      - Single-precision floating-point format
    * - BF16 format
      - Brain floating-point format
    * - FP16 format
      - Half-precision floating-point format
    * - I16 format
      - 2-byte signed integer format
    * - I8 format
      - 1-byte signed integer format
    * - U16 format
      - 2-byte unsigned integer format
    * - U8 format
      - 1-byte unsigned integer format

NHWC, NCHW, and NCDHW refer to the data ordering in batches of images:

* NHWC and NCHW refer to image data layout.

* NCDHW refers to image sequence data layout.

Abbreviations in the support tables are as follows:

* N: Number of images in a batch

* D: Depth. Depend on model it could be spatial or time dimension

* H: Number of pixels in the vertical dimension

* W: Number of pixels in the horizontal dimension

* C: Number of channels

CHW, NC, C - Tensor memory layout. For example, the CHW value at index (c,h,w) is physically located at index (c\*H+h)\*W+w, for others by analogy.

Supported Model Formats
-----------------------

.. list-table::
    :header-rows: 1

    * - Plugin
      - FP32
      - FP16
      - I8
    * - CPU plugin
      - Supported and preferred
      - Supported
      - Supported
    * - GPU plugin
      - Supported
      - Supported and preferred
      - Supported
    * - VPU plugins
      - Not supported
      - Supported
      - Not supported
    * - GNA plugin
      - Supported
      - Supported
      - Not supported
    * - Arm® CPU plugin
      - Supported and preferred
      - Supported
      - Supported (partially)

For :ref:`Multi-Device <deploy_infer__multi_plugin>` and :ref:`Heterogeneous <deploy_infer__hetero_plugin>` executions the supported models formats depends on the actual underlying devices. *Generally, FP16 is preferable as it is most ubiquitous and performant*.

Supported Input Precision
-------------------------

.. list-table::
    :header-rows: 1

    * - Plugin
      - FP32
      - FP16
      - U8
      - U16
      - I8
      - I16
    * - CPU plugin
      - Supported
      - Not supported
      - Supported
      - Supported
      - Not supported
      - Supported
    * - GPU plugin
      - Supported
      - Supported\*
      - Supported\*
      - Supported\*
      - Not supported
      - Supported\*
    * - VPU plugins
      - Supported
      - Supported
      - Supported
      - Not supported
      - Not supported
      - Not supported
    * - GNA plugin
      - Supported
      - Not supported
      - Supported
      - Not supported
      - Supported
      - Supported
    * - Arm® CPU plugin
      - Supported
      - Supported
      - Supported
      - Supported
      - Not supported
      - Not supported

\* - Supported via ``SetBlob`` only, ``GetBlob`` returns FP32

For :ref:`Multi-Device <deploy_infer__multi_plugin>` and :ref:`Heterogeneous <deploy_infer__hetero_plugin>` executions the supported input precision depends on the actual underlying devices. *Generally, U8 is preferable as it is most ubiquitous*.

Supported Output Precision
--------------------------

.. list-table::
    :header-rows: 1

    * - Plugin
      - FP32
      - FP16
    * - CPU plugin
      - Supported
      - Not supported
    * - GPU plugin
      - Supported
      - Supported
    * - VPU plugins
      - Supported
      - Supported
    * - GNA plugin
      - Supported
      - Not supported
    * - Arm® CPU plugin
      - Supported
      - Supported

For :ref:`Multi-Device <deploy_infer__multi_plugin>` and :ref:`Heterogeneous <deploy_infer__hetero_plugin>` executions the supported output precision depends on the actual underlying devices. *Generally, FP32 is preferable as it is most ubiquitous*.

Supported Input Layout
----------------------

.. list-table::
    :header-rows: 1

    * - Plugin
      - NCDHW
      - NCHW
      - NHWC
      - NC
    * - CPU plugin
      - Supported
      - Supported
      - Supported
      - Supported
    * - GPU plugin
      - Supported
      - Supported
      - Supported
      - Supported
    * - VPU plugins
      - Supported
      - Supported
      - Supported
      - Supported
    * - GNA plugin
      - Not supported
      - Supported
      - Supported
      - Supported
    * - Arm® CPU plugin
      - Not supported
      - Supported
      - Supported
      - Supported

Supported Output Layout
-----------------------

.. list-table::
    :header-rows: 1

    * - Number of dimensions
      - 5
      - 4
      - 3
      - 2
      - 1
    * - Layout
      - NCDHW
      - NCHW
      - CHW
      - NC
      - C

For setting relevant configuration, refer to the :ref:`Integrate with Customer Application <deploy_infer__integrate_application>` topic (step 3 "Configure input and output").

Supported Layers
----------------

The following layers are supported by the plugins:

.. list-table::
    :header-rows: 1

    * - Layers
      - GPU
      - CPU
      - VPU
      - GNA
      - Arm® CPU
    * - Abs
      - Supported
      - Supported\*\*
      - Supported
      - Not Supported
      - Supported
    * - Acos
      - Supported
      - Supported\*\*
      - Not Supported
      - Not Supported
      - Supported\*\*\*\*
    * - Acosh
      - Supported
      - Supported\*\*
      - Not Supported
      - Not Supported
      - Supported\*\*\*\*
    * - Activation-Clamp
      - Supported
      - Supported\*\*\*
      - Supported
      - Supported
      - Supported
    * - Activation-ELU
      - Supported
      - Supported\*\*\*
      - Supported
      - Not Supported
      - Supported
    * - Activation-Exp
      - Supported
      - Supported\*\*\*
      - Supported
      - Supported
      - Supported
    * - Activation-Leaky ReLU
      - Supported
      - Supported\*\*\*
      - Supported
      - Supported
      - Not Supported
    * - Activation-Not
      - Supported
      - Supported\*\*\*
      - Supported
      - Not Supported
      - Not Supported
    * - Activation-PReLU
      - Supported
      - Supported\*\*\*
      - Supported
      - Not Supported
      - Supported
    * - Activation-ReLU
      - Supported
      - Supported\*\*\*
      - Supported
      - Supported
      - Supported
    * - Activation-ReLU6
      - Supported
      - Supported\*\*\*
      - Supported
      - Not Supported
      - Not Supported
    * - Activation-Sigmoid/Logistic
      - Supported
      - Supported\*\*\*
      - Supported
      - Supported
      - Supported
    * - Activation-TanH
      - Supported
      - Supported\*\*\*
      - Supported
      - Supported
      - Supported
    * - ArgMax
      - Supported
      - Supported\*\*
      - Supported
      - Not Supported
      - Not Supported
    * - Asin
      - Supported
      - Supported\*\*
      - Not Supported
      - Not Supported
      - Supported\*\*\*\*
    * - Asinh
      - Supported
      - Supported\*\*
      - Not Supported
      - Not Supported
      - Supported\*\*\*\*
    * - Atan
      - Supported
      - Supported\*\*
      - Not Supported
      - Not Supported
      - Supported\*\*\*\*
    * - Atanh
      - Supported
      - Supported\*\*
      - Not Supported
      - Not Supported
      - Supported\*\*\*\*
    * - BatchNormalization
      - Supported
      - Supported
      - Supported
      - Not Supported
      - Supported
    * - BinaryConvolution
      - Supported
      - Supported
      - Not Supported
      - Not Supported
      - Not Supported
    * - Broadcast
      - Supported
      - Supported\*\*
      - Supported
      - Not Supported
      - Supported
    * - Ceil
      - Supported
      - Supported\*\*
      - Supported
      - Not Supported
      - Supported
    * - Concat
      - Supported
      - Supported\*\*\*
      - Supported
      - Supported
      - Supported
    * - Const
      - Supported
      - Supported
      - Supported
      - Supported
      - Supported
    * - Convolution-Dilated
      - Supported
      - Supported
      - Supported
      - Not Supported
      - Supported
    * - Convolution-Dilated 3D
      - Supported
      - Supported
      - Not Supported
      - Not Supported
      - Not Supported
    * - Convolution-Grouped
      - Supported
      - Supported
      - Supported
      - Not Supported
      - Supported
    * - Convolution-Grouped 3D
      - Supported
      - Supported
      - Not Supported
      - Not Supported
      - Not Supported
    * - Convolution-Ordinary
      - Supported
      - Supported
      - Supported
      - Supported\*
      - Supported
    * - Convolution-Ordinary 3D
      - Supported
      - Supported
      - Not Supported
      - Not Supported
      - Not Supported
    * - Cos
      - Supported
      - Supported\*\*
      - Not Supported
      - Not Supported
      - Supported\*\*\*\*
    * - Cosh
      - Supported
      - Supported\*\*
      - Not Supported
      - Not Supported
      - Supported\*\*\*\*
    * - Crop
      - Supported
      - Supported
      - Supported
      - Supported
      - Not Supported
    * - CTCGreedyDecoder
      - Supported\*\*
      - Supported\*\*
      - Supported\*
      - Not Supported
      - Supported\*\*\*\*
    * - Deconvolution
      - Supported
      - Supported
      - Supported
      - Not Supported
      - Not Supported
    * - Deconvolution 3D
      - Supported
      - Supported
      - Not Supported
      - Not Supported
      - Not Supported
    * - DeformableConvolution
      - Supported
      - Supported
      - Not Supported
      - Not Supported
      - Not Supported
    * - DepthToSpace
      - Supported
      - Supported\*\*
      - Not Supported
      - Not Supported
      - Supported\*
    * - DetectionOutput
      - Supported
      - Supported\*\*
      - Supported\*
      - Not Supported
      - Supported\*\*\*\*
    * - Eltwise-And
      - Supported
      - Supported\*\*\*
      - Supported
      - Not Supported
      - Supported
    * - Eltwise-Add
      - Supported
      - Supported\*\*\*
      - Supported
      - Not Supported
      - Supported
    * - Eltwise-Div
      - Supported
      - Supported\*\*\*
      - Supported
      - Not Supported
      - Supported
    * - Eltwise-Equal
      - Supported
      - Supported\*\*\*
      - Supported
      - Not Supported
      - Supported\*
    * - Eltwise-FloorMod
      - Supported
      - Supported\*\*\*
      - Supported
      - Not Supported
      - Supported\*\*\*\*
    * - Eltwise-Greater
      - Supported
      - Supported\*\*\*
      - Supported
      - Not Supported
      - Supported
    * - Eltwise-GreaterEqual
      - Supported
      - Supported\*\*\*
      - Supported
      - Not Supported
      - Supported
    * - Eltwise-Less
      - Supported
      - Supported\*\*\*
      - Supported
      - Not Supported
      - Supported\*
    * - Eltwise-LessEqual
      - Supported
      - Supported\*\*\*
      - Supported
      - Not Supported
      - Supported\*
    * - Eltwise-LogicalAnd
      - Supported
      - Supported\*\*\*
      - Supported
      - Not Supported
      - Supported
    * - Eltwise-LogicalOr
      - Supported
      - Supported\*\*\*
      - Supported
      - Not Supported
      - Supported
    * - Eltwise-LogicalXor
      - Supported
      - Supported\*\*\*
      - Supported
      - Not Supported
      - Supported
    * - Eltwise-Max
      - Supported
      - Supported\*\*\*
      - Supported
      - Not Supported
      - Supported
    * - Eltwise-Min
      - Supported
      - Supported\*\*\*
      - Supported
      - Not Supported
      - Supported
    * - Eltwise-Mul
      - Supported
      - Supported\*\*\*
      - Supported
      - Supported
      - Supported
    * - Eltwise-NotEqual
      - Supported
      - Supported\*\*\*
      - Supported
      - Not Supported
      - Supported\*
    * - Eltwise-Pow
      - Supported
      - Supported\*\*\*
      - Supported
      - Not Supported
      - Supported
    * - Eltwise-Prod
      - Supported
      - Supported\*\*\*
      - Supported
      - Supported
      - Not Supported
    * - Eltwise-SquaredDiff
      - Supported
      - Supported\*\*\*
      - Supported
      - Not Supported
      - Supported
    * - Eltwise-Sub
      - Supported
      - Supported\*\*\*
      - Supported
      - Supported
      - Supported
    * - Eltwise-Sum
      - Supported
      - Supported\*\*\*
      - Supported
      - Supported
      - Supported\*\*\*\*
    * - Erf
      - Supported
      - Supported\*\*
      - Supported
      - Not Supported
      - Supported\*\*\*\*
    * - Exp
      - Supported
      - Supported
      - Supported
      - Supported
      - Supported
    * - FakeQuantize
      - Not Supported
      - Supported
      - Not Supported
      - Not Supported
      - Supported\*
    * - Fill
      - Not Supported
      - Supported\*\*
      - Not Supported
      - Not Supported
      - Not Supported
    * - Flatten
      - Supported
      - Supported
      - Supported
      - Not Supported
      - Not Supported
    * - Floor
      - Supported
      - Supported\*\*
      - Supported
      - Not Supported
      - Supported
    * - FullyConnected (Inner Product)
      - Supported
      - Supported\*\*\*
      - Supported
      - Supported
      - Supported
    * - Gather
      - Supported
      - Supported\*\*
      - Supported
      - Not Supported
      - Supported\*
    * - GatherTree
      - Not Supported
      - Supported\*\*
      - Not Supported
      - Not Supported
      - Supported\*\*\*\*
    * - Gemm
      - Supported
      - Supported
      - Supported
      - Not Supported
      - Not Supported
    * - GRN
      - Supported\*\*
      - Supported\*\*
      - Supported
      - Not Supported
      - Supported
    * - HardSigmoid
      - Supported
      - Supported\*\*
      - Not Supported
      - Not Supported
      - Supported\*\*\*\*
    * - Interp
      - Supported\*\*
      - Supported\*\*
      - Supported
      - Not Supported
      - Supported\*
    * - Log
      - Supported
      - Supported\*\*
      - Supported
      - Supported
      - Supported
    * - LRN (Norm)
      - Supported
      - Supported
      - Supported
      - Not Supported
      - Supported\*
    * - LSTMCell
      - Supported
      - Supported
      - Supported
      - Supported
      - Supported
    * - GRUCell
      - Supported
      - Supported
      - Not Supported
      - Not Supported
      - Supported
    * - RNNCell
      - Supported
      - Supported
      - Not Supported
      - Not Supported
      - Supported
    * - LSTMSequence
      - Supported
      - Supported
      - Supported
      - Not Supported
      - Supported\*\*\*\*
    * - GRUSequence
      - Supported
      - Supported
      - Not Supported
      - Not Supported
      - Supported\*\*\*\*
    * - RNNSequence
      - Supported
      - Supported
      - Not Supported
      - Not Supported
      - Supported\*\*\*\*
    * - LogSoftmax
      - Supported
      - Supported\*\*
      - Not Supported
      - Not Supported
      - Supported
    * - Memory
      - Not Supported
      - Supported
      - Not Supported
      - Supported
      - Not Supported
    * - MVN
      - Supported
      - Supported\*\*
      - Supported\*
      - Not Supported
      - Supported\*
    * - Neg
      - Supported
      - Supported\*\*
      - Not Supported
      - Not Supported
      - Supported
    * - NonMaxSuppression
      - Not Supported
      - Supported\*\*
      - Supported
      - Not Supported
      - Supported\*\*\*\*
    * - Normalize
      - Supported
      - Supported\*\*
      - Supported\*
      - Not Supported
      - Supported\*
    * - OneHot
      - Supported
      - Supported\*\*
      - Supported
      - Not Supported
      - Supported\*\*\*\*
    * - Pad
      - Supported
      - Supported\*\*
      - Supported\*
      - Not Supported
      - Supported\*
    * - Permute
      - Supported
      - Supported
      - Supported
      - Supported\*
      - Not Supported
    * - Pooling(AVG,MAX)
      - Supported
      - Supported
      - Supported
      - Supported
      - Supported
    * - Pooling(AVG,MAX) 3D
      - Supported
      - Supported
      - Not Supported
      - Not Supported
      - Supported\*
    * - Power
      - Supported
      - Supported\*\*
      - Supported
      - Supported\*
      - Supported
    * - PowerFile
      - Not Supported
      - Supported\*\*
      - Not Supported
      - Not Supported
      - Not Supported
    * - PriorBox
      - Supported
      - Supported\*\*
      - Supported
      - Not Supported
      - Supported
    * - PriorBoxClustered
      - Supported\*\*
      - Supported\*\*
      - Supported
      - Not Supported
      - Supported
    * - Proposal
      - Supported
      - Supported\*\*
      - Supported
      - Not Supported
      - Supported\*\*\*\*
    * - PSROIPooling
      - Supported
      - Supported\*\*
      - Supported
      - Not Supported
      - Supported\*\*\*\*
    * - Range
      - Not Supported
      - Supported\*\*
      - Not Supported
      - Not Supported
      - Not Supported
    * - Reciprocal
      - Supported
      - Supported\*\*
      - Not Supported
      - Not Supported
      - Not Supported
    * - ReduceAnd
      - Supported
      - Supported\*\*
      - Supported
      - Not Supported
      - Supported\*\*\*\*
    * - ReduceL1
      - Supported
      - Supported\*\*
      - Not Supported
      - Not Supported
      - Supported
    * - ReduceL2
      - Supported
      - Supported\*\*
      - Not Supported
      - Not Supported
      - Supported
    * - ReduceLogSum
      - Supported
      - Supported\*\*
      - Not Supported
      - Not Supported
      - Supported
    * - ReduceLogSumExp
      - Supported
      - Supported\*\*
      - Not Supported
      - Not Supported
      - Not Supported
    * - ReduceMax
      - Supported
      - Supported\*\*
      - Supported
      - Not Supported
      - Supported
    * - ReduceMean
      - Supported
      - Supported\*\*
      - Supported
      - Not Supported
      - Supported
    * - ReduceMin
      - Supported
      - Supported\*\*
      - Supported
      - Not Supported
      - Supported
    * - ReduceOr
      - Supported
      - Supported\*\*
      - Not Supported
      - Not Supported
      - Supported\*\*\*\*
    * - ReduceProd
      - Supported
      - Supported\*\*
      - Not Supported
      - Not Supported
      - Supported
    * - ReduceSum
      - Supported
      - Supported\*\*
      - Supported
      - Not Supported
      - Supported
    * - ReduceSumSquare
      - Supported
      - Supported\*\*
      - Not Supported
      - Not Supported
      - Not Supported
    * - RegionYolo
      - Supported
      - Supported\*\*
      - Supported
      - Not Supported
      - Supported\*\*\*\*
    * - ReorgYolo
      - Supported
      - Supported\*\*
      - Supported
      - Not Supported
      - Supported
    * - Resample
      - Supported
      - Supported\*\*
      - Supported
      - Not Supported
      - Not Supported
    * - Reshape
      - Supported
      - Supported\*\*\*
      - Supported
      - Supported
      - Supported
    * - ReverseSequence
      - Supported
      - Supported\*\*
      - Supported
      - Not Supported
      - Supported\*\*\*\*
    * - RNN
      - Not Supported
      - Supported
      - Supported
      - Not Supported
      - Supported
    * - ROIPooling
      - Supported\*
      - Supported
      - Supported
      - Not Supported
      - Supported\*\*\*\*
    * - ScaleShift
      - Supported
      - Supported\*\*\*
      - Supported\*
      - Supported
      - Not Supported
    * - ScatterUpdate
      - Not Supported
      - Supported\*\*
      - Supported
      - Not Supported
      - Not Supported
    * - Select
      - Supported
      - Supported
      - Supported
      - Not Supported
      - Supported
    * - Selu
      - Supported
      - Supported\*\*
      - Not Supported
      - Not Supported
      - Supported\*\*\*\*
    * - ShuffleChannels
      - Supported
      - Supported\*\*
      - Not Supported
      - Not Supported
      - Supported
    * - Sign
      - Supported
      - Supported\*\*
      - Supported
      - Not Supported
      - Supported
    * - Sin
      - Supported
      - Supported\*\*
      - Not Supported
      - Not Supported
      - Supported
    * - Sinh
      - Supported
      - Supported\*\*
      - Not Supported
      - Not Supported
      - Supported\*\*\*\*
    * - SimplerNMS
      - Supported
      - Supported\*\*
      - Not Supported
      - Not Supported
      - Not Supported
    * - Slice
      - Supported
      - Supported\*\*\*
      - Supported
      - Supported
      - Not Supported
    * - SoftMax
      - Supported
      - Supported\*\*\*
      - Supported
      - Not Supported
      - Supported
    * - Softplus
      - Supported
      - Supported\*\*
      - Supported
      - Not Supported
      - Supported
    * - Softsign
      - Supported
      - Supported\*\*
      - Not Supported
      - Supported
      - Not Supported
    * - SpaceToDepth
      - Not Supported
      - Supported\*\*
      - Not Supported
      - Not Supported
      - Supported\*
    * - SpatialTransformer
      - Not Supported
      - Supported\*\*
      - Not Supported
      - Not Supported
      - Not Supported
    * - Split
      - Supported
      - Supported\*\*\*
      - Supported
      - Supported
      - Supported
    * - Squeeze
      - Supported
      - Supported\*\*
      - Supported
      - Supported
      - Supported
    * - StridedSlice
      - Supported
      - Supported\*\*
      - Supported
      - Not Supported
      - Supported\*
    * - Tan
      - Supported
      - Supported\*\*
      - Not Supported
      - Not Supported
      - Supported\*\*\*\*
    * - TensorIterator
      - Not Supported
      - Supported
      - Supported
      - Supported
      - Supported
    * - Tile
      - Supported\*\*
      - Supported\*\*\*
      - Supported
      - Not Supported
      - Supported
    * - TopK
      - Supported
      - Supported\*\*
      - Supported
      - Not Supported
      - Supported\*\*\*\*
    * - Unpooling
      - Supported
      - Not Supported
      - Not Supported
      - Not Supported
      - Not Supported
    * - Unsqueeze
      - Supported
      - Supported\*\*
      - Supported
      - Supported
      - Supported
    * - Upsampling
      - Supported
      - Not Supported
      - Not Supported
      - Not Supported
      - Not Supported

\*- support is limited to the specific parameters. Refer to "Known Layers Limitation" section for the device :ref:`from the list of supported <doxid-openvino_docs__o_v__u_g_supported_plugins__supported__devices>`.

\*\*- support is implemented via :ref:`Extensibility mechanism <extensibility__api_introduction>`.

\*\*\*- supports NCDHW layout.

\*\*\*\*- support is implemented via runtime reference.

