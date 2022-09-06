.. index:: pair: page; GPU Device
.. _deploy_infer__gpu_device:

.. meta::
   :description: The GPU plugin in the Intel® Distribution of OpenVINO™ toolkit 
                 is is an OpenCL based plugin for inference of deep neural 
                 networks on Intel® GPus.
   :keywords: OpenVINO™, OpenVINO Runtime, GPU plugin, Intel GPU, inference, 
              inference device, integrated Intel GPU, discrete Intel GPU, 
              inference precision, f32 data type, f16 data type, bfloat16, 
              u8 data type, i8 data type, u1 data type, FP32, FP32 precision, 
              floating-point data type, FP16 precision, multi-device 
              execution, multi-stream execution, dynamic shapes, preprocessing 
              acceleration, model caching, extensibility, read-write 
              properties, read-only properties, OpenVINO IR, OpenVINO 
              Intermediate Representation, compile model, BATCH, BATCH plugin

GPU Device
==========

:target:`deploy_infer__gpu_device_1md_openvino_docs_ov_runtime_ug_supported_plugins_gpu`

.. toctree::
   :maxdepth: 1
   :hidden:

   ./inference-device-gpu/remote-tensor-gpu

The GPU plugin is an OpenCL based plugin for inference of deep neural networks 
on Intel GPUs, both integrated and discrete ones. For an in-depth description 
of the GPU plugin, see:

* `GPU plugin developers documentation <https://github.com/openvinotoolkit/openvino/wiki/GPUPluginDevelopersDocs>`__

* `OpenVINO Runtime GPU plugin source files <https://github.com/openvinotoolkit/openvino/tree/master/src/plugins/intel_gpu/>`__

* `Accelerate Deep Learning Inference with Intel® Processor Graphics <https://software.intel.com/en-us/articles/accelerating-deep-learning-inference-with-intel-processor-graphics>`__.

The GPU plugin is a part of the Intel® Distribution of OpenVINO™ toolkit. For 
more information on how to configure a system to use it, see the 
:ref:`GPU configuration <install__config_gpu>`.

Device Naming Convention
~~~~~~~~~~~~~~~~~~~~~~~~

* Devices are enumerated as ``GPU.X``, where ``X={0, 1, 2,...}`` (only Intel® 
  GPU devices are considered).

* If the system has an integrated GPU, its ``id`` is always 0 (``GPU.0``).

* The order of other GPUs is not predefined and depends on the GPU driver.

* The ``GPU`` is an alias for ``GPU.0``.

* If the system does not have an integrated GPU, devices are enumerated, 
  starting from 0.

* For GPUs with multi-tile architecture (multiple sub-devices in OpenCL terms), 
  a specific tile may be addressed as ``GPU.X.Y``, where ``X,Y={0, 1, 2,...}``, 
  ``X`` - id of the GPU device, ``Y`` - id of the tile within device ``X``

For demonstration purposes, see the 
:ref:`Hello Query Device C++ Sample <doxid-openvino_inference_engine_samples_hello_query_device__r_e_a_d_m_e>` 
that can print out the list of available devices with associated indices. Below 
is an example output (truncated to the device names only):

.. ref-code-block:: cpp

   ./hello_query_device
   Available devices:
       Device: CPU
   ...
       Device: GPU.0
   ...
       Device: GPU.1
   ...
       Device: HDDL

Then, device name can be passed to the 
``:ref:`ov::Core::compile_model() <doxid-classov_1_1_core_1a46555f0803e8c29524626be08e7f5c5a>``` 
method:

.. tab:: Running on a default device

   .. tab:: C++

      .. ref-code-block:: cpp

         :ref:`ov::Core <doxid-classov_1_1_core>` core;
         auto :ref:`model <doxid-group__ov__runtime__cpp__prop__api_1ga461856fdfb6d7533dc53355aec9e9fad>` = core.:ref:`read_model <doxid-classov_1_1_core_1ae0576a95f841c3a6f5e46e4802716981>`("model.xml");
         auto compiled_model = core.:ref:`compile_model <doxid-classov_1_1_core_1a46555f0803e8c29524626be08e7f5c5a>`(:ref:`model <doxid-group__ov__runtime__cpp__prop__api_1ga461856fdfb6d7533dc53355aec9e9fad>`, "GPU");

   .. tab:: Python

      .. ref-code-block:: cpp

         core = Core()
         model = core.read_model("model.xml")
         compiled_model = core.compile_model(model, "GPU")

