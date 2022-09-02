.. index:: pair: page; GNA Device
.. _deploy_infer__gna_device:

.. meta::
   :description: The GNA plugin in OpenVINO™ Runtime enables running inference 
                 on Intel® Gaussian & Neural Accelerator (GNA) and in the 
                 software execution mode on CPU.
   :keywords: OpenVINO™, GNA plugin, OpenVINO Runtime, GNA device, inference device, 
              inference, model inference, software execution mode, CPU device, 
              offload inference, Intel® Core™ Processors, GNA 2.0, Intel® GNA 
              hardware, compile model, GNA 3.0, 2D convolution, interoperability,
              software emulation mode, Windows GNA driver, i16 data type, i8 data 
              type, Automatic QoS feature, noise reduction, stateful models, 
              model caching, profiling, inference request, import model, 
              Convolution, MatMul, Convolution layer, MatMul layer

GNA Device
==========

:target:`deploy_infer__gna_device_1md_openvino_docs_ov_runtime_ug_supported_plugins_gna` The Intel® Gaussian & Neural Accelerator (GNA) is a low-power neural coprocessor for continuous inference at the edge.

Intel® GNA is not intended to replace typical inference devices such as the CPU, graphics processing unit (GPU), or vision processing unit (VPU). It is designed for offloading continuous inference workloads including but not limited to noise reduction or speech recognition to save power and free CPU resources.

The GNA plugin provides a way to run inference on Intel® GNA, as well as in the software execution mode on CPU.

For more details on how to configure a machine to use GNA plugin, see the :ref:`GNA configuration page <install__config_gna>`.

Intel® GNA Generational Differences
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The first (1.0) and second (2.0) versions of Intel® GNA found in 10th and 11th generation Intel® Core™ Processors may be considered functionally equivalent. Intel® GNA 2.0 provided performance improvement with respect to Intel® GNA 1.0. Starting with 12th Generation Intel® Core™ Processors (formerly codenamed Alder Lake), support for Intel® GNA 3.0 features is being added.

In this documentation, "GNA 2.0" refers to Intel® GNA hardware delivered on 10th and 11th generation Intel® Core™ processors, and the term "GNA 3.0" refers to GNA hardware delivered on 12th generation Intel® Core™ processors.

Intel® GNA Forward and Backward Compatibility
----------------------------------------------

When a model is run, using the GNA plugin, it is compiled internally for the specific hardware target. It is possible to export a compiled model, using `Import/Export <#import-export>`__ functionality to use it later. In general, there is no guarantee that a model compiled and exported for GNA 2.0 runs on GNA 3.0 or vice versa.

.. csv-table:: Interoperability of compile target and hardware target
   :header: "Hardware", "Compile target 2.0", "Compile target 3.0"

   "GNA 2.0", "Supported", "Not supported (incompatible layers emulated on CPU)"
   "GNA 3.0", "Partially supported", "Supported"

.. note::

   In most cases, a network compiled for GNA 2.0 runs as expected on GNA 3.0. 
   However, the performance may be worse compared to when a network is compiled 
   specifically for the latter. The exception is a network with convolutions with 
   the number of filters greater than 8192 
   (see the `Models and Operations Limitations <#models-and-operations-limitations>`__ section).



For optimal work with POT quantized models, which include 2D convolutions on GNA 3.0 hardware, the `following requirements <#support-for-2d-convolutions-using-pot>`__ should be satisfied.

Choose a compile target with priority on: cross-platform execution, performance, memory, or power optimization.

Use the following properties to check interoperability in your application: ``:ref:`ov::intel_gna::execution_target <doxid-group__ov__runtime__gna__prop__cpp__api_1ga4ecfa3938d07be52618f606bb54ac429>``` and ``:ref:`ov::intel_gna::compile_target <doxid-group__ov__runtime__gna__prop__cpp__api_1gad9a766500212ccb6826b47aedde9e825>```.

:ref:`Speech C++ Sample <doxid-openvino_inference_engine_samples_speech_sample__r_e_a_d_m_e>` can be used for experiments (see the ``-exec_target`` and ``-compile_target`` command line options).

Software Emulation Mode
~~~~~~~~~~~~~~~~~~~~~~~

