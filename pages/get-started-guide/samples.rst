.. index:: pair: page; OpenVINO Samples
.. _get_started__samples_overview:


Samples
=======

:target:`get_started__samples_overview_1md_openvino_docs_ov_runtime_ug_samples_overview`

.. _code samples:

.. toctree::
   :maxdepth: 1
   :hidden:

   ./samples/basic-openvino-workflow
   ./samples/cpp-sample-image-classification
   ./samples/python-sample-image-classification
   ./samples/cpp-sample-hello-classification
   ./samples/c-sample-hello-classification
   ./samples/python-sample-hello-classification
   ./samples/cpp-sample-hello-reshape-ssd
   ./samples/python-sample-hello-reshape-ssd
   ./samples/cpp-sample-hello-nv12-input-classification
   ./samples/c-sample-hello-nv12-input-classification
   ./samples/cpp-sample-hello-query-device
   ./samples/python-sample-hello-query-device
   ./samples/cpp-sample-model-creation
   ./samples/python-sample-model-creation
   ./samples/cpp-sample-automatic-speech-recognition.rst
   ./samples/python-sample-automatic-speech-recognition
   ./samples/cpp-benchmark-tool
   ./samples/python-benchmark-tool

The OpenVINO samples are simple console applications that show how to utilize 
specific OpenVINO API capabilities within an application. They can assist you 
in executing specific tasks such as loading a model, running inference, querying 
specific device capabilities, etc.

If you install OpenVINO™ Runtime, sample applications for C, C++, and Python are 
created in the following directories:

* ``<INSTALL_DIR>/samples/c``

* ``<INSTALL_DIR>/samples/cpp``

* ``<INSTALL_DIR>/samples/python``

The applications include:

* **Speech Sample** - Acoustic model inference based on Kaldi neural networks 
  and speech feature vectors.

  * :ref:`Automatic Speech Recognition C++ Sample <doxid-openvino_inference_engine_samples_speech_sample__r_e_a_d_m_e>`

  * :ref:`Automatic Speech Recognition Python Sample <doxid-openvino_inference_engine_ie_bridges_python_sample_speech_sample__r_e_a_d_m_e>`

* **Hello Classification Sample** - Inference of image classification networks 
  like AlexNet and GoogLeNet using Synchronous Inference Request API. Input of 
  any size and layout can be set to an infer request which will be pre-processed 
  automatically during inference (the sample supports only images as inputs and 
  supports Unicode paths).

  * :ref:`Hello Classification C++ Sample <doxid-openvino_inference_engine_samples_hello_classification__r_e_a_d_m_e>`

  * :ref:`Hello Classification C Sample <doxid-openvino_inference_engine_ie_bridges_c_samples_hello_classification__r_e_a_d_m_e>`

  * :ref:`Hello Classification Python Sample <doxid-openvino_inference_engine_ie_bridges_python_sample_hello_classification__r_e_a_d_m_e>`

* **Hello NV12 Input Classification Sample** - Input of any size and layout can 
  be provided to an infer request. The sample transforms the input to the NV12 
  color format and pre-process it automatically during inference. The sample 
  supports only images as inputs.

  * :ref:`Hello NV12 Input Classification C++ Sample <doxid-openvino_inference_engine_samples_hello_nv12_input_classification__r_e_a_d_m_e>`

  * :ref:`Hello NV12 Input Classification C Sample <doxid-openvino_inference_engine_ie_bridges_c_samples_hello_nv12_input_classification__r_e_a_d_m_e>`

* **Hello Query Device Sample** - Query of available OpenVINO devices and their 
  metrics, configuration values.
  
  * :ref:`Hello Query Device C++ Sample <doxid-openvino_inference_engine_samples_hello_query_device__r_e_a_d_m_e>`
  
  * :ref:`Hello Query Device Python Sample <doxid-openvino_inference_engine_ie_bridges_python_sample_hello_query_device__r_e_a_d_m_e>`

* **Hello Reshape SSD Sample** - Inference of SSD networks resized by ShapeInfer 
  API according to an input size.

  * :ref:`Hello Reshape SSD C++ Sample <doxid-openvino_inference_engine_samples_hello_reshape_ssd__r_e_a_d_m_e>`

  * :ref:`Hello Reshape SSD Python Sample <doxid-openvino_inference_engine_ie_bridges_python_sample_hello_reshape_ssd__r_e_a_d_m_e>`

* **Image Classification Sample Async** - Inference of image classification 
  networks like AlexNet and GoogLeNet using Asynchronous Inference Request API 
  (the sample supports only images as inputs).

  * :ref:`Image Classification Async C++ Sample <doxid-openvino_inference_engine_samples_classification_sample_async__r_e_a_d_m_e>`

  * :ref:`Image Classification Async Python Sample <doxid-openvino_inference_engine_ie_bridges_python_sample_classification_sample_async__r_e_a_d_m_e>`

