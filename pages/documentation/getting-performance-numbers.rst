.. index:: pair: page; Getting Performance Numbers
.. _getting_performance_numbers:

.. meta::
   :description: Using the benchmark_app tool to test inference performance. Detailed insights 
                 into performance breakdown with performance counters and execution graphs.
   :keywords: benchmark, benchmark_app, ITT, Intel® VTune™ Profiler, performance numbers, 
              testing performance, performance counters, execution graphs, OpenVINO Runtime,
              OpenVINO IR, throughput, latency, performance hints, GPU plugin, CPU plugin, 
              inference, inference performance, I8, FP32, 8-bit precision, 32-bit precision


Getting Performance Numbers
===========================

:target:`getting_performance_numbers_1md_openvino_docs_mo_dg_prepare_model_getting_performance_numbers` 

This guide introduces things to notice and how to use the benchmark_app to get 
performance numbers. It also explains how the performance numbers are reflected 
through internal inference performance counters and execution graphs. In the 
last section, it includes information on using ITT and Intel® VTune™ Profiler 
to get performance insights.

Tip 1: Select Proper Set of Operations to Measure
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When evaluating the performance of a model with OpenVINO Runtime, it is required 
to measure proper set of operations. Remember the following tips:

* Avoid including one-time costs such as model loading.

* Track operations that occur outside OpenVINO Runtime (such as video decoding) separately.

.. note:: Some image pre-processing can be baked into OpenVINO IR and accelerated 
   accordingly. For more information, refer to 
   :ref:`Embedding the Pre-processing <doxid-openvino_docs__m_o__d_g__additional__optimization__use__cases>` 
   and `General Runtime Optimizations <../../optimization_guide/dldt_deployment_optimization_common>`__.


Tip 2: Try to Get Credible Data
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Performance conclusions should be build upon reproducible data. As for the 
performance measurements, they should be done with a large number of invocations 
of the same routine. Since the first iteration is almost always significantly 
slower than the subsequent ones, an aggregated value can be used for the execution 
time for final projections:

* If the warm-up run does not help or execution time still varies, you can try 
  running a large number of iterations and then average or find a mean of the results.

* If the time values range too much, consider geomean.

* Be aware of the throttling and other power oddities. A device can exist in one 
  of several different power states. When optimizing your model, consider fixing 
  the device frequency for better performance data reproducibility. However, the 
  end-to-end (application) benchmarking should also be performed under real 
  operational conditions.

Using benchmark_app to Measure Reference Performance Numbers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To get performance numbers, use the dedicated :ref:`OpenVINO Benchmark app <doxid-openvino_inference_engine_samples_benchmark_app__r_e_a_d_m_e>` sample, which is the most-recommended solution to produce performance reference. It includes a lot of device-specific knobs, but the primary usage is as simple as in the following command to measure the performance of the model on GPU:

.. ref-code-block:: cpp

	$ ./benchmark_app –d GPU –m <model> -i <input>

to measure the performance of the model on the GPU. Or

.. ref-code-block:: cpp

	$ ./benchmark_app –d CPU –m <model> -i <input>

to execute on the CPU instead.

Each of the :ref:`OpenVINO supported devices <doxid-openvino_docs__o_v__u_g_supported_plugins__supported__devices>` offers performance settings that contain command-line equivalents in the :ref:`Benchmark app <doxid-openvino_inference_engine_samples_benchmark_app__r_e_a_d_m_e>`. While these settings provide really low-level control and allow leveraging the optimal model performance on the *specific* device, it is recommended to always start the performance evaluation with the :ref:`OpenVINO High-Level Performance Hints <doxid-openvino_docs__o_v__u_g__performance__hints>` first:

* benchmark_app **-hint tput** -d 'device' -m 'path to your model'

* benchmark_app **-hint latency** -d 'device' -m 'path to your model'

Notes for Comparing Performance with Native/Framework Code
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When comparing the OpenVINO Runtime performance with the framework or another 
reference code, make sure that both versions are as similar as possible:

* Wrap the exact inference execution (refer to the 
  :ref:`Benchmark app <doxid-openvino_inference_engine_samples_benchmark_app__r_e_a_d_m_e>` 
  for examples).

* Do not include model loading time.

* Ensure that the inputs are identical for OpenVINO Runtime and the framework. 
  For example, watch out for random values that can be used to populate the inputs.

* In situations when any user-side pre-processing should be tracked separately, 
  consider :ref:`image pre-processing and conversion <deploy_infer__preprocessing_overview>`.

* When applicable, leverage the :ref:`Dynamic Shapes support <doxid-openvino_docs__o_v__u_g__dynamic_shapes>`.

* If possible, demand the same accuracy. For example, TensorFlow allows ``FP16`` 
  execution, so when comparing to that, make sure to test the OpenVINO Runtime with the ``FP16`` as well.

