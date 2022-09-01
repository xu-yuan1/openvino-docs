.. index:: pair: page; Use Post-Training Optimization Tool Command-Line Interface (Model Zoo flow)
.. _pot_cli:

.. meta::
   :description: In Post-Training Optimization Tool Command-line Interface 
                 basic options are specified directly via command-line and 
                 advanced options in a configuration file.
   :keywords: Post-training Optimization Tool, Post-training Optimization Tool 
              Command-Line Interface, POT, POT CLI, DefaultQuantization, 
              default quantization, quantizing models, AccuracyAwareQuantization, 
              accuracy-aware quantization, accuracy checker, full-precision model,
              post-training quantization, AccuracyChecker, Open Model Zoo, 
              command-line interface, configuration file, Simplified Mode

POT Command-line Interface
==========================

:target:`pot_cli_1md_openvino_tools_pot_docs_cli`


.. toctree::
   :maxdepth: 1
   :hidden:

   ./command-line-interface/simplified-mode
   ./command-line-interface/configuration-file

Introduction
~~~~~~~~~~~~

Post-Training Optimization Tool command-line interface (CLI) is aimed at 
optimizing models that are similar to the models from OpenVINO 
`Model Zoo <https://github.com/openvinotoolkit/open_model_zoo>`__ 
or if there is a valid AccuracyChecker Tool configuration file for the model. 
Examples of AccuracyChecker configuration files can be found on 
`GitHub <https://github.com/openvinotoolkit/open_model_zoo/tree/master/models/public>`__. 
Each model folder contains YAML configuration file that can be used with POT as is.

.. note:: There is also the so-called :ref:`Simplified mode <pot_simplified_mode>` 
   aimed at optimization of models from the Computer Vision domain and has a simple 
   dataset preprocessing, like image resize and crop. In this case, you can also 
   use POT CLI for optimization. However, the accuracy results are not guaranteed 
   in this case. Moreover, you are also limited in the optimization methods choice 
   since the accuracy measurement is not available.

Run POT CLI
~~~~~~~~~~~

There are two ways how to run POT via command line:

* **Basic usage for DefaultQuantization**. In this case you can run POT with 
  basic setting just specifying all the options via command line. ``-q default`` 
  stands for :ref:`DefaultQuantization <default_quantization_algorithm>` 
  algorithm:

  .. ref-code-block:: cpp

     pot -q default -m <path_to_xml> -w <path_to_bin> --ac-config <path_to_AC_config_yml>

* **Basic usage for AccuracyAwareQuantization**. You can also run 
  :ref:`AccuracyAwareQuantization <accuracy_aware_quantization_algorithm>` method 
  with basic options. ``--max-drop 0.01`` option defines maximum accuracy 
  deviation to 1 absolute percent from the original model:

  .. ref-code-block:: cpp

     pot -q accuracy_aware -m <path_to_xml> -w <path_to_bin> --ac-config <path_to_AC_config_yml> --max-drop 0.01

* **Advanced usage**. In this case you should prepare a configuration file for 
  the POT where you can specify advanced options for the optimization methods 
  available. See :ref:`POT configuration file description <pot_configuration_file>` 
  for more details. To launch the command-line tool with the configuration 
  file run:

  .. ref-code-block:: cpp

     pot -c <path_to_config_file>

  For all available usage options, use the ``-h``, ``--help`` arguments or 
  refer to the Command-Line Arguments section below.

By default, the results are dumped into the separate output subfolder inside 
the ``./results`` folder that is created in the same directory where the tool 
is run from. Use the ``-e`` option to evaluate the accuracy directly from the tool.

See also the :ref:`End-to-end example <pot_cli_example>` 
about how to run a particular example of 8-bit quantization with the POT.

Command-Line Arguments
----------------------

The following command-line options are available to run the tool:

.. list-table::
    :header-rows: 1

    * - Argument
      - Description
    * - ``-h`` , ``--help``
      - Optional. Show help message and exit.
    * - ``-q`` , ``--quantize``
      - Quantize model to 8 bits with specified quantization method: 
        ``default`` or ``accuracy_aware`` .
    * - ``--preset``
      - Use ``performance`` for fully symmetric quantization or ``mixed`` preset 
        for symmetric quantization of weight and asymmetric quantization of 
        activations. Applicable only when ``-q`` option is used.
    * - ``-m`` , ``--model``
      - Path to the optimizing model file (.xml). Applicable only when ``-q`` 
        option is used.
    * - ``-w`` , ``--weights``
      - Path to the weights file of the optimizing model (.bin). Applicable 
        only when ``-q`` option is used.
    * - ``-n`` , ``--name``
      - Optional. Model name. Applicable only when ``-q`` option is used.
    * - ``--engine {accuracy_checker, simplified}``
      - Engine type used to specify CLI mode. Default: ``accuracy_checker`` .
    * - ``--data-source DATA_DIR``
      - Optional. Valid and required for Simplified mode only. Specifies the 
        path to calibration data.
    * - ``--ac-config``
      - Path to the Accuracy Checker configuration file. Applicable only when 
        ``-q`` option is used.
    * - ``--max-drop``
      - Optional. Maximum accuracy drop. Valid only for accuracy-aware 
        quantization. Applicable only when ``-q`` option is used and 
        ``accuracy_aware`` method is selected.
    * - ``-c CONFIG`` , ``--config CONFIG``
      - Path to a config file with task- or model-specific parameters.
    * - ``-e`` , ``--evaluate``
      - Optional. Evaluate model on the whole dataset after optimization.
    * - ``--output-dir OUTPUT_DIR``
      - Optional. A directory where results are saved. Default: ``./results`` .
    * - ``-sm`` , ``--save-model``
      - Optional. Save the original full-precision model.
    * - ``-d`` , ``--direct-dump``
      - Optional. Save results to the "optimized" subfolder within the specified 
        output directory with no additional subpaths added at the end.
    * - ``--log-level {CRITICAL,ERROR,WARNING,INFO,DEBUG}``
      - Optional. Log level to print. Default: INFO.
    * - ``--progress-bar``
      - Optional. Disable CL logging and enable progress bar.
    * - ``--stream-output``
      - Optional. Switch model quantization progress display to a multiline 
        mode. Use with third-party components.
    * - ``--keep-uncompressed-weights``
      - Optional. Keep Convolution, Deconvolution and FullyConnected weights 
        uncompressed. Use with third-party components.

See Also
~~~~~~~~

* :ref:`Optimization with Simplified mode <pot_simplified_mode>`

* :ref:`Post-Training Optimization Best Practices <pot_quantization_best_practices>`
