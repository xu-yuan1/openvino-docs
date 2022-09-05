.. index:: pair: page; Hello Reshape SSD C++ Sample
.. _doxid-openvino_inference_engine_samples_hello_reshape_ssd__r_e_a_d_m_e:


Hello Reshape SSD C++ Sample
============================

:target:`doxid-openvino_inference_engine_samples_hello_reshape_ssd__r_e_a_d_m_e_1md_openvino_samples_cpp_hello_reshape_ssd_readme` This sample demonstrates how to do synchronous inference of object detection models using :ref:`input reshape feature <deploy_infer__shape_inference>`. Models with only one input and output are supported.

The following C++ API is used in the application:

.. list-table::
    :header-rows: 1

    * - Feature
      - API
      - Description
    * - Node operations
      - ``:ref:`ov::Node::get_type_info <doxid-classov_1_1_node_1a21eaf78313b6823ee7af4a099147f2a7>``` , ``:ref:`ngraph::op::DetectionOutput::get_type_info_static <doxid-classov_1_1op_1_1_op_1a67be7c9343aa67e8dcc9866c722cb097>``` , ``ov::Output::get_any_name`` , ``ov::Output::get_shape``
      - Get a node info
    * - Model Operations
      - ``:ref:`ov::Model::get_ops <doxid-classov_1_1_model_1ac52bc1bbf8140877ceb74f387794d7b3>``` , ``:ref:`ov::Model::reshape <doxid-classov_1_1_model_1aa21aff80598d5089d591888a4c7f33ae>```
      - Get model nodes, reshape input
    * - Tensor Operations
      - ``:ref:`ov::Tensor::data <doxid-classov_1_1_tensor_1aaf6d1cd69a759b31c65fed8b3e7d66fb>```
      - Get a tensor data
    * - Preprocessing
      - ``:ref:`ov::preprocess::PreProcessSteps::convert_element_type <doxid-classov_1_1preprocess_1_1_pre_process_steps_1aac6316155a1690609eb320637c193d50>``` , ``:ref:`ov::preprocess::PreProcessSteps::convert_layout <doxid-classov_1_1preprocess_1_1_pre_process_steps_1a0f65fdadca32e90f5ef3a323b640b978>```
      - Model input preprocessing

Basic OpenVINO™ Runtime API is covered by :ref:`Hello Classification C++ sample <doxid-openvino_inference_engine_samples_hello_classification__r_e_a_d_m_e>`.

.. list-table::
    :header-rows: 1

    * - Options
      - Values
    * - Validated Models
      - person-detection-retail-0013
    * - Model Format
      - OpenVINO™ toolkit Intermediate Representation (\*.xml + \*.bin), ONNX (\*.onnx)
    * - Supported devices
      - :ref:`All <doxid-openvino_docs__o_v__u_g_supported_plugins__supported__devices>`
    * - Other language realization
      - :ref:`Python <doxid-openvino_inference_engine_ie_bridges_python_sample_hello_reshape_ssd__r_e_a_d_m_e>`

How It Works
~~~~~~~~~~~~

Upon the start-up the sample application reads command line parameters, loads specified network and image to the Inference Engine plugin. Then, the sample creates an synchronous inference request object. When inference is done, the application creates output image and output data to the standard output stream.

You can see the explicit description of each sample step at :ref:`Integration Steps <deploy_infer__integrate_application>` section of "Integrate OpenVINO™ Runtime with Your Application" guide.

Building
~~~~~~~~

To build the sample, please use instructions available at :ref:`Build the Sample Applications <get_started__samples_overview>` section in OpenVINO™ Toolkit Samples guide.

Running
~~~~~~~

.. ref-code-block:: cpp

	hello_reshape_ssd <path_to_model> <path_to_image> <device>

To run the sample, you need specify a model and image:

* you can use public or Intel's pre-trained models from the Open Model Zoo. The models can be downloaded using the Model Downloader.

* you can use images from the media files collection available at `https://storage.openvinotoolkit.org/data/test_data <https://storage.openvinotoolkit.org/data/test_data>`__.

**NOTES** :

* By default, OpenVINO™ Toolkit Samples and Demos expect input with BGR channels order. If you trained your model to work with RGB order, you need to manually rearrange the default channels order in the sample or demo application or reconvert your model using the Model Optimizer tool with ``--reverse_input_channels`` argument specified. For more information about the argument, refer to **When to Reverse Input Channels** section of :ref:`Embedding Preprocessing Computation <doxid-openvino_docs__m_o__d_g_prepare_model_convert_model__converting__model>`.

* Before running the sample with a trained model, make sure the model is converted to the intermediate representation (IR) format (\*.xml + \*.bin) using the :ref:`Model Optimizer tool <conv_prep__conv_with_model_optimizer>`.

* The sample accepts models in ONNX format (\*.onnx) that do not require preprocessing.



Example
-------

#. Install openvino-dev python package if you don't have it to use Open Model Zoo Tools:

.. ref-code-block:: cpp

	python -m pip install openvino-dev[caffe,onnx,tensorflow2,pytorch,mxnet]

#. Download a pre-trained model using:

.. ref-code-block:: cpp

	omz_downloader --name person-detection-retail-0013

#. ``person-detection-retail-0013`` does not need to be converted, because it is already in necessary format, so you can skip this step. If you want to use another model that is not in the IR or ONNX format, you can convert it using the model converter script:

.. ref-code-block:: cpp

	omz_converter --name <model_name>

#. Perform inference of ``person_detection.bmp`` using ``person-detection-retail-0013`` model on a ``GPU``, for example:

.. ref-code-block:: cpp

	hello_reshape_ssd person-detection-retail-0013.xml person_detection.bmp GPU

Sample Output
~~~~~~~~~~~~~

The application renders an image with detected objects enclosed in rectangles. It outputs the list of classes of the detected objects along with the respective confidence values and the coordinates of the rectangles to the standard output stream.

.. ref-code-block:: cpp

	[ INFO ] OpenVINO Runtime version ......... <version>
	[ INFO ] Build ........... <build>
	[ INFO ]
	[ INFO ] Loading model files: \models\person-detection-retail-0013.xml
	[ INFO ] model name: ResMobNet_v4 (LReLU) with single SSD head
	[ INFO ]     inputs
	[ INFO ]         input name: data
	[ INFO ]         input type: f32
	[ INFO ]         input shape: {1, 3, 320, 544}
	[ INFO ]     outputs
	[ INFO ]         output name: detection_out
	[ INFO ]         output type: f32
	[ INFO ]         output shape: {1, 1, 200, 7}
	Reshape network to the image size = [960x1699]
	[ INFO ] model name: ResMobNet_v4 (LReLU) with single SSD head
	[ INFO ]     inputs
	[ INFO ]         input name: data
	[ INFO ]         input type: f32
	[ INFO ]         input shape: {1, 3, 960, 1699}
	[ INFO ]     outputs
	[ INFO ]         output name: detection_out
	[ INFO ]         output type: f32
	[ INFO ]         output shape: {1, 1, 200, 7}
	[0,1] element, prob = 0.716309,    (852,187)-(983,520)
	The resulting image was saved in the file: hello_reshape_ssd_output.bmp
	
	This sample is an API example, for any performance measurements please use the dedicated benchmark_app tool

See Also
~~~~~~~~

* :ref:`Integrate the OpenVINO™ Runtime with Your Application <deploy_infer__integrate_application>`

* :ref:`Using OpenVINO™ Toolkit Samples <get_started__samples_overview>`

* Model Downloader

* :ref:`Model Optimizer <conv_prep__conv_with_model_optimizer>`