.. tab:: Running on a specific GPU

   .. tab:: C++

      .. ref-code-block:: cpp

         :ref:`ov::Core <doxid-classov_1_1_core>` core;
         auto :ref:`model <doxid-group__ov__runtime__cpp__prop__api_1ga461856fdfb6d7533dc53355aec9e9fad>` = core.:ref:`read_model <doxid-classov_1_1_core_1ae0576a95f841c3a6f5e46e4802716981>`("model.xml");
         auto compiled_model = core.:ref:`compile_model <doxid-classov_1_1_core_1a46555f0803e8c29524626be08e7f5c5a>`(:ref:`model <doxid-group__ov__runtime__cpp__prop__api_1ga461856fdfb6d7533dc53355aec9e9fad>`, "GPU.1");

   .. tab:: Python

      .. ref-code-block:: cpp

         core = Core()
         model = core.read_model("model.xml")
         compiled_model = core.compile_model(model, "GPU.1")

.. tab:: Running on a specific tile

   .. tab:: C++

      .. ref-code-block:: cpp

         :ref:`ov::Core <doxid-classov_1_1_core>` core;
         auto :ref:`model <doxid-group__ov__runtime__cpp__prop__api_1ga461856fdfb6d7533dc53355aec9e9fad>` = core.:ref:`read_model <doxid-classov_1_1_core_1ae0576a95f841c3a6f5e46e4802716981>`("model.xml");
         auto compiled_model = core.:ref:`compile_model <doxid-classov_1_1_core_1a46555f0803e8c29524626be08e7f5c5a>`(:ref:`model <doxid-group__ov__runtime__cpp__prop__api_1ga461856fdfb6d7533dc53355aec9e9fad>`, "GPU.1.0");

   .. tab:: Python

      .. ref-code-block:: cpp

         core = Core()
         model = core.read_model("model.xml")
         compiled_model = core.compile_model(model, "GPU.1.0")


Supported Inference Data Types
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The GPU plugin supports the following data types as inference precision of 
internal primitives:

* Floating-point data types:

  * f32

  * f16

* Quantized data types:

  * u8

  * i8

  * u1

Selected precision of each primitive depends on the operation precision in IR, 
quantization primitives, and available hardware capabilities. The ``u1`` / 
``u8`` / ``i8`` data types are used for quantized operations only, which means 
that they are not selected automatically for non-quantized operations. For more 
details on how to get a quantized model, refer to the 
:ref:`Model Optimization guide <optim_perf__model_optim_guide>`.

Floating-point precision of a GPU primitive is selected based on operation 
precision in the OpenVINO IR, except for the 
:ref:`compressed f16 OpenVINO IR form <conv_prep__fp16_compression>`, 
which is executed in the ``f16`` precision.

.. note:: Hardware acceleration for ``i8`` / ``u8`` precision may be unavailable 
   on some platforms. In such cases, a model is executed in the floating-point 
   precision taken from IR. Hardware support of ``u8`` / ``i8`` acceleration can 
   be queried via the ``:ref:`ov::device::capabilities <doxid-group__ov__runtime__cpp__prop__api_1gadb13d62787fc4485733329f044987294>``` 
   property.

:ref:`Hello Query Device C++ Sample <doxid-openvino_inference_engine_samples_hello_query_device__r_e_a_d_m_e>` 
can be used to print out the supported data types for all detected devices.

Supported Features
~~~~~~~~~~~~~~~~~~

The GPU plugin supports the following features:

Multi-device Execution
----------------------

If a system has multiple GPUs (for example, an integrated and a discrete Intel 
GPU), then any supported model can be executed on all GPUs simultaneously. It 
is done by specifying ``MULTI:GPU.1,GPU.0`` as a target device.

.. tab:: C++

   .. ref-code-block:: cpp

      :ref:`ov::Core <doxid-classov_1_1_core>` core;
      auto :ref:`model <doxid-group__ov__runtime__cpp__prop__api_1ga461856fdfb6d7533dc53355aec9e9fad>` = core.:ref:`read_model <doxid-classov_1_1_core_1ae0576a95f841c3a6f5e46e4802716981>`("model.xml");
      auto compiled_model = core.:ref:`compile_model <doxid-classov_1_1_core_1a46555f0803e8c29524626be08e7f5c5a>`(:ref:`model <doxid-group__ov__runtime__cpp__prop__api_1ga461856fdfb6d7533dc53355aec9e9fad>`, "MULTI:GPU.1,GPU.0");

