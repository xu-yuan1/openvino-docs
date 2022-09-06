.. index:: pair: page; Install Intel® Distribution of OpenVINO™ Toolkit from PyPI Repository
.. _install__from_pypi:


Install Intel® Distribution of OpenVINO™ Toolkit from PyPI Repository
========================================================================

:target:`install__from_pypi_1md_openvino_docs_install_guides_installing_openvino_pip` You can install both OpenVINO™ Runtime and OpenVINO Development Tools through the PyPI repository. This page provides the main steps for installing OpenVINO Runtime.

.. note:: From the 2022.1 release, the OpenVINO™ Development Tools can only be installed via PyPI. See :ref:`Install OpenVINO Development Tools <install_openvino_dev_tools>` for detailed steps.





Installing OpenVINO Runtime
~~~~~~~~~~~~~~~~~~~~~~~~~~~

For system requirements and troubleshooting, see `https://pypi.org/project/openvino/ <https://pypi.org/project/openvino/>`__.

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

.. tab:: On Linux and macOS

   .. code-block:: sh

      source openvino_env/bin/activate

.. tab:: On Windows

   .. code-block:: sh

      openvino_env\Scripts\activate

Step 3. Set Up and Update PIP to the Highest Version
----------------------------------------------------

Use the following command:

.. ref-code-block:: cpp

	python -m pip install --upgrade pip

Step 4. Install the Package
---------------------------

Use the following command:

.. ref-code-block:: cpp

	pip install openvino

Step 5. Verify that the Package Is Installed
--------------------------------------------

Run the command below:

.. ref-code-block:: cpp

	python -c "from openvino.runtime import Core"

If installation was successful, you will not see any error messages (no console output).

Installing OpenVINO Development Tools
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

OpenVINO Development Tools include Model Optimizer, Benchmark Tool, Accuracy Checker, Post-Training Optimization Tool and Open Model Zoo tools including Model Downloader. If you want to install OpenVINO Development Tools, OpenVINO Runtime will also be installed as a dependency, so you don't need to install OpenVINO Runtime separately.

See :ref:`Install OpenVINO™ Development Tools <install_openvino_dev_tools>` for detailed steps.

What's Next?
~~~~~~~~~~~~

Now you may continue with the following tasks:

* To convert models for use with OpenVINO, see :ref:`Model Optimizer Developer Guide <conv_prep__conv_with_model_optimizer>`.

* See pre-trained deep learning models in our :ref:`Open Model Zoo <doxid-model_zoo>`.

* Try out OpenVINO via `OpenVINO Notebooks <https://docs.openvino.ai/latest/notebooks/notebooks.html>`__.

* To write your own OpenVINO™ applications, see :ref:`OpenVINO Runtime User Guide <deploy_infer__openvino_runtime_user_guide>`.

* See sample applications in :ref:`OpenVINO™ Toolkit Samples Overview <get_started__samples_overview>`.

Additional Resources
~~~~~~~~~~~~~~~~~~~~

* Intel® Distribution of OpenVINO™ toolkit home page: `https://software.intel.com/en-us/openvino-toolkit <https://software.intel.com/en-us/openvino-toolkit>`__

* For IoT Libraries & Code Samples, see `Intel® IoT Developer Kit <https://github.com/intel-iot-devkit>`__.

