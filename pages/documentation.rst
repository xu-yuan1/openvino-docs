.. index:: pair: page; Documentation
.. _doxid-documentation:


Documentation
=============

:target:`doxid-documentation_1md_openvino_docs_documentation`





.. toctree::
   :maxdepth: 1
   :caption: API 2.0
   :hidden:

   openvino_2_0_transition_guide


.. toctree::
   :maxdepth: 1
   :caption: Converting and Preparing Models
   :hidden:

   openvino_docs_model_processing_introduction
   openvino_docs_MO_DG_Deep_Learning_Model_Optimizer_DevGuide
   omz_tools_downloader


.. toctree::
   :maxdepth: 1
   :caption: Optimization and Performance
   :hidden:

   openvino_docs_optimization_guide_dldt_optimization_guide
   openvino_docs_MO_DG_Getting_Performance_Numbers
   openvino_docs_model_optimization_guide
   openvino_docs_deployment_optimization_guide_dldt_optimization_guide
   openvino_docs_tuning_utilities
   openvino_docs_performance_benchmarks


.. toctree::
   :maxdepth: 1
   :caption: Deploying Inference
   :hidden:

   openvino_docs_deployment_guide_introduction
   openvino_docs_OV_UG_OV_Runtime_User_Guide
   openvino_deployment_guide
   openvino_inference_engine_tools_compile_tool_README


.. toctree::
   :maxdepth: 1
   :hidden:
   :caption: THE Ecosystem

   openvino_ecosystem
   ovms_what_is_openvino_model_server
   ovsa_get_started
   ovtf_integration
   ote_documentation
   workbench_docs_Workbench_DG_Introduction


.. toctree::
   :maxdepth: 1
   :hidden:
   :caption: Media Processing and Computer Vision Libraries

   Intel® Deep Learning Streamer <openvino_docs_dlstreamer>
   openvino_docs_gapi_gapi_intro
   OpenCV* Developer Guide <https://docs.opencv.org/master/>
   OpenCL™ Developer Guide <https://software.intel.com/en-us/openclsdk-devguide>   


.. toctree::
   :maxdepth: 1
   :caption: OpenVINO Extensibility
   :hidden:

   openvino_docs_Extensibility_UG_Intro
   openvino_docs_transformations
   OpenVINO Plugin Developer Guide <openvino_docs_ie_plugin_dg_overview>

.. toctree::
   :maxdepth: 1
   :hidden:
   :caption: Use OpenVINO™ Toolkit Securely

   openvino_docs_security_guide_introduction
   openvino_docs_security_guide_workbench
   openvino_docs_OV_UG_protecting_model_guide
   ovsa_get_started

This section provides reference documents that guide you through the OpenVINO toolkit workflow, from obtaining models, optimizing them, to deploying them in your own deep learning applications.

Converting and Preparing Models
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

With Model Downloader and :ref:`Model Optimizer <doxid-openvino_docs__m_o__d_g__deep__learning__model__optimizer__dev_guide>` guides, you will learn to download pre-trained models and convert them for use with OpenVINO™. You can use your own models or choose some from a broad selection provided in the :ref:`Open Model Zoo <doxid-model_zoo>`.

Optimization and Performance
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In this section you will find resources on :ref:`how to test inference performance <doxid-openvino_docs__m_o__d_g__getting__performance__numbers>` and :ref:`how to increase it <doxid-openvino_docs_optimization_guide_dldt_optimization_guide>`. It can be achieved by :ref:`optimizing the model <doxid-openvino_docs_model_optimization_guide>` or :ref:`optimizing inference at runtime <doxid-openvino_docs_deployment_optimization_guide_dldt_optimization_guide>`.

Deploying Inference
~~~~~~~~~~~~~~~~~~~

This section explains the process of creating your own inference application using :ref:`OpenVINO™ Runtime <doxid-openvino_docs__o_v__u_g__o_v__runtime__user__guide>` and documents the `OpenVINO Runtime API <./api_references.html>`__ for both Python and C++. It also provides a :ref:`guide on deploying applications with OpenVINO <doxid-openvino_deployment_guide>` and directs you to other sources on this topic.

OpenVINO Ecosystem
~~~~~~~~~~~~~~~~~~

Apart from the core components, OpenVINO offers tools, plugins, and expansions revolving around it, even if not constituting necessary parts of its workflow. This section will give you an overview of :ref:`what makes up OpenVINO Toolkit <doxid-openvino_ecosystem>`.

Media Processing and Computer Vision Libraries
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The OpenVINO™ toolkit also works with the following media processing frameworks and libraries:

* :ref:`Intel® Deep Learning Streamer (Intel® DL Streamer) <doxid-openvino_docs_dlstreamer>` — A streaming media analytics framework based on GStreamer, for creating complex media analytics pipelines optimized for Intel hardware platforms. Go to the Intel® DL Streamer `documentation <https://dlstreamer.github.io/>`__ website to learn more.

* `Intel® oneAPI Video Processing Library (oneVPL) <https://www.intel.com/content/www/us/en/develop/documentation/oneapi-programming-guide/top/api-based-programming/intel-oneapi-video-processing-library-onevpl.html>`__ — A programming interface for video decoding, encoding, and processing to build portable media pipelines on CPUs, GPUs, and other accelerators.

You can also add computer vision capabilities to your application using optimized versions of `OpenCV <https://opencv.org/>`__.