Software emulation mode is used by default on platforms without GNA hardware support. Therefore, model runs even if there is no GNA HW within your platform. GNA plugin enables switching the execution between software emulation mode and hardware execution mode once the model has been loaded. For details, see a description of the ``:ref:`ov::intel_gna::execution_mode <doxid-group__ov__runtime__gna__prop__cpp__api_1ga68ea397901af8f965863fbe599535341>``` property.

Recovery from Interruption by High-Priority Windows Audio Processes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

GNA is designed for real-time workloads i.e., noise reduction. For such workloads, processing should be time constrained. Otherwise, extra delays may cause undesired effects such as *audio glitches*. The GNA driver provides a Quality of Service (QoS) mechanism to ensure that processing can satisfy real-time requirements. The mechanism interrupts requests that might cause high-priority Windows audio processes to miss the schedule. As a result, long running GNA tasks terminate early.

To prepare the applications correctly, use Automatic QoS Feature described below.

Automatic QoS Feature on Windows
--------------------------------

Starting with the 2021.4.1 release of OpenVINO™ and the 03.00.00.1363 version of Windows GNA driver, a new execution mode of ``:ref:`ov::intel_gna::ExecutionMode::HW_WITH_SW_FBACK <doxid-group__ov__runtime__gna__prop__cpp__api_1ggab1ef047d51bcaf91e5d2bbb1fd535499a5628dcdf14e39ece06c6ed5297b2a823>``` has been available to ensure that workloads satisfy real-time execution. In this mode, the GNA driver automatically falls back on CPU for a particular infer request if the HW queue is not empty. Therefore, there is no need for explicitly switching between GNA and CPU.

.. raw:: html

   <div class='sphinxtabset'>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="C++">





.. ref-code-block:: cpp

	#include <openvino/openvino.hpp>
	#include <openvino/runtime/intel_gna/properties.hpp>



.. ref-code-block:: cpp

	:ref:`ov::Core <doxid-classov_1_1_core>` core;
	auto :ref:`model <doxid-group__ov__runtime__cpp__prop__api_1ga461856fdfb6d7533dc53355aec9e9fad>` = core.:ref:`read_model <doxid-classov_1_1_core_1ae0576a95f841c3a6f5e46e4802716981>`(model_path);
	auto compiled_model = core.:ref:`compile_model <doxid-classov_1_1_core_1a46555f0803e8c29524626be08e7f5c5a>`(:ref:`model <doxid-group__ov__runtime__cpp__prop__api_1ga461856fdfb6d7533dc53355aec9e9fad>`, "GNA",
	   :ref:`ov::intel_gna::execution_mode <doxid-group__ov__runtime__gna__prop__cpp__api_1ga68ea397901af8f965863fbe599535341>`(:ref:`ov::intel_gna::ExecutionMode::HW_WITH_SW_FBACK <doxid-group__ov__runtime__gna__prop__cpp__api_1ggab1ef047d51bcaf91e5d2bbb1fd535499a5628dcdf14e39ece06c6ed5297b2a823>`));

.. raw:: html

   </div>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="Python">





.. ref-code-block:: cpp

	from openvino.runtime import Core



.. ref-code-block:: cpp

	core = Core()
	model = core.read_model(model=model_path)
	compiled_model = core.compile_model(model, device_name="GNA",
	    config={ 'GNA_DEVICE_MODE' : 'GNA_HW_WITH_SW_FBACK'})

.. raw:: html

   </div>







.. raw:: html

   </div>





.. note::

   Due to the "first come - first served" nature of GNA driver and the QoS feature, 
   this mode may lead to increased CPU consumption



if there are several clients using GNA simultaneously. Even a lightweight competing infer request, not cleared at the time when the user's GNA client process makes its request, can cause the user's request to be executed on CPU, unnecessarily increasing CPU utilization and power.

Supported Inference Data Types
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Intel® GNA essentially operates in the low-precision mode which represents a mix of 8-bit (``i8``), 16-bit (``i16``), and 32-bit (``i32``) integer computations.

GNA plugin users are encouraged to use the :ref:`Post-Training Optimization Tool <pot_tool_introduction>` to get a model with quantization hints based on statistics for the provided dataset.

Unlike other plugins supporting low-precision execution, the GNA plugin can calculate quantization factors at the model loading time. Therefore, a model can be run without calibration. However, this mode may not provide satisfactory accuracy because the internal quantization algorithm is based on heuristics, the efficiency of which depends on the model and dynamic range of input data. This mode is going to be deprecated soon.

