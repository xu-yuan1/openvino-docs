.. index:: pair: page; General Optimizations
.. _deployment_general_optimizations:

.. meta::
   :description: General optimizations include application-level optimization 
                 methods that improve data pipelining, pre-processing 
                 acceleration and both latency and throughput.
   :keywords: runtime inference optimizations, deployment optimizations, 
              latency, throughput, performance optimization, Synchronous 
              API, Model Optimizer, asynchronous execution, synchronous 
              execution, input tensor, output tensor, get_tensor, Asynchronous
              API, OpenVINO Async API, remote tensors API, GPU plugin,
              model inference, Intel VTune

General Optimizations
=====================

:target:`deployment_general_optimizations_1md_openvino_docs_optimization_guide_dldt_deployment_optimization_common` 

This article covers application-level optimization techniques, such as 
asynchronous execution, to improve data pipelining, pre-processing acceleration 
and so on. While the techniques (e.g. pre-processing) can be specific to 
end-user applications, the associated performance improvements are general and 
shall improve any target scenario both latency and throughput.

:target:`deployment_general_optimizations_1inputs_pre_processing`

Inputs Pre-Processing with OpenVINO
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In many cases, a network expects a pre-processed image. It is advised not to 
perform any unnecessary steps in the code:

* Model Optimizer can efficiently incorporate the mean and normalization 
  (scale) values into a model (for example, to the weights of the first 
  convolution). For more details, see the 
  :ref:`relevant Model Optimizer command-line options <doxid-openvino_docs__m_o__d_g__additional__optimization__use__cases>`.

* Let OpenVINO accelerate other means of 
  :ref:`Image Pre-processing and Conversion <doxid-openvino_docs__o_v__u_g__preprocessing__overview>`.

* Data which is already in the "on-device" memory can be input directly by 
  using the :ref:`remote tensors API of the GPU Plugin <doxid-openvino_docs__o_v__u_g_supported_plugins__g_p_u__remote_tensor__a_p_i>`.

:target:`deployment_general_optimizations_1async_api`

Prefer OpenVINO Async API
~~~~~~~~~~~~~~~~~~~~~~~~~

The API of the inference requests offers Sync and Async execution. While the 
``:ref:`ov::InferRequest::infer() <doxid-classov_1_1_infer_request_1abcb7facc9f7c4b9226a1fd343e56958d>``` 
is inherently synchronous and executes immediately (effectively serializing the 
execution flow in the current application thread), the Async "splits" the 
``infer()`` into ``:ref:`ov::InferRequest::start_async() <doxid-classov_1_1_infer_request_1a5a05ae4352f804c865e11f5d68b983d5>``` 
and ``:ref:`ov::InferRequest::wait() <doxid-classov_1_1_infer_request_1ab0e0739da45789d816f8b5584a0b5691>```. 
For more information, see the :ref:`API examples <openvino_inference_request>`.

A typical use case for the 
``:ref:`ov::InferRequest::infer() <doxid-classov_1_1_infer_request_1abcb7facc9f7c4b9226a1fd343e56958d>``` 
is running a dedicated application thread per source of inputs (e.g. a camera), 
so that every step (frame capture, processing, parsing the results, and 
associated logic) is kept serial within the thread. In contrast, the 
``:ref:`ov::InferRequest::start_async() <doxid-classov_1_1_infer_request_1a5a05ae4352f804c865e11f5d68b983d5>``` 
and ``:ref:`ov::InferRequest::wait() <doxid-classov_1_1_infer_request_1ab0e0739da45789d816f8b5584a0b5691>``` 
allow the application to continue its activities and poll or wait for the 
inference completion when really needed. Therefore, one reason for using an 
asynchronous code is "efficiency".

.. note:: Although the Synchronous API can be somewhat easier to start with, prefer 
   to use the Asynchronous (callbacks-based, below) API in the production code. 
   The reason is that it is the most general and scalable way to implement the 
   flow control for any possible number of requests (and hence both latency and throughput scenarios).

The key advantage of the Async approach is that when a device is busy with the 
inference, the application can do other things in parallel (e.g. populating 
inputs or scheduling other requests) rather than wait for the current 
inference to complete first.

In the example below, inference is applied to the results of the video decoding. 
It is possible to keep two parallel infer requests, and while the current one 
is processed, the input frame for the next one is being captured. This 
essentially hides the latency of capturing, so that the overall frame rate is 
rather determined only by the slowest part of the pipeline (decoding vs 
inference) and not by the sum of the stages.

