.. index:: pair: page; Installing Intel® Distribution of OpenVINO™ Toolkit
.. _install__overview:


Installing Intel® Distribution of OpenVINO™ Toolkit
======================================================

:target:`install__overview_1md_openvino_docs_install_guides_installing_openvino_overview`





.. toctree::
   :maxdepth: 3
   :hidden:

   OpenVINO Runtime <./install-openvino-overview/install-openvino-runtime>
   OpenVINO Development Tools <./install-openvino-overview/install-openvino-dev-tools>
   Build from Source <https://github.com/openvinotoolkit/openvino/wiki/BuildingCode>
   Creating a Yocto Image <./install-openvino-overview/install-create-yocto-image>

Intel® Distribution of OpenVINO™ toolkit is a comprehensive toolkit for developing applications and solutions based on deep learning tasks, such as: emulation of human vision, automatic speech recognition, natural language processing, recommendation systems, etc. It provides high-performance and rich deployment options, from edge to cloud. Some of its advantages are:

* Enabling CNN-based deep learning inference on the edge.

* Supporting various execution modes across Intel® technologies: Intel® CPU, Intel® Integrated Graphics, Intel® Neural Compute Stick 2, and Intel® Vision Accelerator Design with Intel® Movidius™ VPUs.

* Speeding time-to-market via an easy-to-use library of computer vision functions and pre-optimized kernels.

Installation Options
~~~~~~~~~~~~~~~~~~~~

Since the 2022.1 release, the OpenVINO installation package has been distributed in two parts: OpenVINO Runtime and OpenVINO Development Tools. See the following instructions to choose your installation process.

Decide What to Install
----------------------

If you have already finished developing your models and converting them to the OpenVINO model format, you can :ref:`install OpenVINO Runtime <install_openvino_runtime>` to deploy your applications on various devices. OpenVINO Runtime contains a set of libraries for easy inference integration with your products.

If you want to download models from :ref:`Open Model Zoo <doxid-model_zoo>`, :ref:`convert your own models to OpenVINO IR <conv_prep__conv_with_model_optimizer>`, or :ref:`optimize and tune pre-trained deep learning models <optim_perf__model_optim_guide>`, :ref:`install OpenVINO Development Tools <install_openvino_dev_tools>`, which provides the following tools:

* Model Optimizer

* Post-Training Optimization Tool

* Benchmark Tool

* Accuracy Checker and Annotation Converter

* Model Downloader and other Open Model Zoo tools

Choose Your Installation Method
-------------------------------

For Python developers, the easiest way is to :ref:`install OpenVINO Development Tools <install_openvino_dev_tools>`, which will install both OpenVINO Runtime and OpenVINO Development Tools with a few steps. If you want to install OpenVINO Runtime only, see :ref:`Install OpenVINO Runtime from PyPI <doxid-openvino_docs_install_guides_installing_openvino_pip>`.

For C++ developers, you may choose one of the following installation options for OpenVINO Runtime on your specific operating system:

* Linux: You can install OpenVINO Runtime using an :ref:`Installer <install__linux_installer>`, :ref:`APT <install__linux_apt>`, :ref:`YUM <install__linux_yum>`, :ref:`Anaconda Cloud <doxid-openvino_docs_install_guides_installing_openvino_conda>`, or :ref:`Docker <install__on_linux_from_docker>`.

* Windows: You can install OpenVINO Runtime using an :ref:`Installer <install__windows_installer>`, :ref:`Anaconda Cloud <doxid-openvino_docs_install_guides_installing_openvino_conda>`, or :ref:`Docker <install__on_windows_from_docker>`.

* macOS: You can install OpenVINO Runtime using an :ref:`Installer <doxid-openvino_docs_install_guides_installing_openvino_macos>` or :ref:`Anaconda Cloud <doxid-openvino_docs_install_guides_installing_openvino_conda>`.

* :ref:`Raspbian OS <doxid-openvino_docs_install_guides_installing_openvino_raspbian>`.

.. note:: With the introduction of the 2022.1 release, the OpenVINO Development Tools can be installed **only** via PyPI. See :ref:`Install OpenVINO Development Tools <install_openvino_dev_tools>` for detailed steps.



Source files are also available in the `OpenVINO toolkit GitHub repository <https://github.com/openvinotoolkit/openvino/>`__, so you can build your own package for the supported platforms, as described in `OpenVINO Build Instructions <https://github.com/openvinotoolkit/openvino/wiki/BuildingCode>`__.

Next Steps
~~~~~~~~~~

* :ref:`Install OpenVINO Runtime <install_openvino_runtime>`

* :ref:`Install OpenVINO Development Tools <install_openvino_dev_tools>`

* `Build from Source <https://github.com/openvinotoolkit/openvino/wiki/BuildingCode>`__

* :ref:`Create a Yocto Image <install__create_yocto_image>`

