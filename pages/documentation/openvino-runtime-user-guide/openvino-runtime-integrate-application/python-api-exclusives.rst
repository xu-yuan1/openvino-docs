.. index:: pair: page; OpenVINO™ Python API Exclusives
.. _deploy_infer__python_api_exclusives:

.. meta::
   :description: OpenVINO™ Runtime Python API includes additional features to 
                 improve user experience and provide simple yet powerful tool 
                 for Python users.
   :keywords: OpenVINO™ Runtime, OpenVINO™ Runtime Python API, Python API, inference, 
              model inference, CompiledModel, tensor, numpy array, Shared Memory Mode, 
              synchronous inference mode, asynchronous inference mode, AsyncInferQueue, 
              setting callbacks, low precision element types, u1, u4, i4, element type, 
              u1 element type, u4 element type, i4 element type, GIL, Global Lock Interpreter


OpenVINO™ Python API Exclusives
=================================

:target:`deploy_infer__python_api_exclusives_1md_openvino_docs_ov_runtime_ug_python_api_exclusives` 

OpenVINO™ Runtime Python API offers additional features and helpers to enhance 
user experience. The main goal of Python API is to provide user-friendly and 
simple yet powerful tool for Python users.

Easier Model Compilation
~~~~~~~~~~~~~~~~~~~~~~~~

``CompiledModel`` can be easily created with the helper method. It hides the 
creation of ``Core`` and applies ``AUTO`` inference mode by default.

.. ref-code-block:: cpp

   import openvino.runtime as ov

   compiled_model = ov.compile_model("model.xml")

Model/CompiledModel Inputs and Outputs
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Besides functions aligned to C++ API, some of them have their Python 
counterparts or extensions. For example, ``Model`` and ``CompiledModel`` 
inputs/outputs can be accessed via properties.

.. ref-code-block:: cpp

   core = :ref:`ov.Core <doxid-classov_1_1_core>`()

   input_a = ov.opset8.parameter([8])
   res = ov.opset8.absolute(input_a)
   model = :ref:`ov.Model <doxid-classov_1_1_model>`(res, [input_a])
   compiled = core.compile_model(model, "CPU")

   print(model.inputs)
   print(model.outputs)

   print(compiled.inputs)
   print(compiled.outputs)

Refer to Python API documentation on which helper functions or properties are 
available for different classes.

Working with Tensor
~~~~~~~~~~~~~~~~~~~

Python API allows passing data as tensors. The ``Tensor`` object holds a copy 
of the data from the given array. The ``dtype`` of *numpy* arrays is converted 
to OpenVINO™ types automatically.

.. ref-code-block:: cpp

   data_float64 = np.ones(shape=(2,8))

   tensor = :ref:`ov.Tensor <doxid-classov_1_1_tensor>`(data_float64)
   assert tensor.element_type == ov.Type.f64

   data_int32 = np.ones(shape=(2,8), dtype=np.int32)

   tensor = :ref:`ov.Tensor <doxid-classov_1_1_tensor>`(data_int32)
   assert tensor.element_type == ov.Type.i32

Shared Memory Mode
------------------

``Tensor`` objects can share the memory with *numpy* arrays. By specifying the 
``shared_memory`` argument, the ``Tensor`` object does not copy data. Instead, 
it has access to the memory of the *numpy* array.

.. ref-code-block:: cpp

   data_to_share = np.ones(shape=(2,8))

   shared_tensor = :ref:`ov.Tensor <doxid-classov_1_1_tensor>`(data_to_share, shared_memory=True)

   # Editing of the numpy array affects Tensor's data
   data_to_share[0][2] = 6.0
   assert shared_tensor.data[0][2] == 6.0

   # Editing of Tensor's data affects the numpy array
   shared_tensor.data[0][2] = 0.6
   assert data_to_share[0][2] == 0.6

Running Inference
~~~~~~~~~~~~~~~~~

Python API supports extra calling methods to synchronous and asynchronous 
modes for inference.

All infer methods allow users to pass data as popular *numpy* arrays, gathered 
in either Python dicts or lists.