.. tab:: Python

   .. ref-code-block:: cpp

      core = Core()
      model = core.read_model("model.xml")
      compiled_model = core.compile_model(model, "MULTI:GPU.1,GPU.0")


For more details, see the :ref:`Multi-device execution <deploy_infer__multi_plugin>`.

Automatic Batching
------------------

The GPU plugin is capable of reporting 
``:ref:`ov::max_batch_size <doxid-group__ov__runtime__cpp__prop__api_1ga5dbd8ab0c8a177234cade9a54c96249c>``` 
and ``:ref:`ov::optimal_batch_size <doxid-group__ov__runtime__cpp__prop__api_1ga129bad2da2fc2a40a7d746d86fc9c68d>``` 
metrics with respect to the current hardware platform and model. Therefore, 
automatic batching is enabled by default when 
``:ref:`ov::optimal_batch_size <doxid-group__ov__runtime__cpp__prop__api_1ga129bad2da2fc2a40a7d746d86fc9c68d>``` 
is ``> 1`` and ``ov::hint::performance_mode(ov::hint::PerformanceMode::THROUGHPUT)`` 
is set. Alternatively, it can be enabled explicitly via the device notion, 
for example ``BATCH:GPU``.

.. tab:: Batching via BATCH plugin

   .. tab:: C++

      .. ref-code-block:: cpp

         :ref:`ov::Core <doxid-classov_1_1_core>` core;
         auto :ref:`model <doxid-group__ov__runtime__cpp__prop__api_1ga461856fdfb6d7533dc53355aec9e9fad>` = core.:ref:`read_model <doxid-classov_1_1_core_1ae0576a95f841c3a6f5e46e4802716981>`("model.xml");
         auto compiled_model = core.:ref:`compile_model <doxid-classov_1_1_core_1a46555f0803e8c29524626be08e7f5c5a>`(:ref:`model <doxid-group__ov__runtime__cpp__prop__api_1ga461856fdfb6d7533dc53355aec9e9fad>`, "BATCH:GPU");

   .. tab:: Python

      .. ref-code-block:: cpp

         core = Core()
         model = core.read_model("model.xml")
         compiled_model = core.compile_model(model, "BATCH:GPU")

.. tab:: Batching via throughput hint

   .. tab:: C++

      .. ref-code-block:: cpp

         :ref:`ov::Core <doxid-classov_1_1_core>` core;
         auto :ref:`model <doxid-group__ov__runtime__cpp__prop__api_1ga461856fdfb6d7533dc53355aec9e9fad>` = core.:ref:`read_model <doxid-classov_1_1_core_1ae0576a95f841c3a6f5e46e4802716981>`("model.xml");
         auto compiled_model = core.:ref:`compile_model <doxid-classov_1_1_core_1a46555f0803e8c29524626be08e7f5c5a>`(:ref:`model <doxid-group__ov__runtime__cpp__prop__api_1ga461856fdfb6d7533dc53355aec9e9fad>`, "GPU", :ref:`ov::hint::performance_mode <doxid-group__ov__runtime__cpp__prop__api_1ga2691fe27acc8aa1d1700ad40b6da3ba2>`(:ref:`ov::hint::PerformanceMode::THROUGHPUT <doxid-group__ov__runtime__cpp__prop__api_1gga032aa530efa40760b79af14913d48d73a50f9b1f40c078d242af7ec323ace44b3>`));

   .. tab:: Python

      .. ref-code-block:: cpp

         core = Core()
         model = core.read_model("model.xml")
         compiled_model = core.compile_model(model, "GPU", {"PERFORMANCE_HINT": "THROUGHPUT"})


For more details, see the :ref:`Automatic batching <deploy_infer__automatic_batching>`.

Multi-stream Execution
----------------------

If either the ``ov::num_streams(n_streams)`` with ``n_streams > 1`` or the 
``ov::hint::performance_mode(ov::hint::PerformanceMode::THROUGHPUT)`` property 
is set for the GPU plugin, multiple streams are created for the model. In the 
case of GPU plugin each stream has its own host thread and an associated OpenCL 
queue which means that the incoming infer requests can be processed simultaneously.