Below are example-codes for the regular and async-based approaches to compare:

* Normally, the frame is captured with OpenCV and then immediately processed:

.. ref-code-block:: cpp

   while(true) {
       // capture frame
       // populate CURRENT InferRequest
       // Infer CURRENT InferRequest //this call is synchronous
       // display CURRENT result
   }

.. image:: ./_assets/vtune_regular.png
   :alt: Intel VTune screenshot

* In the "true" async mode, the ``NEXT`` request is populated in the main 
  (application) thread, while the ``CURRENT`` request is processed:

.. ref-code-block:: cpp

   while(true) {
       // capture frame
       // populate NEXT InferRequest
       // start NEXT InferRequest //this call is async and returns immediately
       
       // wait for the CURRENT InferRequest
       // display CURRENT result
       // swap CURRENT and NEXT InferRequests
   }

.. image:: ./_assets/vtune_async.png
   :alt: Intel VTune screenshot

The technique can be generalized to any available parallel slack. For example, 
you can do inference and simultaneously encode the resulting or previous 
frames or run further inference, like emotion detection on top of the face 
detection results. Refer to the Object Detection C++ Demo, Object Detection 
Python Demo(latency-oriented Async API showcase) and 
:ref:`Benchmark App Sample <doxid-openvino_inference_engine_samples_benchmark_app__r_e_a_d_m_e>` 
for complete examples of the Async API in action.

.. note:: Using the Asynchronous API is a must for 
   :ref:`throughput-oriented scenarios <deployment_optimizing_for_throughput>`.

Notes on Callbacks
------------------

Keep in mind that the ``:ref:`ov::InferRequest::wait() <doxid-classov_1_1_infer_request_1ab0e0739da45789d816f8b5584a0b5691>``` 
of the Async API waits for the specific request only. However, running multiple 
inference requests in parallel provides no guarantees on the completion order. 
This may complicate a possible logic based on the 
``:ref:`ov::InferRequest::wait <doxid-classov_1_1_infer_request_1ab0e0739da45789d816f8b5584a0b5691>```. 
The most scalable approach is using callbacks (set via the 
``:ref:`ov::InferRequest::set_callback <doxid-classov_1_1_infer_request_1afba2a10162ab356728ec8901973e8f02>```) 
that are executed upon completion of the request. The callback functions will 
be used by OpenVINO Runtime to notify you of the results (or errors). This is 
a more event-driven approach.

A few important points on the callbacks:

* It is the job of the application to ensure that any callback function is 
  thread-safe.

* Although executed asynchronously by a dedicated threads, the callbacks 
  should NOT include heavy operations (e.g. I/O) and/or blocking calls. 
  Work done by any callback should be kept to a minimum.

:target:`deployment_general_optimizations_1tensor_idiom`

The "get_tensor" Idiom
~~~~~~~~~~~~~~~~~~~~~~

Each device within OpenVINO may have different internal requirements on the 
memory padding, alignment, etc., for intermediate tensors. The 
**input/output tensors** are also accessible by the application code. As every 
``:ref:`ov::InferRequest <doxid-classov_1_1_infer_request>``` is created by the 
particular instance of the ``:ref:`ov::CompiledModel <doxid-classov_1_1_compiled_model>``` 
(that is already device-specific) the requirements are respected and the 
input/output tensors of the requests are still device-friendly. To sum it up:

* The ``get_tensor`` (that offers the ``data()`` method to get a system-memory 
  pointer to the content of a tensor), is a recommended way to populate the 
  inference inputs (and read back the outputs) **from/to the host memory** :

  * For example, for the GPU device, the **input/output tensors** are mapped to 
    the host (which is fast) only when the ``get_tensor`` is used, while for 
    the ``set_tensor`` a copy into the internal GPU structures may happen.

* In contrast, when the input tensors are already in the **on-device memory** 
  (e.g. as a result of the video-decoding), prefer the ``set_tensor`` as a 
  zero-copy way to proceed. For more details, see the 
  :ref:`GPU device Remote tensors API <doxid-openvino_docs__o_v__u_g_supported_plugins__g_p_u__remote_tensor__a_p_i>`.

Consider the :ref:`API examples <openvino_inference_request_1in_out_tensors>` 
for the ``get_tensor`` and ``set_tensor``.