.. ref-code-block:: cpp

   # Passing inputs data in form of a dictionary
   infer_request.infer(inputs={0: data})
   # Passing inputs data in form of a list
   infer_request.infer(inputs=[data])

Results from inference can be obtained in various ways:

.. ref-code-block:: cpp

   # Get output tensor
   results = infer_request.get_output_tensor().data

   # Get tensor with CompiledModel's output node
   results = infer_request.get_tensor(compiled.outputs[0]).data

   # Get all results with special helper property
   results = list(infer_request.results.values())

Synchronous Mode - Extended
---------------------------

Python API provides different synchronous calls to infer model, which block the 
application execution. Additionally, these calls return results of inference:

.. ref-code-block:: cpp

   # Simple call to InferRequest
   results = infer_request.infer(inputs={0: data})
   # Extra feature: calling CompiledModel directly
   results = compiled_model(inputs={0: data})

AsyncInferQueue
---------------

Asynchronous mode pipelines can be supported with a wrapper class called 
``AsyncInferQueue``. This class automatically spawns the pool of 
``InferRequest`` objects (also called "jobs") and provides synchronization 
mechanisms to control the flow of the pipeline.

Each job is distinguishable by a unique ``id``, which is in the range from 0 
up to the number of jobs specified in the ``AsyncInferQueue`` constructor.

The ``start_async`` function call is not required to be synchronized - it waits 
for any available job if the queue is busy/overloaded. Every 
``AsyncInferQueue`` code block should end with the ``wait_all`` function which 
provides the "global" synchronization of all jobs in the pool and ensure that 
access to them is safe.

.. ref-code-block:: cpp

   core = :ref:`ov.Core <doxid-classov_1_1_core>`()

   # Simple model that adds two inputs together
   input_a = ov.opset8.parameter([8])
   input_b = ov.opset8.parameter([8])
   res = ov.opset8.add(input_a, input_b)
   model = :ref:`ov.Model <doxid-classov_1_1_model>`(res, [input_a, input_b])
   compiled = core.compile_model(model, "CPU")

   # Number of InferRequests that AsyncInferQueue holds
   jobs = 4
   infer_queue = ov.AsyncInferQueue(compiled, jobs)

   # Create data
   data = [np.array([i] \* 8, dtype=np.float32) for i in :ref:`range <doxid-namespacengraph_1_1runtime_1_1reference_1ad38dec78131946cded583cc1154a406d>`(jobs)]

   # Run all jobs
   for i in :ref:`range <doxid-namespacengraph_1_1runtime_1_1reference_1ad38dec78131946cded583cc1154a406d>`(len(data)):
       infer_queue.start_async({0: data[i], 1: data[i]})
   infer_queue.wait_all()

Acquiring Results from Requests
+++++++++++++++++++++++++++++++

After the call to ``wait_all``, jobs and their data can be safely accessed. 
Acquiring a specific job with ``[id]`` will return the ``InferRequest`` 
object, which will result in seamless retrieval of the output data.

.. ref-code-block:: cpp

   results = infer_queue[3].get_output_tensor().data

Setting Callbacks
+++++++++++++++++

Another feature of ``AsyncInferQueue`` is the ability to set callbacks. When 
callback is set, any job that ends inference calls upon the Python function. 
The callback function must have two arguments: one is the request that calls 
the callback, which provides the ``InferRequest`` API; the other is called 
"userdata", which provides the possibility of passing runtime values. Those 
values can be of any Python type and later used within the callback function.

The callback of ``AsyncInferQueue`` is uniform for every job. When executed, 
GIL is acquired to ensure safety of data manipulation inside the function.

.. ref-code-block:: cpp

   data_done = [False for _ in :ref:`range <doxid-namespacengraph_1_1runtime_1_1reference_1ad38dec78131946cded583cc1154a406d>`(jobs)]

   def :ref:`f <doxid-namespacengraph_1_1runtime_1_1reference_1a4582949bb0b6082a5159f90c43a71ca9>`(request, userdata):
       print(f"Done! Result: {request.get_output_tensor().data}")
       data_done[userdata] = True

   infer_queue.set_callback(f)

   for i in :ref:`range <doxid-namespacengraph_1_1runtime_1_1reference_1ad38dec78131946cded583cc1154a406d>`(len(data)):
       infer_queue.start_async({0: data[i], 1: data[i]}, userdata=i)
   infer_queue.wait_all()

   assert all(data_done)