* **OpenVINO Model Creation Sample** - Construction of the LeNet model using 
  the OpenVINO model creation sample.

  * :ref:`OpenVINO Model Creation C++ Sample <doxid-openvino_inference_engine_samples_model_creation_sample__r_e_a_d_m_e>`

  * :ref:`OpenVINO Model Creation Python Sample <doxid-openvino_inference_engine_ie_bridges_python_sample_model_creation_sample__r_e_a_d_m_e>`

* **Benchmark Application** - Estimates deep learning inference performance on 
  supported devices for synchronous and asynchronous modes.

  * :ref:`Benchmark C++ Tool <doxid-openvino_inference_engine_samples_benchmark_app__r_e_a_d_m_e>`

  Note that the Python version of the benchmark tool is currently available only 
  through the :ref:`OpenVINO Development Tools installation <doxid-openvino_docs_install_guides_install_dev_tools>`. 
  It is not created in the samples directory but can be launched with the following 
  command: ``benchmark_app -m <model> -i <input> -d <device>`` For more information, 
  check the :ref:`Benchmark Python Tool <doxid-openvino_inference_engine_tools_benchmark_tool__r_e_a_d_m_e>` 
  documentation.

.. note:: All C++ samples support input paths containing only ASCII characters, 
   except for the Hello Classification Sample, that supports Unicode.


Media Files Available for Samples
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To run the sample applications, you can use images and videos from the media 
files collection available at `https://storage.openvinotoolkit.org/data/test_data <https://storage.openvinotoolkit.org/data/test_data>`__.

Samples that Support Pre-Trained Models
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To run the sample, you can use public or Intel's pre-trained models from the 
Open Model Zoo. The models can be downloaded using the Model Downloader.

Build the Sample Applications
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. _build_samples_linux:

Build the Sample Applications on Linux
--------------------------------------

The officially supported Linux build environment is the following:

* Ubuntu 18.04 LTS 64-bit or Ubuntu 20.04 LTS 64-bit

* GCC 7.5.0 (for Ubuntu 18.04) or GCC\* 9.3.0 (for Ubuntu 20.04)

* CMake version 3.10 or higher

.. note:: For building samples from the open-source version of OpenVINO™ toolkit, 
   see the `build instructions on GitHub <https://github.com/openvinotoolkit/openvino/wiki/BuildingCode>`__.


To build the C or C++ sample applications for Linux, go to the ``<INSTALL_DIR>/samples/c`` 
or ``<INSTALL_DIR>/samples/cpp`` directory, respectively, and run the 
``build_samples.sh`` script:

.. ref-code-block:: cpp

	build_samples.sh

Once the build is completed, you can find sample binaries in the following folders:

* C samples: ``~/openvino_c_samples_build/intel64/Release``

* C++ samples: ``~/openvino_cpp_samples_build/intel64/Release``

You can also build the sample applications manually:

.. note:: If you have installed the product as a root user, switch to root mode 
   before you continue: ``sudo -i``


#. Navigate to a directory that you have write access to and create a samples 
   build directory. This example uses a directory named ``build`` :

   .. ref-code-block:: cpp

      mkdir build


   .. note:: If you run the Image Classification verification script during the 
      installation, the C++ samples build directory is created in your home 
      directory: ``~/openvino_cpp_samples_build/``

#. Go to the created directory:
   
   .. ref-code-block:: cpp
   
   	cd build

#. Run CMake to generate the Make files for release or debug configuration. For 
   example, for C++ samples:

   * For release configuration:

     .. ref-code-block:: cpp

     	cmake -DCMAKE_BUILD_TYPE=Release <INSTALL_DIR>/samples/cpp

   * For debug configuration:

     .. ref-code-block:: cpp

     	cmake -DCMAKE_BUILD_TYPE=Debug <INSTALL_DIR>/samples/cpp

#. Run ``make`` to build the samples:
   
   .. ref-code-block:: cpp
   
      make

For the release configuration, the sample application binaries are in 
``<path_to_build_directory>/intel64/Release/``; for the debug configuration — 
in ``<path_to_build_directory>/intel64/Debug/``.

.. _build_samples_windows:

Build the Sample Applications on Microsoft Windows
--------------------------------------------------

The recommended Windows build environment is the following:

* Microsoft Windows 10

* Microsoft Visual Studio 2019

* CMake version 3.10 or higher

.. note:: If you want to use Microsoft Visual Studio 2019, you are required to 
   install CMake 3.14 or higher.


To build the C or C++ sample applications on Windows, go to the 
``<INSTALL_DIR>\samples\c`` or ``<INSTALL_DIR>\samples\cpp`` directory, respectively, 
and run the ``build_samples_msvc.bat`` batch file:

.. ref-code-block:: cpp

   build_samples_msvc.bat

By default, the script automatically detects the highest Microsoft Visual Studio 
version installed on the machine and uses it to create and build a solution for 
a sample code

Once the build is completed, you can find sample binaries in the following folders:

* C samples: ``C:\Users\<user>\Documents\Intel\OpenVINO\openvino_c_samples_build\intel64\Release``

* C++ samples: ``C:\Users\<user>\Documents\Intel\OpenVINO\openvino_cpp_samples_build\intel64\Release``

