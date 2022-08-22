.. index:: pair: page; Configuration File Description
.. _pot_configuration_file:


Configuration File Description
==============================

:target:`pot_configuration_file_1md_openvino_tools_pot_configs_readme` 

The tool is designed to work with the configuration file where all the 
parameters required for the optimization are specified. These parameters are 
organized as a dictionary and stored in a JSON file. JSON file allows using 
comments that are supported by the ``jstyleson`` Python package. Logically 
all parameters are divided into three groups:

* **Model parameters** that are related to the model definition (for example, 
  model name, model path, etc.)

* **Engine parameters** that define parameters of the engine which is 
  responsible for the model inference and data preparation used for 
  optimization and evaluation (for example, preprocessing parameters, dataset path, etc.)

* **Compression parameters** that are related to the optimization algorithm 
  (for example, algorithm name and specific parameters)

Model Parameters
~~~~~~~~~~~~~~~~

.. ref-code-block:: cpp

   "model": {
           "model_name": "model_name",
           "model": "<MODEL_PATH>",
           "weights": "<PATH_TO_WEIGHTS>"
       }

This section contains only three parameters:

* ``"model_name"`` - string parameter that defines a model name, for 
  example ``"MobileNetV2"``

* ``"model"`` - string parameter that defines the path to an input model 
  topology (.xml)

* ``"weights"`` - string parameter that defines the path to an input model 
  weights (.bin)

Engine Parameters
~~~~~~~~~~~~~~~~~

.. ref-code-block:: cpp

   "engine": {
           "type": "accuracy_checker",
           "config": "./configs/examples/accuracy_checker/mobilenet_v2.yaml"
       }

The main parameter is ``"type"`` which can take two possible options: 
``"accuracy_checher"`` (default) or ``"simplified"``. It specifies the engine 
used for model inference and validation (if supported):

* **Simplified mode** engines. These engines can be used only with 
  ``DefaultQuantization`` algorithm to get a fully quantized model. They do not 
  use the Accuracy Checker tool and annotation. In this case, the following 
  parameters are applicable:

  * ``"data_source"`` Specifies the path to the directory​ where the 
    calibration data is stored.

  * ``"layout"`` - (Optional) Layout of input data. Supported values: 
    [``"NCHW"``, ``"NHWC"``, ``"CHW"``, ``"CWH"``]​.

* **Accuracy Checker** engine. It relies on the Deep Learning Accuracy 
  Validation Framework (Accuracy Checker) when inferencing DL models and 
  working with datasets. If you have annotations, you can benefit from this 
  mode by measuring accuracy. When this mode is selected, you can use the 
  accuracy-aware algorithms family. There are two options to define engine 
  parameters in this mode:

  * Refer to the existing Accuracy Checker configuration file which is 
    represented by the YAML file. It can be a file used for full-precision 
    model validation. In this case, you should define only the ``"config"`` 
    parameter containing the path to the AccuracyChecker configuration file.

  * Define all the required Accuracy Checker parameters directly in the 
    JSON file. In this case, POT just passes the corresponding dictionary of 
    parameters to the Accuracy Checker when instantiating it. For more details, 
    refer to the corresponding Accuracy Checker information and examples of 
    configuration files provided with the tool:

    * 8-bit quantization of `SSD-MobileNet model <https://github.com/openvinotoolkit/openvino/blob/master/tools/pot/configs/examples/quantization/object_detection/ssd_mobilenetv1_int8.json>`__

Compression Parameters
~~~~~~~~~~~~~~~~~~~~~~

For more details about parameters of the concrete optimization algorithm, see 
descriptions of :ref:`Default Quantization <default_quantization_algorithm>` 
and :ref:`Accuracy-aware Quantizatoin <accuracy_aware_quantization_algorithm>` 
methods.

Examples of the Configuration File
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For a quick start, many examples of configuration files are provided 
`here <https://github.com/openvinotoolkit/openvino/blob/master/tools/pot/configs/examples>`__. There you can find ready-to-use configurations for the models from various domains: Computer Vision (Image Classification, Object Detection, Segmentation), Natural Language Processing, Recommendation Systems. We put configuration files for the models which require non-default configuration settings to get accurate results.

For details on how to run the Post-Training Optimization Tool with a sample configuration file, see the :ref:`example <pot_cli_example>`.

See Also
~~~~~~~~

* :ref:`Optimization with Simplified mode <pot_simplified_mode>`