Working with u1, u4 and i4 Element Types
----------------------------------------

Since OpenVINO™ supports low precision element types, there are a few ways to 
handle them in Python. To create an input tensor with such element types, you 
may need to pack your data in the new *numpy* array, with which the byte size 
matches the original input size:

.. ref-code-block:: cpp

   from openvino.helpers import pack_data

   packed_buffer = pack_data(unt8_data, ov.Type.u4)
   # Create tensor with shape in element types
   t = :ref:`ov.Tensor <doxid-classov_1_1_tensor>`(packed_buffer, [1, 128], ov.Type.u4)

To extract low precision values from a tensor into the *numpy* array, you can 
use the following helper:

.. ref-code-block:: cpp

   from openvino.helpers import unpack_data

   unpacked_data = unpack_data(t.data, t.element_type, t.shape)
   assert np.array_equal(unpacked_data , unt8_data)

Release of GIL
--------------

Some functions in Python API release the Global Lock Interpreter (GIL) while 
running work-intensive code. This can help you achieve more parallelism in your 
application, using Python threads. For more information about GIL, refer to the 
Python documentation.

.. ref-code-block:: cpp

   import openvino.runtime as ov
   import cv2 as cv
   from threading import Thread

   input_data = []

   # Processing input data will be done in a separate thread
   # while compilation of the model and creation of the infer request
   # is going to be executed in the main thread.
   def prepare_data(input, image_path):
       image = cv.imread(image_path)
       h, w = list(input.shape)[-2:]
       image = cv.resize(image, (h, w))
       image = image.transpose((2, 0, 1))
       image = np.expand_dims(image, 0)
       input_data.append(image)

   core = :ref:`ov.Core <doxid-classov_1_1_core>`()
   model = core.read_model("model.xml")
   # Create thread with prepare_data function as target and start it
   thread = Thread(target=prepare_data, args=[model.input(), "path/to/image"])
   thread.start()
   # The GIL will be released in compile_model.
   # It allows a thread above to start the job,
   # while main thread is running in the background.
   compiled = core.compile_model(model, "GPU")
   # After returning from compile_model, the main thread acquires the GIL
   # and starts create_infer_request which releases it once again.
   request = compiled.create_infer_request()
   # Join the thread to make sure the input_data is ready
   thread.join()
   # running the inference
   request.infer(input_data)

.. note:: While GIL is released, functions can still modify and/or operate on Python 
   objects in C++. Hence, there is no reference counting. You should pay attention 
   to thread safety in case sharing of these objects with another thread occurs. 
   It might affect code only if multiple threads are spawned in Python.

List of Functions that Release the GIL
++++++++++++++++++++++++++++++++++++++

* openvino.runtime.AsyncInferQueue.start_async

* openvino.runtime.AsyncInferQueue.is_ready

* openvino.runtime.AsyncInferQueue.wait_all

* openvino.runtime.AsyncInferQueue.get_idle_request_id

* openvino.runtime.CompiledModel.create_infer_request

* openvino.runtime.CompiledModel.infer_new_request

* openvino.runtime.CompiledModel.__call__

* openvino.runtime.CompiledModel.export

* openvino.runtime.CompiledModel.get_runtime_model

* openvino.runtime.Core.compile_model

* openvino.runtime.Core.read_model

* openvino.runtime.Core.import_model

* openvino.runtime.Core.query_model

* openvino.runtime.Core.get_available_devices

* openvino.runtime.InferRequest.infer

* openvino.runtime.InferRequest.start_async

* openvino.runtime.InferRequest.wait

* openvino.runtime.InferRequest.wait_for

* openvino.runtime.InferRequest.get_profiling_info

* openvino.runtime.InferRequest.query_state

* openvino.runtime.Model.reshape

* openvino.preprocess.PrePostProcessor.build