.. note:: Simultaneous scheduling of kernels to different queues does not mean 
   that the kernels are actually executed in parallel on the GPU device. The 
   actual behavior depends on the hardware architecture and in some cases the 
   execution may be serialized inside the GPU driver.

When multiple inferences of the same model need to be executed in parallel, the 
multi-stream feature is preferred to multiple instances of the model or 
application. The reason for this is that the implementation of streams in the 
GPU plugin supports weight memory sharing across streams, thus, memory 
consumption may be lower, compared to the other approaches.

For more details, see the :ref:`optimization guide <optim_perf__runtime_inference_optim>`.

Dynamic Shapes
--------------

The GPU plugin supports dynamic shapes for batch dimension only (specified as 
``N`` in the :ref:`layouts terms <deploy_infer__layout_api_overview>`) 
with a fixed upper bound. Any other dynamic dimensions are unsupported. Internally, 
GPU plugin creates ``log2(N)`` (``N`` - is an upper bound for batch dimension 
here) low-level execution graphs for batch sizes equal to powers of 2 to emulate 
dynamic behavior, so that incoming infer request with a specific batch size is 
executed via a minimal combination of internal networks. For example, batch size 
33 may be executed via 2 internal networks with batch size 32 and 1.

.. note:: Such approach requires much more memory and the overall model compilation 
   time is significantly longer, compared to the static batch scenario.

The code snippet below demonstrates how to use dynamic batching in simple scenarios:

.. tab:: C++

   .. ref-code-block:: cpp


      // Read model
      :ref:`ov::Core <doxid-classov_1_1_core>` core;
      auto :ref:`model <doxid-group__ov__runtime__cpp__prop__api_1ga461856fdfb6d7533dc53355aec9e9fad>` = core.:ref:`read_model <doxid-classov_1_1_core_1ae0576a95f841c3a6f5e46e4802716981>`("model.xml");

      :ref:`model <doxid-group__ov__runtime__cpp__prop__api_1ga461856fdfb6d7533dc53355aec9e9fad>`->reshape({{:ref:`ov::Dimension <doxid-classov_1_1_dimension>`(1, 10), :ref:`ov::Dimension <doxid-classov_1_1_dimension>`(:ref:`C <doxid-ie__preprocess__gapi_8cpp_1a5464533d23b59ba11030432e73528730>`), :ref:`ov::Dimension <doxid-classov_1_1_dimension>`(:ref:`H <doxid-ie__preprocess__gapi_8cpp_1affa487e8e3cc48473cfc05c0ce0165e9>`), :ref:`ov::Dimension <doxid-classov_1_1_dimension>`(:ref:`W <doxid-ie__preprocess__gapi_8cpp_1a2dd51e03005d5cb52315290d27f61870>`)}});  // {1..10, C, H, W}

      // compile model and create infer request
      auto compiled_model = core.:ref:`compile_model <doxid-classov_1_1_core_1a46555f0803e8c29524626be08e7f5c5a>`(:ref:`model <doxid-group__ov__runtime__cpp__prop__api_1ga461856fdfb6d7533dc53355aec9e9fad>`, "GPU");
      auto infer_request = compiled_model.:ref:`create_infer_request <doxid-classov_1_1_compiled_model_1ae3633c0eb5173ed776446fba32b95953>`();
      auto input = :ref:`model <doxid-group__ov__runtime__cpp__prop__api_1ga461856fdfb6d7533dc53355aec9e9fad>`->get_parameters().at(0);

      // ...

      // create input tensor with specific batch size
      :ref:`ov::Tensor <doxid-classov_1_1_tensor>` input_tensor(input->get_element_type(), {2, C, H, W});

      // ...

      infer_request.set_tensor(input, input_tensor);
      infer_request.infer();

.. tab:: Python

   .. ref-code-block:: cpp

      core = :ref:`ov.Core <doxid-classov_1_1_core>`()

      C = 3
      H = 224
      W = 224

      model = core.read_model("model.xml")
      model.reshape([(1, 10), C, H, W])

      # compile model and create infer request
      compiled_model = core.compile_model(model, "GPU")
      infer_request = compiled_model.create_infer_request()

      # create input tensor with specific batch size
      input_tensor = :ref:`ov.Tensor <doxid-classov_1_1_tensor>`(model.input().element_type, [2, C, H, W])

      # ...

      infer_request.infer([input_tensor])