You can also build a generated solution manually. For example, if you want to 
build C++ sample binaries in Debug configuration, run the appropriate version 
of the Microsoft Visual Studio and open the generated solution file from the 
``C:\Users\<user>\Documents\Intel\OpenVINO\openvino_cpp_samples_build\Samples.sln`` 
directory.

.. _build_samples_macos:

Build the Sample Applications on macOS
----------------------------------------

The officially supported macOS build environment is the following:

* macOS 10.15 64-bit or higher

* Clang compiler from Xcode 10.1 or higher

* CMake version 3.13 or higher

.. note:: For building samples from the open-source version of OpenVINO™ toolkit, 
   see the `build instructions on GitHub <https://github.com/openvinotoolkit/openvino/wiki/BuildingCode>`__.


To build the C or C++ sample applications for macOS, go to the 
``<INSTALL_DIR>/samples/c`` or ``<INSTALL_DIR>/samples/cpp`` directory, respectively, 
and run the ``build_samples.sh`` script:

.. ref-code-block:: cpp

	build_samples.sh

Once the build is completed, you can find sample binaries in the following folders:

* C samples: ``~/inference_engine_c_samples_build/intel64/Release``

* C++ samples: ``~/inference_engine_cpp_samples_build/intel64/Release``

You can also build the sample applications manually:

.. note:: If you have installed the product as a root user, switch to root mode 
   before you continue: ``sudo -i``


.. note:: Before proceeding, make sure you have OpenVINO™ environment set correctly. 
   This can be done manually by


.. ref-code-block:: cpp

	cd <INSTALL_DIR>/
	source setupvars.sh

#. Navigate to a directory that you have write access to and create a samples 
   build directory. This example uses a directory named ``build`` :

   .. ref-code-block:: cpp

      mkdir build


   .. note:: If you ran the Image Classification verification script during the 
      installation, the C++ samples build directory was already created in your 
      home directory: ``~/openvino_cpp_samples_build/``

#. Go to the created directory:
   
   .. ref-code-block:: cpp
   
   	cd build

#. Run CMake to generate the Make files for release or debug configuration. For 
   example, for C++ samples:

   * For release configuration:

     .. ref-code-block:: cpp

        cmake -DCMAKE_BUILD_TYPE=Release <INSTALL_DIR>/samples/cpp

   * For debug configuration:
     
     .. ref-code-block:: cpp
     
        cmake -DCMAKE_BUILD_TYPE=Debug <INSTALL_DIR>/samples/cpp

#. Run ``make`` to build the samples:
   
   .. ref-code-block:: cpp
   
   	make


For the release configuration, the sample application binaries are in 
``<path_to_build_directory>/intel64/Release/``; for the debug configuration — in 
``<path_to_build_directory>/intel64/Debug/``.

Get Ready for Running the Sample Applications
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Get Ready for Running the Sample Applications on Linux
------------------------------------------------------

Before running compiled binary files, make sure your application can find the 
OpenVINO Runtime libraries. Run the ``setupvars`` script to set all necessary 
environment variables:

.. ref-code-block:: cpp

   source <INSTALL_DIR>/setupvars.sh

**(Optional)**: The OpenVINO environment variables are removed when you 
close the shell. As an option, you can permanently set the environment variables 
as follows:

#. Open the ``.bashrc`` file in ``<user_home_directory>`` :

   .. ref-code-block:: cpp

      vi <user_home_directory>/.bashrc

#. Add this line to the end of the file:

   .. ref-code-block:: cpp

      source /opt/intel/openvino_2022/setupvars.sh

#. Save and close the file: press the **Esc** key, type ``:wq`` and press the 
   **Enter** key.

#. To test your change, open a new terminal. You will see 
   ``[setupvars.sh] OpenVINO environment initialized``.

You are ready to run sample applications. To learn about how to run a particular 
sample, read the sample documentation by clicking the sample name in the samples 
list above.

Get Ready for Running the Sample Applications on Windows
----------------------------------------------------------

Before running compiled binary files, make sure your application can find the 
OpenVINO Runtime libraries. Use the ``setupvars`` script, which sets all necessary 
environment variables:

.. ref-code-block:: cpp

   <INSTALL_DIR>\setupvars.bat

To debug or run the samples on Windows in Microsoft Visual Studio, make sure you 
have properly configured **Debugging** environment settings for the **Debug** and 
**Release** configurations. Set correct paths to the OpenCV libraries, and debug 
and release versions of the OpenVINO Runtime libraries. For example, for the 
**Debug** configuration, go to the project's **Configuration Properties** to the 
**Debugging** category and set the ``PATH`` variable in the **Environment** 
field to the following:

.. ref-code-block:: cpp

   PATH=<INSTALL_DIR>\runtime\bin;%PATH%

where ``<INSTALL_DIR>`` is the directory in which the OpenVINO toolkit is installed.

You are ready to run sample applications. To learn about how to run a particular 
sample, read the sample documentation by clicking the sample name in the samples 
list above.

See Also
~~~~~~~~

* :ref:`OpenVINO™ Runtime User Guide <deploy_infer__openvino_runtime_user_guide>`
