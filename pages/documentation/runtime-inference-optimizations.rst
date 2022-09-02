.. index:: pair: page; Runtime Inference Optimizations
.. _optim_perf__runtime_inference_optim:

.. meta::
   :description: Runtime optimizations are highly device-specific and improve 
                 execution means and inference parameters, typically trading 
                 accuracy for performance. 
   :keywords: runtime inference optimizations, deployment optimizations, 
              inference precision, inference_precision, latency, throughput,
              OpenVINO Runtime, performance optimization, model configuration,
              GPU-oriented optimizations, Performance Hints, batching, streams


Runtime Inference Optimizations
===============================

:target:`optim_perf__runtime_inference_optim_1md_openvino_docs_optimization_guide_dldt_deployment_optimization_guide`

.. toctree::
   :maxdepth: 1
   :hidden:

   ./runtime-inference-optimizations/general-optimizations
   ./runtime-inference-optimizations/optimizing-for-latency
   ./runtime-inference-optimizations/optimizing-for-throughput
   ./runtime-inference-optimizations/advanced-throughput-options
   ./runtime-inference-optimizations/further-low-level-implementation

Runtime optimizations, or deployment optimizations, focus on tuning inference 
parameters and execution means (e.g., the optimum number of requests executed 
simultaneously). Unlike model-level optimizations, they are highly specific to 
the hardware and case they are used for, and often come at a cost. 
``:ref:`ov::hint::inference_precision <doxid-group__ov__runtime__cpp__prop__api_1gad605a888f3c9b7598ab55023fbf44240>``` 
is a "typical runtime configuration" which trades accuracy for performance, 
allowing ``fp16/bf16`` execution for the layers that remain in ``fp32`` after 
quantization of the original ``fp32`` model.

Therefore, optimization should start with defining the use case. For example, 
if it is about processing millions of samples by overnight jobs in data 
centers, throughput could be prioritized over latency. On the other hand, 
real-time usages would likely trade off throughput to deliver the results at 
minimal latency. A combined scenario is also possible, targeting the highest 
possible throughput, while maintaining a specific latency threshold.

It is also important to understand how the full-stack application would use 
the inference component "end-to-end." For example, to know what stages need to 
be orchestrated to save workload devoted to fetching and preparing input data.

For more information on this topic, see the following articles:

* :ref:`feature support by device <deploy_infer__working_with_devices_1features_support_matrix>`,

* :ref:`Inputs Pre-processing with the OpenVINO <optim_perf__deploy_general_optim_1inputs_pre_processing>`.

* :ref:`Async API <optim_perf__deploy_general_optim_1async_api>`.

* :ref:`The 'get_tensor' Idiom <optim_perf__deploy_general_optim_1tensor_idiom>`.

* For variably-sized inputs, consider :ref:`dynamic shapes <deploy_infer__dynamic_shapes>`.

See the :ref:`latency <optim_perf__deploy_optim_latency>` 
and :ref:`throughput <optim_perf__deploy_optim_throughput>` optimization guides, for **use-case-specific optimizations**

Writing Performance-Portable Inference Applications
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Although inference performed in OpenVINO Runtime can be configured with a 
multitude of low-level performance settings, it is not recommended in most 
cases. Firstly, achieving the best performance with such adjustments requires 
deep understanding of device architecture and the inference engine.

Secondly, such optimization may not translate well to other device-model 
combinations. In other words, one set of execution parameters is likely to 
result in different performance when used under different conditions. 
For example:

* both the CPU and GPU support the notion of 
  :ref:`streams <optim_perf__deploy_throughput_adv>`, 
  yet they deduce their optimal number very differently.

* Even among devices of the same type, different execution configurations can 
  be considered optimal, as in the case of instruction sets or the number of 
  cores for the CPU and the batch size for the GPU.

* Different models have different optimal parameter configurations, 
  considering factors such as compute vs memory-bandwidth, inference precision, 
  and possible model quantization.

* Execution "scheduling" impacts performance strongly and is highly 
  device-specific, for example, GPU-oriented optimizations like batching, 
  combining multiple inputs to achieve the optimal throughput, 
  :ref:`do not always map well to the CPU <optim_perf__deploy_low_level_implement>`.

To make the configuration process much easier and its performance optimization 
more portable, the option of :ref:`Performance Hints <deploy_infer__performance_hints>` 
has been introduced. It comprises two high-level "presets" focused on either 
**latency** or **throughput** and, essentially, makes execution specifics irrelevant.

The Performance Hints functionality makes configuration transparent to the 
application, for example, anticipates the need for explicit (application-side) 
batching or streams, and facilitates parallel processing of separate infer 
requests for different input sources

Additional Resources
~~~~~~~~~~~~~~~~~~~~

* :ref:`Using Async API and running multiple inference requests in parallel to leverage throughput <optim_perf__deploy_optim_throughput_1throughput_app_design>`.

* :ref:`The throughput approach implementation details for specific devices <optim_perf__deploy_low_level_implement>`

* :ref:`Details on throughput <optim_perf__deploy_optim_throughput>`

* :ref:`Details on latency <optim_perf__deploy_optim_latency>`

* :ref:`API examples and details <deploy_infer__performance_hints>`.