For more details, see the :ref:`dynamic shapes guide <deploy_infer__dynamic_shapes>`.

Preprocessing Acceleration
--------------------------

The GPU plugin has the following additional preprocessing options:

* The ``:ref:`ov::intel_gpu::memory_type::surface <doxid-group__ov__runtime__ocl__gpu__prop__cpp__api_1gaec0856a3b996876371138961269b742d>``` and ``ov::intel_gpu::memory_type::buffer`` values for the ``:ref:`ov::preprocess::InputTensorInfo::set_memory_type() <doxid-classov_1_1preprocess_1_1_input_tensor_info_1ad838f8c41ba0ab450b72fec5e2ebf808>``` preprocessing method. These values are intended to be used to provide a hint for the plugin on the type of input Tensors that will be set in runtime to generate proper kernels.

.. tab:: C++

   .. ref-code-block:: cpp

      using namespace :ref:`ov::preprocess <doxid-namespaceov_1_1preprocess>`;
      auto p = PrePostProcessor(:ref:`model <doxid-group__ov__runtime__cpp__prop__api_1ga461856fdfb6d7533dc53355aec9e9fad>`);
      p.input().tensor().set_element_type(:ref:`ov::element::u8 <doxid-group__ov__element__cpp__api_1gaaf60c536d3e295285f6a899eb3d29e2f>`)
                        .set_color_format(:ref:`ov::preprocess::ColorFormat::NV12_TWO_PLANES <doxid-namespaceov_1_1preprocess_1ab027f26e58038e454e1b50a5243f1707a54f60c652650de96e9d118187b3ba25f>`, {"y", "uv"})
                        .set_memory_type(:ref:`ov::intel_gpu::memory_type::surface <doxid-group__ov__runtime__ocl__gpu__prop__cpp__api_1gaec0856a3b996876371138961269b742d>`);
      p.input().preprocess().convert_color(:ref:`ov::preprocess::ColorFormat::BGR <doxid-namespaceov_1_1preprocess_1ab027f26e58038e454e1b50a5243f1707a2ad5640ebdec72fc79531d1778c6c2dc>`);
      p.input().model().set_layout("NCHW");
      auto model_with_preproc = p.build();

.. tab:: Python

   .. ref-code-block:: cpp

      from openvino.runtime import Core, Type, Layout
      from openvino.preprocess import PrePostProcessor, ColorFormat

      core = Core()
      model = core.read_model("model.xml")

      p = PrePostProcessor(model)
      p.input().tensor().set_element_type(Type.u8) \
                        .set_color_format(ColorFormat.NV12_TWO_PLANES, ["y", "uv"]) \
                        .set_memory_type("GPU_SURFACE")
      p.input().preprocess().convert_color(ColorFormat.BGR)
      p.input().:ref:`model <doxid-group__ov__runtime__cpp__prop__api_1ga461856fdfb6d7533dc53355aec9e9fad>`().:ref:`set_layout <doxid-group__ov__layout__cpp__api_1ga18464fb8ed029acb5fdc2bb1737358d9>`(:ref:`Layout <doxid-namespace_inference_engine_1a246d143abc5ca07da8d2cadeeb88fdb8>`("NCHW"))
      model_with_preproc = p.build()


With such preprocessing, GPU plugin will expect 
``:ref:`ov::intel_gpu::ocl::ClImage2DTensor <doxid-classov_1_1intel__gpu_1_1ocl_1_1_cl_image2_d_tensor>``` 
(or derived) to be passed for each NV12 plane via 
``:ref:`ov::InferRequest::set_tensor() <doxid-classov_1_1_infer_request_1af54f126e7fb3b3a0343841dda8bcc368>``` 
or ``:ref:`ov::InferRequest::set_tensors() <doxid-classov_1_1_infer_request_1a935a952c07cc7130a64614d0952db997>``` 
methods.

For usage examples, refer to the :ref:`RemoteTensor API <deploy_infer__gpu_device_remote_tensor>`.

For more details, see the :ref:`preprocessing API <deploy_infer__preprocessing_overview>`.