GNA plugin supports the ``i16`` and ``i8`` quantized data types as inference precision of internal primitives.

:ref:`Hello Query Device C++ Sample <doxid-openvino_inference_engine_samples_hello_query_device__r_e_a_d_m_e>` can be used to print out supported data types for all detected devices.

:ref:`POT API Usage sample for GNA <pot_api_example_gna>` demonstrates how a model can be quantized for GNA, using POT API in two modes:

* Accuracy (i16 weights)

* Performance (i8 weights)

For POT quantized model, the ``:ref:`ov::hint::inference_precision <doxid-group__ov__runtime__cpp__prop__api_1gad605a888f3c9b7598ab55023fbf44240>``` property has no effect except cases described in `Support for 2D Convolutions using POT <#support-for-2d-convolutions-using-pot>`__.

Supported Features
~~~~~~~~~~~~~~~~~~

The plugin supports the features listed below:

Models Caching
--------------

Due to import/export functionality support (see below), cache for GNA plugin may be enabled via common ``:ref:`ov::cache_dir <doxid-group__ov__runtime__cpp__prop__api_1ga3276fc4ed7cc7d0bbdcf0ae12063728d>``` property of OpenVINO™.

For more details, see the :ref:`Model caching overview <model_caching_overview>`.

Import/Export
-------------

The GNA plugin supports import/export capability, which helps decrease first inference time significantly. The model compile target is the same as the execution target by default. If there is no GNA HW in the system, the default value for the execution target corresponds to available hardware or latest hardware version, supported by the plugin (i.e., GNA 3.0).

To export a model for a specific version of GNA HW, use the ``:ref:`ov::intel_gna::compile_target <doxid-group__ov__runtime__gna__prop__cpp__api_1gad9a766500212ccb6826b47aedde9e825>``` property and then export the model:

.. raw:: html

   <div class='sphinxtabset'>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="C++">





.. ref-code-block:: cpp

	std::ofstream ofs(blob_path, std::ios_base::binary | :ref:`std::ios::out <doxid-namespacengraph_1_1runtime_1_1reference_1ac9d07fc6d49867bb411a4f4132777aae>`);
	compiled_model.export_model(ofs);

.. raw:: html

   </div>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="Python">





.. ref-code-block:: cpp

	user_stream = compiled_model.export_model()
	with open(blob_path, 'wb') as f:
	    f.write(user_stream)

.. raw:: html

   </div>







.. raw:: html

   </div>



Import model:

.. raw:: html

   <div class='sphinxtabset'>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="C++">





.. ref-code-block:: cpp

	std::ifstream ifs(blob_path, std::ios_base::binary | std::ios_base::in);
	auto compiled_model = core.:ref:`import_model <doxid-classov_1_1_core_1a0d2853511bd7ba60cb591f4685b91884>`(ifs, "GNA");

.. raw:: html

   </div>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="Python">





.. ref-code-block:: cpp

	with open(blob_path, 'rb') as f:
	    buf = BytesIO(f.read())
	    compiled_model = core.import_model(buf, device_name="GNA")

.. raw:: html

   </div>







.. raw:: html

   </div>



To compile a model, use either :ref:`compile Tool <doxid-openvino_inference_engine_tools_compile_tool__r_e_a_d_m_e>` or :ref:`Speech C++ Sample <doxid-openvino_inference_engine_samples_speech_sample__r_e_a_d_m_e>`.

Stateful Models
---------------

GNA plugin natively supports stateful models. For more details on such models, refer to the :ref:`Stateful models <deploy_infer__stateful_models>`.

.. note::

   The GNA is typically used in streaming scenarios when minimizing latency is 
   important. Taking into account that POT does not support the ``TensorIterator`` 
   operation, the recommendation is to use the ``--transform`` option of the Model 
   Optimizer to apply ``LowLatency2`` transformation when converting an original model.





Profiling
---------

The GNA plugin allows turning on profiling, using the ``:ref:`ov::enable_profiling <doxid-group__ov__runtime__cpp__prop__api_1gafc5bef2fc2b5cfb5a0709cfb04346438>``` property. With the following methods, you can collect profiling information with various performance data about execution on GNA:

.. tab:: C++

   ``ov::InferRequest::get_profiling_info``

