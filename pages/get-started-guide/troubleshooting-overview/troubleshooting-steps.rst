.. index:: pair: page; Troubleshooting Steps for OpenVINO™ Installation and Configurations
.. _doxid-openvino_docs_get_started_guide_troubleshooting_steps:


Troubleshooting Steps for OpenVINO™ Installation and Configurations
=====================================================================

:target:`doxid-openvino_docs_get_started_guide_troubleshooting_steps_1md_openvino_docs_install_guides_troubleshooting_steps` If you run into issues while installing or configuring OpenVINO™, you can try the following methods to do some quick checks first.

Check the versions of OpenVINO Runtime and Developement Tools
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* To check the version of OpenVINO Development Tools, use the following command:
  
  .. ref-code-block:: cpp
  
  	mo --version

* To check the version of OpenVINO Runtime, use the following code:
  
  .. ref-code-block:: cpp
  
  	from openvino.runtime import get_version get_version()

Check the versions of Python and PIP
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To check your Python version, run  ``python -VV`` or ``python --version``. The supported Python versions should be 64-bit and between 3.7 and 3.9. If you are using Python 3.6, you are recommended to upgrade the version to 3.7 or higher.

If your Python version does not meet the requirements, update Python:

* For Windows, **do not install Python from a Windows Store** as it can cause issues. You are highly recommended to install Python from `https://www.python.org/ <https://www.python.org/>`__.

* For Linux and macOS systems, download and install a proper Python version from `https://www.python.org/ <https://www.python.org/>`__. See the `Python Beginners' Guide <https://wiki.python.org/moin/BeginnersGuide/Download>`__ for more information on selecting a version. Note that macOS 10.x comes with python 2.7 installed, which is not supported, so you must install Python from the official website.

For PIP, make sure that you have installed the latest version. To check and upgrade your PIP version, run the following command:

.. ref-code-block:: cpp

	python -m pip install --upgrade pip

Check if required external dependencies are installed
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For Ubuntu and RHEL 8 systems, if you installed OpenVINO Runtime via the installer, APT, or YUM repository, and decided to :ref:`install OpenVINO Development Tools <install_openvino_dev_tools>`, make sure that you :ref:`Install External Software Dependencies <install-external-dependencies>` first.

For C++ developers with Windows systems, make sure that Microsoft Visual Studio 2019 with MSBuild and CMake 3.14 or higher (64-bit) are installed. While installing Microsoft Visual Studio 2019, make sure that you have selected \*\*Desktop development with C++\*\* in the \*\*Workloads\*\* tab. If not, launch the installer again to select that option. For more information on modifying the installation options for Microsoft Visual Studio, see its `official support page <https://docs.microsoft.com/en-us/visualstudio/install/modify-visual-studio?view=vs-2019>`__.

Check if environment variables are set correctly
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* For Python developers, if you previously installed OpenVINO using the installer, and are now installing OpenVINO using PIP, remove all the PATH settings and the lines with ``setupvars`` from ``.bashrc``. Note that if you installed OpenVINO with PIP in a virtual environment, you don't need to set any environment variables.

* If you have installed OpenVINO before, you probably have added ``setupvars`` to your ``PATH /.bashrc`` or Windows environment variables. After restarting your environment, you should see similar information as below:
  
  .. ref-code-block:: cpp
  
  	[setupvars.sh] OpenVINO™ environment initialized
  
  
  
  * If you don't see the information above, your PATH variables may be configured incorrectly. Check if you have typed the correct <INSTALL_DIR> or you are trying to activate in the correct directory.
  
  * If you added it to a ``.bashrc`` file, make sure that the command is correctly written and the file is found in the ``~/.bashrc`` folder.

Verify that OpenVINO is correctly installed
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* For Python developers, to verify if OpenVINO is correctly installed, use the following command:

  .. code-block:: sh

     python -c "from openvino.runtime import Core"

  If OpenVINO was successfully installed, nothing will happen. If not, an error will be displayed.

* If you installed OpenVINO Runtime using the installer, you can search "openvino" in Apps & Features on a Windows system, or check your installation directory on Linux to see if OpenVINO is there.

* If you installed OpenVINO Runtime from APT, use the ``apt list --installed | grep openvino`` command to list the installed OpenVINO packages.

* If you installed OpenVINO Runtime from YUM, use the ``yum list installed 'openvino*'`` command to list the installed OpenVINO packages.

Check if GPU drvier is installed
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:ref:`Additional configurations <install__additional_config>` may be required in order to use OpenVINO with different hardware such as Intel® GPUs.

To run inference on an Intel® GPU, make sure that you have installed the correct GPU driver. To check that, see :ref:`additional configurations for GPU <doxid-openvino_docs_install_guides_configurations_for_intel_gpu>`.

Check firewall and network settings
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Make sure that your firewall and network settings are configured correctly. For example, consider configuring system-wide proxy settings and specifying options for using PIP behind the proxy:

.. code-block:: sh

      pip install --proxy http://address:port --trusted-host pypi.org openvino

For specific issues, see :ref:`Errors with Installing via PIP for Users in China <install-for-prc>` and :ref:`proxy issues with installing OpenVINO on Linux from Docker <proxy-issues>`.