Model Caching
-------------

Cache for the GPU plugin may be enabled via the common OpenVINO 
``:ref:`ov::cache_dir <doxid-group__ov__runtime__cpp__prop__api_1ga3276fc4ed7cc7d0bbdcf0ae12063728d>``` 
property. GPU plugin implementation supports only caching of compiled kernels, 
so all plugin-specific model transformations are executed on each 
``:ref:`ov::Core::compile_model() <doxid-classov_1_1_core_1a46555f0803e8c29524626be08e7f5c5a>``` 
call regardless of the ``cache_dir`` option. Still, since kernel compilation 
is a bottleneck in the model loading process, a significant load time reduction 
can be achieved with the ``:ref:`ov::cache_dir <doxid-group__ov__runtime__cpp__prop__api_1ga3276fc4ed7cc7d0bbdcf0ae12063728d>``` 
property enabled.

For more details, see the :ref:`Model caching overview <optim_perf__model_caching>`.

Extensibility
-------------

For information on this subject, see the 
:ref:`GPU Extensibility <extensibility__gpu>`.

GPU Context and Memory Sharing via RemoteTensor API
---------------------------------------------------

For information on this subject, see the 
:ref:`RemoteTensor API of GPU Plugin <deploy_infer__gpu_device_remote_tensor>`.

Supported Properties
~~~~~~~~~~~~~~~~~~~~

The plugin supports the properties listed below.

Read-write properties
---------------------

All parameters must be set before calling 
``:ref:`ov::Core::compile_model() <doxid-classov_1_1_core_1a46555f0803e8c29524626be08e7f5c5a>``` 
in order to take effect or passed as additional argument to 
``:ref:`ov::Core::compile_model() <doxid-classov_1_1_core_1a46555f0803e8c29524626be08e7f5c5a>```.

* :ref:`ov::cache_dir <doxid-group__ov__runtime__cpp__prop__api_1ga3276fc4ed7cc7d0bbdcf0ae12063728d>`

* :ref:`ov::enable_profiling <doxid-group__ov__runtime__cpp__prop__api_1gafc5bef2fc2b5cfb5a0709cfb04346438>`

* :ref:`ov::hint::model_priority <doxid-group__ov__runtime__cpp__prop__api_1ga3663a3976ff7c4bdc3ccdb9ce44945ce>`

* :ref:`ov::hint::performance_mode <doxid-group__ov__runtime__cpp__prop__api_1ga2691fe27acc8aa1d1700ad40b6da3ba2>`

* ov::hint::num_requests

* :ref:`ov::hint::inference_precision <doxid-group__ov__runtime__cpp__prop__api_1gad605a888f3c9b7598ab55023fbf44240>`

* :ref:`ov::num_streams <doxid-group__ov__runtime__cpp__prop__api_1ga6c63a0223565f650475450fdb466bc0c>`

* :ref:`ov::compilation_num_threads <doxid-group__ov__runtime__cpp__prop__api_1ga91555d2fad22aa802aa9d36698805755>`

* :ref:`ov::device::id <doxid-group__ov__runtime__cpp__prop__api_1ga433b8ea52e99c2b1fa8b26453485d75d>`

* :ref:`ov::intel_gpu::hint::host_task_priority <doxid-group__ov__runtime__ocl__gpu__prop__cpp__api_1ga1650ac020ec6e9ea8d03f898ef454e43>`

* :ref:`ov::intel_gpu::hint::queue_priority <doxid-group__ov__runtime__ocl__gpu__prop__cpp__api_1ga41a9b0bfa860966128952ebfcca324b9>`

* :ref:`ov::intel_gpu::hint::queue_throttle <doxid-group__ov__runtime__ocl__gpu__prop__cpp__api_1gace6031a0761c1917aa84135fe2163d56>`

* :ref:`ov::intel_gpu::enable_loop_unrolling <doxid-group__ov__runtime__ocl__gpu__prop__cpp__api_1ga2d18d0f9e29ddde42b95d523405ae322>`

Read-only Properties
--------------------

* :ref:`ov::supported_properties <doxid-group__ov__runtime__cpp__prop__api_1ga097f1274f26f3f4e1aa4fc3928748592>`

* :ref:`ov::available_devices <doxid-group__ov__runtime__cpp__prop__api_1gac4d3e86ef4fc43b1a80ec28c7be39ef1>`