.. tab:: Python

   ``openvino.runtime.InferRequest.get_profiling_info``

The current GNA implementation calculates counters for the whole utterance scoring and does not provide per-layer information. The API enables you to retrieve counter units in cycles. You can convert cycles to seconds as follows:

.. ref-code-block:: cpp

	seconds = cycles / frequency

Refer to the table below to learn about the frequency of Intel® GNA inside a particular processor:

.. csv-table:: Frequency of Intel® GNA inside a particular processor
   :header: "Processor", "Frequency of Intel® GNA, MHz"

   "Intel® Core™ processors", 400
   "Intel® processors formerly codenamed Elkhart Lake", 200
   "Intel® processors formerly codenamed Gemini Lake", 200

Inference request performance counters provided for the time being:

* The number of total cycles spent on scoring in hardware, including compute and memory stall cycles

* The number of stall cycles spent in hardware

Supported Properties
~~~~~~~~~~~~~~~~~~~~

Read-write Properties
---------------------

In order to take effect, the following parameters must be set before model compilation or passed as additional arguments to ``:ref:`ov::Core::compile_model() <doxid-classov_1_1_core_1a46555f0803e8c29524626be08e7f5c5a>``` :

* :ref:`ov::cache_dir <doxid-group__ov__runtime__cpp__prop__api_1ga3276fc4ed7cc7d0bbdcf0ae12063728d>`

* :ref:`ov::enable_profiling <doxid-group__ov__runtime__cpp__prop__api_1gafc5bef2fc2b5cfb5a0709cfb04346438>`

* :ref:`ov::hint::inference_precision <doxid-group__ov__runtime__cpp__prop__api_1gad605a888f3c9b7598ab55023fbf44240>`

* ov::hint::num_requests

* :ref:`ov::intel_gna::compile_target <doxid-group__ov__runtime__gna__prop__cpp__api_1gad9a766500212ccb6826b47aedde9e825>`

* :ref:`ov::intel_gna::firmware_model_image_path <doxid-group__ov__runtime__gna__prop__cpp__api_1gafe83f57de302a35fa0d94563fab01e2d>`

* :ref:`ov::intel_gna::execution_target <doxid-group__ov__runtime__gna__prop__cpp__api_1ga4ecfa3938d07be52618f606bb54ac429>`

* :ref:`ov::intel_gna::pwl_design_algorithm <doxid-group__ov__runtime__gna__prop__cpp__api_1ga4b02b547bf360236e72ab5aa9c8d1d44>`

* :ref:`ov::intel_gna::pwl_max_error_percent <doxid-group__ov__runtime__gna__prop__cpp__api_1gaaf0afe1c01700ad7eed94783910c27fa>`

* :ref:`ov::intel_gna::scale_factors_per_input <doxid-group__ov__runtime__gna__prop__cpp__api_1gaf72daf77f0c085f54b0a84f77c3d7734>`

These parameters can be changed after model compilation ``:ref:`ov::CompiledModel::set_property <doxid-classov_1_1_compiled_model_1a9beec68aa25d6535e26fae5df00aaba0>``` :

* :ref:`ov::hint::performance_mode <doxid-group__ov__runtime__cpp__prop__api_1ga2691fe27acc8aa1d1700ad40b6da3ba2>`

* :ref:`ov::intel_gna::execution_mode <doxid-group__ov__runtime__gna__prop__cpp__api_1ga68ea397901af8f965863fbe599535341>`

* :ref:`ov::log::level <doxid-group__ov__runtime__cpp__prop__api_1gab4f55acc0df42391be3e9356ca0be7f8>`

Read-only Properties
--------------------

* :ref:`ov::available_devices <doxid-group__ov__runtime__cpp__prop__api_1gac4d3e86ef4fc43b1a80ec28c7be39ef1>`

* :ref:`ov::device::capabilities <doxid-group__ov__runtime__cpp__prop__api_1gadb13d62787fc4485733329f044987294>`

* :ref:`ov::device::full_name <doxid-group__ov__runtime__cpp__prop__api_1gaabacd9ea113b966be7b53b1d70fd6f42>`

* :ref:`ov::intel_gna::library_full_version <doxid-group__ov__runtime__gna__prop__cpp__api_1gae3d6b5080a37a65548ed411d3f6b00ca>`

