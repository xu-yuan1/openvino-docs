.. index:: pair: page; Optimizing for the Latency
.. _deployment_optimizing_for_latency:

.. meta::
   :description: OpenVINO provides methods that help to preserve minimal 
                 latency despite the number of inference requests and 
                 improve throughput without degrading latency.
   :keywords: OpenVINO, throughput, latency, low latency, CPU plugin, 
              GPU plugin, Performance Hints, first-inference latency,
              model inference, high-level performance hints, inference
              mode, AUTO device selection, model caching, inference 
              performance, improving latency, optimizing latency

Optimizing for the Latency
==========================

:target:`deployment_optimizing_for_latency_1md_openvino_docs_optimization_guide_dldt_deployment_optimization_latency`

.. toctree::
   :maxdepth: 1
   :hidden:

   ./optimizing-for-latency/model-caching-overview

A significant portion of deep learning use cases involve applications loading 
a single model and using a single input at a time, which is the of typical 
"consumer" scenario. While an application can create more than one request if 
needed, for example to support :ref:`asynchronous inputs population <deployment_general_optimizations_1async_api>`, 
its **inference performance depends on how many requests are being inferred in parallel** 
on a device.

Similarly, when multiple models are served on the same device, it is important 
whether the models are executed simultaneously or in a chain, for example, in 
the inference pipeline. As expected, the easiest way to achieve **low latency 
is by running only one inference at a time** on one device. Accordingly, any 
additional concurrency usually results in latency rising fast.

However, some conventional "root" devices (i.e., CPU or GPU) can be in fact 
internally composed of several "sub-devices". In many cases, letting OpenVINO 
leverage the "sub-devices" transparently helps to improve application's 
throughput (e.g., serve multiple clients simultaneously) without degrading 
latency. For example, multi-socket CPUs can deliver as many requests at the 
same minimal latency as there are NUMA nodes in the system. Similarly, a 
multi-tile GPU, which is essentially multiple GPUs in a single package, can 
deliver a multi-tile scalability with the number of inference requests, while 
preserving the single-tile latency.

Typically, human expertise is required to get more "throughput" out of the 
device, even in the inherently latency-oriented cases. OpenVINO can take this 
configuration burden via :ref:`high-level performance hints <doxid-openvino_docs__o_v__u_g__performance__hints>`, 
the ``:ref:`ov::hint::PerformanceMode::LATENCY <doxid-group__ov__runtime__cpp__prop__api_1gga032aa530efa40760b79af14913d48d73a501069dd75f76384ba18f133fdce99c2>``` 
specified for the ``:ref:`ov::hint::performance_mode <doxid-group__ov__runtime__cpp__prop__api_1ga2691fe27acc8aa1d1700ad40b6da3ba2>``` 
property for the ``compile_model``.

.. note:: :ref:`OpenVINO performance hints <doxid-openvino_docs__o_v__u_g__performance__hints>` 
   is a recommended way for performance configuration, which is both device-agnostic and future-proof.

When multiple models are to be used simultaneously, consider running inference 
on separate devices for each of them. Finally, when multiple models are 
executed in parallel on a device, using additional 
``:ref:`ov::hint::model_priority <doxid-group__ov__runtime__cpp__prop__api_1ga3663a3976ff7c4bdc3ccdb9ce44945ce>``` 
may help to define relative priorities of the models. Refer to the documentation 
on the :ref:`matrix features support for OpenVINO devices <doxid-openvino_docs__o_v__u_g__working_with_devices_1features_support_matrix>` 
to check if your device supports the feature.

**First-Inference Latency and Model Load/Compile Time**

In some cases, model loading and compilation contribute to the "end-to-end" 
latency more than usual. For example, when the model is used exactly once, or 
when it is unloaded and reloaded in a cycle, to free the memory for another 
inference due to on-device memory limitations.

Such a "first-inference latency" scenario may pose an additional limitation on 
the model load\compilation time, as inference accelerators (other than the CPU) 
usually require a certain level of model compilation upon loading. The 
:ref:`model caching <model_caching_overview>` 
option is a way to lessen the impact over multiple application runs. If model 
caching is not possible, for example, it may require write permissions for the 
application, the CPU offers the fastest model load time almost every time.

Another way of dealing with first-inference latency is using the 
:ref:`AUTO device selection inference mode <doxid-openvino_docs__o_v__u_g_supported_plugins__a_u_t_o>`. 
It starts inference on the CPU, while waiting for the actual accelerator to 
load the model. At that point, it shifts to the new device seamlessly.

Finally, note that any :ref:`throughput-oriented options <deployment_optimizing_for_throughput>` 
may significantly increase the model uptime.