* :ref:`ov::range_for_async_infer_requests <doxid-group__ov__runtime__cpp__prop__api_1ga3549425153790834c212d905b8216196>`

* :ref:`ov::range_for_streams <doxid-group__ov__runtime__cpp__prop__api_1ga8a5d84196f6873729167aa512c34a94a>`

* :ref:`ov::optimal_batch_size <doxid-group__ov__runtime__cpp__prop__api_1ga129bad2da2fc2a40a7d746d86fc9c68d>`

* :ref:`ov::max_batch_size <doxid-group__ov__runtime__cpp__prop__api_1ga5dbd8ab0c8a177234cade9a54c96249c>`

* :ref:`ov::device::full_name <doxid-group__ov__runtime__cpp__prop__api_1gaabacd9ea113b966be7b53b1d70fd6f42>`

* :ref:`ov::device::type <doxid-group__ov__runtime__cpp__prop__api_1gaf9b20fd37487c1f525e68c6e0567f1f1>`

* :ref:`ov::device::gops <doxid-group__ov__runtime__cpp__prop__api_1gae233c458317f6ae508b887eb09308c4c>`

* :ref:`ov::device::capabilities <doxid-group__ov__runtime__cpp__prop__api_1gadb13d62787fc4485733329f044987294>`

* :ref:`ov::intel_gpu::device_total_mem_size <doxid-group__ov__runtime__ocl__gpu__prop__cpp__api_1ga4545149544127b7f82b5d673b8a5a017>`

* :ref:`ov::intel_gpu::uarch_version <doxid-group__ov__runtime__ocl__gpu__prop__cpp__api_1ga55179d37180f123686ab43b27ed3f2c9>`

* :ref:`ov::intel_gpu::execution_units_count <doxid-group__ov__runtime__ocl__gpu__prop__cpp__api_1ga86642bacd4b0fa7f803c212e72318d79>`

* :ref:`ov::intel_gpu::memory_statistics <doxid-group__ov__runtime__ocl__gpu__prop__cpp__api_1ga2364c38776f270d5b9560e745fd8ff80>`

Limitations
~~~~~~~~~~~

In some cases, the GPU plugin may implicitly execute several primitives on CPU 
using internal implementations, which may lead to an increase in CPU utilization. 
Below is a list of such operations:

* Proposal

* NonMaxSuppression

* DetectionOutput

The behavior depends on specific parameters of the operations and hardware configuration.

.. _gpu-checklist:

GPU Performance Checklist: Summary
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Since OpenVINO relies on the OpenCL kernels for the GPU implementation, many 
general OpenCL tips apply:

* Prefer ``FP16`` inference precision over ``FP32``, as Model Optimizer can 
  generate both variants, and the ``FP32`` is the default. Also, consider using 
  the `Post-training Optimization Tool <https://docs.openvino.ai/latest/pot_introduction.html>`__.

* Try to group individual infer jobs by using 
  :ref:`automatic batching <deploy_infer__automatic_batching>`.

* Consider :ref:`caching <optim_perf__model_caching>` 
  to minimize model load time.

* If your application performs inference on the CPU alongside the GPU, or otherwise 
  loads the host heavily, make sure that the OpenCL driver threads do not starve. 
  :ref:`CPU configuration options <deploy_infer__cpu_device>` 
  can be used to limit the number of inference threads for the CPU plugin.

* Even in the GPU-only scenario, a GPU driver might occupy a CPU core with 
  spin-loop polling for completion. If CPU load is a concern, consider the 
  dedicated ``queue_throttle`` property mentioned previously. Note that this 
  option may increase inference latency, so consider combining it with multiple 
  GPU streams or :ref:`throughput performance hints <deploy_infer__performance_hints>`.

* When operating media inputs, consider 
  :ref:`remote tensors API of the GPU Plugin <deploy_infer__gpu_device_remote_tensor>`.

Additional Resources
~~~~~~~~~~~~~~~~~~~~

* :ref:`Supported Devices <doxid-openvino_docs__o_v__u_g_supported_plugins__supported__devices>`

* :ref:`Optimization guide <optim_perf__introduction>`

* `GPU plugin developers documentation <https://github.com/openvinotoolkit/openvino/wiki/GPUPluginDevelopersDocs>`__