* :ref:`ov::optimal_number_of_infer_requests <doxid-group__ov__runtime__cpp__prop__api_1ga087c6da667f7c3d8374aec5f6cbba027>`

* :ref:`ov::range_for_async_infer_requests <doxid-group__ov__runtime__cpp__prop__api_1ga3549425153790834c212d905b8216196>`

* :ref:`ov::supported_properties <doxid-group__ov__runtime__cpp__prop__api_1ga097f1274f26f3f4e1aa4fc3928748592>`

Limitations
~~~~~~~~~~~

Model and Operation Limitations
-------------------------------

Due to the specification of hardware architecture, Intel® GNA supports a limited set of operations (including their kinds and combinations). For example, GNA Plugin should not be expected to run computer vision models because the plugin does not fully support 2D convolutions. The exception are the models specifically adapted for the GNA Plugin.

Limitations include:

* Prior to GNA 3.0, only 1D convolutions are natively supported on the HW; 2D convolutions have specific limitations (see the table below).

* The number of output channels for convolutions must be a multiple of 4.

* The maximum number of filters is 65532 for GNA 2.0 and 8192 for GNA 3.0.

* *Transpose* layer support is limited to the cases where no data reordering is needed or when reordering is happening for two dimensions, at least one of which is not greater than 8.

* Splits and concatenations are supported for continuous portions of memory (e.g., split of 1,2,3,4 to 1,1,3,4 and 1,1,3,4 or concats of 1,2,3,4 and 1,2,3,5 to 2,2,3,4).

* For *Multiply*, *Add* and *Subtract* layers, auto broadcasting is only supported for constant inputs.

Support for 2D Convolutions
+++++++++++++++++++++++++++

The Intel® GNA 1.0 and 2.0 hardware natively supports only 1D convolutions. However, 2D convolutions can be mapped to 1D when a convolution kernel moves in a single direction.

Initially, a limited subset of Intel® GNA 3.0 features are added to the previous feature set including the following:

* **2D VALID Convolution With Small 2D Kernels:** Two-dimensional convolutions with the following kernel dimensions [``H``, ``W``] are supported: [1,1], [2,2], [3,3], [2,1], [3,1], [4,1], [5,1], [6,1], [7,1], [1,2], or [1,3]. Input tensor dimensions are limited to [1,8,16,16] <= [``N``, ``C``, ``H``, ``W``] <= [1,120,384,240]. Up to 384 ``C`` channels may be used with a subset of kernel sizes (see the table below). Up to 256 kernels (output channels) are supported. Pooling is limited to pool shapes of [1,1], [2,2], or [3,3]. Not all combinations of kernel shape and input tensor shape are supported (see the tables below for exact limitations).

The tables below show that the exact limitation on the input tensor width W depends on the number of input channels *C* (indicated as *Ci* below) and the kernel shape. There is much more freedom to choose the input tensor height and number of output channels.

The following tables provide a more explicit representation of the Intel(R) GNA 3.0 2D convolution operations initially supported. The limits depend strongly on number of input tensor channels (*Ci*) and the input tensor width (*W*). Other factors are kernel height (*KH*), kernel width (*KW*), pool height (*PH*), pool width (*PW*), horizontal pool step (*SH*), and vertical pool step (*PW*). For example, the first table shows that for a 3x3 kernel with max pooling, only square pools are supported, and *W* is limited to 87 when there are 64 input channels.

:download:`Table of Maximum Input Tensor Widths (W) vs. Rest of Parameters (Input and Kernel Precision: i16) <../../../docs/OV_Runtime_UG/supported_plugins/files/GNA_Maximum_Input_Tensor_Widths_i16.csv>`

:download:`Table of Maximum Input Tensor Widths (W) vs. Rest of Parameters (Input and Kernel Precision: i8) <../../../docs/OV_Runtime_UG/supported_plugins/files/GNA_Maximum_Input_Tensor_Widths_i8.csv>`

.. note::

   The above limitations only apply to the new hardware 2D convolution operation. 
   When possible, the Intel® GNA plugin graph compiler flattens 2D convolutions so 
   that the second generation Intel® GNA 1D convolution operations (without these 
   limitations) may be used. The plugin will also flatten 2D convolutions regardless 
   of the sizes if GNA 2.0 compilation target is selected (see below).