.. _performance-counters:

Data from Internal Inference Performance Counters and Execution Graphs
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

More detailed insights into inference performance breakdown can be achieved with 
device-specific performance counters and/or execution graphs. Both 
:ref:`C++ <doxid-openvino_inference_engine_samples_benchmark_app__r_e_a_d_m_e>` 
and :ref:`Python <doxid-openvino_inference_engine_tools_benchmark_tool__r_e_a_d_m_e>` 
versions of the ``benchmark_app`` support a ``-pc`` command-line parameter that 
outputs internal execution breakdown.

For example, the table shown below is the part of performance counters for quantized 
`TensorFlow implementation of ResNet-50 <https://github.com/openvinotoolkit/open_model_zoo/tree/master/models/public/resnet-50-tf>`__ 
model inference on :ref:`CPU Plugin <deploy_infer__cpu_device>`. 
Keep in mind that since the device is CPU, the ``realTime`` wall clock and the 
``cpu`` time layers are the same. Information about layer precision is also 
stored in the performance counters.

.. list-table::
    :header-rows: 1

    * - layerName
      - execStatus
      - layerType
      - execType
      - realTime (ms)
      - cpuTime (ms)
    * - resnet_model/batch_normalization_15/FusedBatchNorm/Add
      - EXECUTED
      - Convolution
      - jit_avx512_1x1_I8
      - 0.377
      - 0.377
    * - resnet_model/conv2d_16/Conv2D/fq_input_0
      - NOT_RUN
      - FakeQuantize
      - undef
      - 0
      - 0
    * - resnet_model/batch_normalization_16/FusedBatchNorm/Add
      - EXECUTED
      - Convolution
      - jit_avx512_I8
      - 0.499
      - 0.499
    * - resnet_model/conv2d_17/Conv2D/fq_input_0
      - NOT_RUN
      - FakeQuantize
      - undef
      - 0
      - 0
    * - resnet_model/batch_normalization_17/FusedBatchNorm/Add
      - EXECUTED
      - Convolution
      - jit_avx512_1x1_I8
      - 0.399
      - 0.399
    * - resnet_model/add_4/fq_input_0
      - NOT_RUN
      - FakeQuantize
      - undef
      - 0
      - 0
    * - resnet_model/add_4
      - NOT_RUN
      - Eltwise
      - undef
      - 0
      - 0
    * - resnet_model/add_5/fq_input_1
      - NOT_RUN
      - FakeQuantize
      - undef
      - 0
      - 0

The ``exeStatus`` column of the table includes the following possible values:

* ``EXECUTED`` - the layer was executed by standalone primitive.

* ``NOT_RUN`` - the layer was not executed by standalone primitive or was fused 
  with another operation and executed in another layer primitive.

The ``execType`` column of the table includes inference primitives with specific 
suffixes. The layers could have the following marks:

* The ``I8`` suffix is for layers that had 8-bit data type input and were computed 
  in 8-bit precision.

* The ``FP32`` suffix is for layers computed in 32-bit precision.

All ``Convolution`` layers are executed in ``int8`` precision. The rest of the 
layers are fused into Convolutions using post-operation optimization, as described 
in :ref:`CPU Device <deploy_infer__cpu_device>`. 
This contains layer names (as seen in OpenVINO IR), type of the layer, and 
execution statistics.

Both ``benchmark_app`` versions also support the ``exec_graph_path`` command-line 
option. It requires OpenVINO to output the same execution statistics per layer, 
but in the form of plugin-specific `Netron-viewable <https://netron.app/>`__ 
graph to the specified file.

Especially when performance-debugging the 
:ref:`latency <deployment_optimizing_for_latency>`, 
note that the counters do not reflect the time spent in the 
``plugin/device/driver/etc`` queues. If the sum of the counters is too different 
from the latency of an inference request, consider testing with less inference 
requests. For example, running single 
:ref:`OpenVINO stream <deployment_optimizing_for_throughput>` 
with multiple requests would produce nearly identical counters as running a 
single inference request, while the actual latency can be quite different.

Lastly, the performance statistics with both performance counters and execution 
graphs are averaged, so such data for the 
:ref:`inputs of dynamic shapes <doxid-openvino_docs__o_v__u_g__dynamic_shapes>` 
should be measured carefully, preferably by isolating the specific shape and 
executing multiple times in a loop, to gather the reliable data.

Using ITT to Get Performance Insights
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In general, OpenVINO and its individual plugins are heavily instrumented with 
Intel® Instrumentation and Tracing Technology (ITT). Therefore, you can also 
compile OpenVINO from the source code with ITT enabled and use tools like 
`Intel® VTune™ Profiler <https://software.intel.com/en-us/vtune>`__ to get 
detailed inference performance breakdown and additional insights in the 
application-level performance on the timeline view.
