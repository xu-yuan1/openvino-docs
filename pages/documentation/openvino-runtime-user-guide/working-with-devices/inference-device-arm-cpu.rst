.. index:: pair: page; Arm® CPU Device
.. _deploy_infer__arm_cpu_device:

.. meta::
   :description: The Arm® CPU plugin in the Intel® Distribution of OpenVINO™ toolkit 
                 is developed to enable inference of deep neural networks on Arm® CPU,
                 using the Arm Compute Library.
   :keywords: OpenVINO™, OpenVINO plugin, Arm® CPU, Arm CPU plugin, 
              device name, compile_model, inference device, inference, 
              model inference, inference data types, floating-point data type, 
              integer data type, quantized data type, f32, f16, i8, precision conversion, 
              preprocessing operations, u8 to u16, u16 -> u8, u16 -> u32, u8 -> s16, 
              u8 -> s32, s16 to u8, s16 to s32, f16 to f32, color conversion, 
              NV12 to RGB, NV12 to BGR, i420 to RGB, i420 to BGR, OpenVINO™ ecosystem, 
              internal primitives, preprocessing acceleration

Arm® CPU Device
================

:target:`deploy_infer__arm_cpu_device_1md_openvino_docs_ov_runtime_ug_supported_plugins_arm_cpu`

Introducing the Arm® CPU Plugin
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The Arm® CPU plugin is developed in order to enable deep neural networks 
inference on Arm® CPU, using `Compute Library <https://github.com/ARM-software/ComputeLibrary>`__ 
as a backend.

.. note:: This is a community-level add-on to OpenVINO™. Intel® welcomes 
   community participation in the OpenVINO™ ecosystem, technical questions and 
   code contributions on community forums. However, this component has not 
   undergone full release validation or qualification from Intel®, hence no 
   official support is offered.


The Arm® CPU plugin is not a part of the Intel® Distribution of OpenVINO™ 
toolkit and is not distributed in the pre-built form. The plugin should be 
built from the source code for use. Plugin build procedure is described in 
`How to build Arm® CPU plugin <https://github.com/openvinotoolkit/openvino_contrib/wiki/How-to-build-ARM-CPU-plugin>`__ 
guide.

The set of supported layers is defined on the 
`Op-set specification page <https://github.com/openvinotoolkit/openvino_contrib/wiki/ARM-plugin-operation-set-specification>`__.

Supported Inference Data Types
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The Arm® CPU plugin supports the following data types as inference precision 
of internal primitives:

* Floating-point data types:

  * f32

  * f16

* Quantized data types:

  * i8 (support is experimental)

:ref:`Hello Query Device C++ Sample <doxid-openvino_inference_engine_samples_hello_query_device__r_e_a_d_m_e>` 
can be used to print out supported data types for all detected devices.

Supported Features
~~~~~~~~~~~~~~~~~~

**Preprocessing Acceleration** The Arm® CPU plugin supports the following 
accelerated preprocessing operations:

* Precision conversion:

  * u8 -> u16, s16, s32

  * u16 -> u8, u32

  * s16 -> u8, s32

  * f16 -> f32

* Transposition of tensors with dims < 5

* Interpolation of 4D tensors with no padding (``pads_begin`` and ``pads_end`` 
  equal 0).

The Arm® CPU plugin supports the following preprocessing operations, however 
they are not accelerated:

* Precision conversion that is not mentioned above

* Color conversion:

  * NV12 to RGB

  * NV12 to BGR

  * i420 to RGB

  * i420 to BGR

For more details, see the :ref:`preprocessing API guide <deploy_infer__preprocessing_overview>`.

Supported Properties
~~~~~~~~~~~~~~~~~~~~

The plugin supports the properties listed below.

**Read-write Properties** In order to take effect, all parameters must be set 
before calling ``:ref:`ov::Core::compile_model() <doxid-classov_1_1_core_1a46555f0803e8c29524626be08e7f5c5a>``` 
or passed as additional argument to ``:ref:`ov::Core::compile_model() <doxid-classov_1_1_core_1a46555f0803e8c29524626be08e7f5c5a>```

* :ref:`ov::enable_profiling <doxid-group__ov__runtime__cpp__prop__api_1gafc5bef2fc2b5cfb5a0709cfb04346438>`

**Read-only Properties**

