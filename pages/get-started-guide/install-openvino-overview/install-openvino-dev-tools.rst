.. index:: pair: page; Install OpenVINO™ Development Tools
.. _install_openvino_dev_tools:


Install OpenVINO™ Development Tools
=====================================

:target:`install_openvino_dev_tools_1md_openvino_docs_install_guides_installing_model_dev_tools` If you want to download, convert, optimize and tune pre-trained deep learning models, install OpenVINO™ Development Tools, which provides the following tools:

* Model Optimizer

* Benchmark Tool

* Accuracy Checker and Annotation Converter

* Post-Training Optimization Tool

* Model Downloader and other Open Model Zoo tools

.. note:: From the 2022.1 release, the OpenVINO™ Development Tools can only be installed via PyPI.





For Python Developers
~~~~~~~~~~~~~~~~~~~~~

If you are a Python developer, you can find the main steps below to install OpenVINO Development Tools. For more details, see `https://pypi.org/project/openvino-dev <https://pypi.org/project/openvino-dev>`__.

While installing OpenVINO Development Tools, OpenVINO Runtime will also be installed as a dependency, so you don't need to install OpenVINO Runtime separately.

Step 1. Set Up Python Virtual Environment
-----------------------------------------

Use a virtual environment to avoid dependency conflicts.

To create a virtual environment, use the following command:

.. tab:: Linux and macOS

   .. code-block:: sh

      python3 -m venv openvino_env

.. tab:: Windows

   .. code-block:: sh

      python -m venv openvino_env

Step 2. Activate Virtual Environment
------------------------------------

.. tab:: Linux and macOS

   .. code-block:: sh

      source openvino_env/bin/activate

.. tab:: Windows

   .. code-block:: sh

      openvino_env\Scripts\activate

Step 3. Set Up and Update PIP to the Highest Version
----------------------------------------------------

Use the following command:

.. ref-code-block:: cpp

	python -m pip install --upgrade pip

Step 4. Install the Package
---------------------------

To install and configure the components of the development package for working with specific frameworks, use the following command:

.. ref-code-block:: cpp

	pip install openvino-dev[extras]

where the ``extras`` parameter specifies one or more deep learning frameworks via these values: ``caffe``, ``kaldi``, ``mxnet``, ``onnx``, ``pytorch``, ``tensorflow``, ``tensorflow2``. Make sure that you install the corresponding frameworks for your models.

For example, to install and configure the components for working with TensorFlow 2.x and ONNX, use the following command:

.. ref-code-block:: cpp

	pip install openvino-dev[tensorflow2,onnx]

.. note:: Model Optimizer support for TensorFlow 1.x environment has been deprecated. Use TensorFlow 2.x environment to convert both TensorFlow 1.x and 2.x models. Use the ``tensorflow2`` value as much as possible. The ``tensorflow`` value is provided only for compatibility reasons.

Step 5. Verify the Installation
-------------------------------

To verify if the package is properly installed, run the command below (this may take a few seconds):

.. ref-code-block:: cpp

	mo -h

You will see the help message for Model Optimizer if installation finished successfully.

For C++ Developers
~~~~~~~~~~~~~~~~~~

Note the following things:

* To install OpenVINO Development Tools, you must have OpenVINO Runtime installed first. You can install OpenVINO Runtime through an installer (:ref:`Linux <doxid-openvino_docs_install_guides_installing_openvino_linux>`, :ref:`Windows <doxid-openvino_docs_install_guides_installing_openvino_windows>`, or :ref:`macOS <doxid-openvino_docs_install_guides_installing_openvino_macos>`), :ref:`APT for Linux <doxid-openvino_docs_install_guides_installing_openvino_apt>` or :ref:`YUM for Linux <doxid-openvino_docs_install_guides_installing_openvino_yum>`.

* Ensure that the version of OpenVINO Development Tools you are installing matches that of OpenVINO Runtime.

Use either of the following ways to install OpenVINO Development Tools:

Recommended: Install Using the Requirements Files
-------------------------------------------------

#. After you have installed OpenVINO Runtime from an installer, APT or YUM repository, you can find a set of requirements files in the ``<INSTALLDIR>\tools\`` directory. Select the most suitable ones to use.

#. Install the same version of OpenVINO Development Tools by using the requirements files. To install mandatory requirements only, use the following command:
   
   .. ref-code-block:: cpp
   
   	pip install -r <INSTALLDIR>\tools\requirements.txt

#. Make sure that you also install your additional frameworks with the corresponding requirements files. For example, if you are using a TensorFlow model, use the following command to install requirements for TensorFlow:
   
   
   
   .. ref-code-block:: cpp
   
   	pip install -r <INSTALLDIR>\tools\requirements_tensorflow2.txt

Alternative: Install from the openvino-dev Package
--------------------------------------------------

You can also use the following command to install the latest package version available in the index:

.. ref-code-block:: cpp

	pip install openvino-dev[EXTRAS]

where the EXTRAS parameter specifies one or more deep learning frameworks via these values: ``caffe``, ``kaldi``, ``mxnet``, ``onnx``, ``pytorch``, ``tensorflow``, ``tensorflow2``. Make sure that you install the corresponding frameworks for your models.

If you have installed OpenVINO Runtime via the installer, to avoid version conflicts, specify your version in the command. For example:

.. ref-code-block:: cpp

	pip install openvino-dev[tensorflow2,onnx]==2022.1

.. note:: Model Optimizer support for TensorFlow 1.x environment has been deprecated. Use TensorFlow 2.x environment to convert both TensorFlow 1.x and 2.x models. The ``tensorflow`` value is provided only for compatibility reasons, use the ``tensorflow2`` value instead.



For more details, see `https://pypi.org/project/openvino-dev/ <https://pypi.org/project/openvino-dev/>`__.

What's Next?
~~~~~~~~~~~~

Now you may continue with the following tasks:

* To convert models for use with OpenVINO, see :ref:`Model Optimizer Developer Guide <doxid-openvino_docs__m_o__d_g__deep__learning__model__optimizer__dev_guide>`.

* See pre-trained deep learning models in our :ref:`Open Model Zoo <doxid-model_zoo>`.

* Try out OpenVINO via `OpenVINO Notebooks <https://docs.openvino.ai/latest/notebooks/notebooks.html>`__.

* To write your own OpenVINO™ applications, see :ref:`OpenVINO Runtime User Guide <deploy_infer__openvino_runtime_user_guide>`.

* See sample applications in :ref:`OpenVINO™ Toolkit Samples Overview <get_started__samples_overview>`.

Additional Resources
~~~~~~~~~~~~~~~~~~~~

* Intel® Distribution of OpenVINO™ toolkit home page: `https://software.intel.com/en-us/openvino-toolkit <https://software.intel.com/en-us/openvino-toolkit>`__

* For IoT Libraries & Code Samples, see `Intel® IoT Developer Kit <https://github.com/intel-iot-devkit>`__.