Support for 2D Convolutions using POT
+++++++++++++++++++++++++++++++++++++

For POT to successfully work with the models including GNA3.0 2D convolutions, the following requirements must be met:

* All convolution parameters are natively supported by HW (see tables above).

* The runtime precision is explicitly set by the ``:ref:`ov::hint::inference_precision <doxid-group__ov__runtime__cpp__prop__api_1gad605a888f3c9b7598ab55023fbf44240>``` property as ``i8`` for the models produced by the ``performance mode`` of POT, and as ``i16`` for the models produced by the ``accuracy mode`` of POT.

Batch Size Limitation
---------------------

Intel® GNA plugin supports the processing of context-windowed speech frames in batches of 1-8 frames.

Refer to the :ref:`Layout API overview <deploy_infer__layout_api_overview>` to determine batch dimension.

To set layout of model inputs in runtime, use the :ref:`Optimize Preprocessing <deploy_infer__preprocessing_overview>` guide:

.. raw:: html

   <div class='sphinxtabset'>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="C++">





.. ref-code-block:: cpp

	#include <openvino/openvino.hpp>



.. ref-code-block:: cpp

	:ref:`ov::preprocess::PrePostProcessor <doxid-classov_1_1preprocess_1_1_pre_post_processor>` ppp(:ref:`model <doxid-group__ov__runtime__cpp__prop__api_1ga461856fdfb6d7533dc53355aec9e9fad>`);
	for (const auto& input : :ref:`model <doxid-group__ov__runtime__cpp__prop__api_1ga461856fdfb6d7533dc53355aec9e9fad>`->inputs()) {
	    auto& in = ppp.input(input.get_any_name());
	    in.model().set_layout(:ref:`ov::Layout <doxid-classov_1_1_layout>`("N?"));
	}
	:ref:`model <doxid-group__ov__runtime__cpp__prop__api_1ga461856fdfb6d7533dc53355aec9e9fad>` = ppp.build();

.. raw:: html

   </div>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="Python">





.. ref-code-block:: cpp

	from openvino.runtime import Core, set_batch
	from openvino.preprocess import PrePostProcessor



.. ref-code-block:: cpp

	ppp = PrePostProcessor(model)
	for i in :ref:`range <doxid-namespacengraph_1_1runtime_1_1reference_1ad38dec78131946cded583cc1154a406d>`(len(model.inputs)):
	    input_name = model.input(i).get_any_name()
	    ppp.input(i).:ref:`model <doxid-group__ov__runtime__cpp__prop__api_1ga461856fdfb6d7533dc53355aec9e9fad>`().:ref:`set_layout <doxid-group__ov__layout__cpp__api_1ga18464fb8ed029acb5fdc2bb1737358d9>`("N?")
	model = ppp.build()

.. raw:: html

   </div>







.. raw:: html

   </div>

then set batch size:

.. raw:: html

   <div class='sphinxtabset'>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="C++">





.. ref-code-block:: cpp

	:ref:`ov::set_batch <doxid-namespaceov_1a3314e2ff91fcc9ffec05b1a77c37862b>`(:ref:`model <doxid-group__ov__runtime__cpp__prop__api_1ga461856fdfb6d7533dc53355aec9e9fad>`, batch_size);

.. raw:: html

   </div>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="Python">





.. ref-code-block:: cpp

	:ref:`set_batch <doxid-namespaceov_1a3314e2ff91fcc9ffec05b1a77c37862b>`(model, batch_size)

.. raw:: html

   </div>







.. raw:: html

   </div>

Increasing batch size only improves efficiency of ``MatMul`` layers.

.. note::

   For models with ``Convolution``, ``LSTMCell``, or ``ReadValue`` / ``Assign`` 
   operations, the only supported batch size is 1.





Compatibility with Heterogeneous mode
-------------------------------------

:ref:`Heterogeneous execution <deploy_infer__hetero_plugin>` is currently not supported by GNA plugin.

See Also
~~~~~~~~

* :ref:`Supported Devices <doxid-openvino_docs__o_v__u_g_supported_plugins__supported__devices>`

* :ref:`Converting Model <doxid-openvino_docs__m_o__d_g_prepare_model_convert_model__converting__model>`

* :ref:`Convert model from Kaldi <doxid-openvino_docs__m_o__d_g_prepare_model_convert_model__convert__model__from__kaldi>`