* :ref:`ov::supported_properties <doxid-group__ov__runtime__cpp__prop__api_1ga097f1274f26f3f4e1aa4fc3928748592>`

* :ref:`ov::available_devices <doxid-group__ov__runtime__cpp__prop__api_1gac4d3e86ef4fc43b1a80ec28c7be39ef1>`

* :ref:`ov::range_for_async_infer_requests <doxid-group__ov__runtime__cpp__prop__api_1ga3549425153790834c212d905b8216196>`

* :ref:`ov::range_for_streams <doxid-group__ov__runtime__cpp__prop__api_1ga8a5d84196f6873729167aa512c34a94a>`

* :ref:`ov::device::full_name <doxid-group__ov__runtime__cpp__prop__api_1gaabacd9ea113b966be7b53b1d70fd6f42>`

* :ref:`ov::device::capabilities <doxid-group__ov__runtime__cpp__prop__api_1gadb13d62787fc4485733329f044987294>`

Known Layers Limitation
~~~~~~~~~~~~~~~~~~~~~~~

* ``AvgPool`` layer is supported via arm_compute library for 4D input tensor 
  and via reference implementation for other cases.

* ``BatchToSpace`` layer is supported for 4D tensors only and constant nodes: 
  ``block_shape`` with ``N`` = 1 and ``C`` = 1, ``crops_begin`` with zero 
  values and ``crops_end`` with zero values.

* ``ConvertLike`` layer is supported for configuration like ``Convert``.

* ``DepthToSpace`` layer is supported for 4D tensors only and for 
  ``BLOCKS_FIRST`` of ``mode`` attribute.

* ``Equal`` does not support ``broadcast`` for inputs.

* ``Gather`` layer is supported for constant scalar or 1D indices axes only. 
  Layer is supported via arm_compute library for non negative indices and via 
  reference implementation otherwise.

* ``Less`` does not support ``broadcast`` for inputs.

* ``LessEqual`` does not support ``broadcast`` for inputs.

* ``LRN`` layer is supported for ``axes = {1}`` or ``axes = {2, 3}`` only.

* ``MaxPool-1`` layer is supported via arm_compute library for 4D input tensor 
  and via reference implementation for other cases.

* ``Mod`` layer is supported for f32 only.

* ``MVN`` layer is supported via arm_compute library for 2D inputs and 
  ``false`` value of ``normalize_variance`` and ``false`` value of 
  ``across_channels``, for other cases layer is implemented via runtime 
  reference.

* ``Normalize`` layer is supported via arm_compute library with ``MAX`` value 
  of ``eps_mode`` and ``axes = {2 | 3}``, and for ``ADD`` value of ``eps_mode`` 
  layer uses ``DecomposeNormalizeL2Add``. For other cases layer is implemented 
  via runtime reference.

* ``NotEqual`` does not support ``broadcast`` for inputs.

* ``Pad`` layer works with ``pad_mode = {REFLECT | CONSTANT | SYMMETRIC}`` 
  parameters only.

* ``Round`` layer is supported via arm_compute library with 
  ``RoundMode::HALF_AWAY_FROM_ZERO`` value of ``mode``, for other cases layer 
  is implemented via runtime reference.

* ``SpaceToBatch`` layer is supported for 4D tensors only and constant nodes: 
  ``shapes``, ``pads_begin`` or ``pads_end`` with zero paddings for batch or 
  channels and one values ``shapes`` for batch and channels.

* ``SpaceToDepth`` layer is supported for 4D tensors only and for 
  ``BLOCKS_FIRST`` of ``mode`` attribute.

* ``StridedSlice`` layer is supported via arm_compute library for tensors with 
  dims < 5 and zero values of ``ellipsis_mask`` or zero values of 
  ``new_axis_mask`` and ``shrink_axis_mask``. For other cases, layer is 
  implemented via runtime reference.

* ``FakeQuantize`` layer is supported via arm_compute library, in Low Precision 
evaluation mode for suitable models, and via runtime reference otherwise.

Additional Resources
~~~~~~~~~~~~~~~~~~~~

* `How to run YOLOv4 model inference using OpenVINO™ and OpenCV on Arm® <https://opencv.org/how-to-run-yolov4-using-openvino-and-opencv-on-arm/>`__.

* `Face recognition on Android™ using OpenVINO™ toolkit with Arm® plugin <https://opencv.org/face-recognition-on-android-using-openvino-toolkit-with-arm-plugin/>`__.
