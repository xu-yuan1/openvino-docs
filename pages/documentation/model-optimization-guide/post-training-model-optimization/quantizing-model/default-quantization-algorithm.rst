.. index:: pair: page; DefaultQuantization Algorithm
.. _doxid-pot_compression_algorithms_quantization_default__r_e_a_d_m_e:


DefaultQuantization Algorithm
=============================

:target:`doxid-pot_compression_algorithms_quantization_default__r_e_a_d_m_e_1md_openvino_tools_pot_openvino_tools_pot_algorithms_quantization_default_readme` The DefaultQuantization Algorithm is designed to perform fast and accurate quantization. It does not offer direct control over the accuracy metric itself but provides many options that can be used to improve it.

Parameters
~~~~~~~~~~

DefaultQuantization Algorithm has mandatory and optional parameters. For more details on how to use these parameters, refer to :ref:`Best Practices <doxid-pot_docs__best_practices>` article. Below is an example of the DefaultQuantization method and its parameters:

.. ref-code-block:: cpp

	{
	    "name": "DefaultQuantization", # the name of optimization algorithm 
	    "params": {
	        ...
	    }
	}

Mandatory parameters
--------------------

* ``"preset"`` - a preset which controls the quantization mode (symmetric and asymmetric). It can take two values:
  
  * ``"performance"`` (default) - stands for symmetric quantization of weights and activations. This is the most efficient across all the HW.
  
  * ``"mixed"`` - symmetric quantization of weights and asymmetric quantization of activations. This mode can be useful for quantization of NN, which has both negative and positive input values in quantizing operations, for example non-ReLU based CNN.

* ``"stat_subset_size"`` - size of a subset to calculate activations statistics used for quantization. The whole dataset is used if no parameter is specified. It is recommended to use not less than 300 samples.

* ``"stat_batch_size"`` - size of a batch to calculate activations statistics used for quantization. It has a value of 1 if no parameter is specified.

Optional parameters
-------------------

All other options should be considered as an advanced mode and require deep knowledge of the quantization process. Below is an overall description of all possible parameters:

* ``"model type"`` - an optional parameter, required for additional patterns in the model. The default value is "None" ("Transformer" is only other supported value now).

* ``"inplace_statistic"`` - an optional parameter, required for change of collect statistics method. This parameter reduces the amount of memory consumed, but increases the calibration time.

* ``"ignored"`` - NN subgraphs which should be excluded from the optimization process:
  
  * ``"scope"`` - a list of particular nodes to exclude.
  
  * ``"operations"`` - a list of operation types to exclude (expressed in OpenVINO IR notation). This list consists of the following tuples:
    
    * ``"type"`` - a type of ignored operation.
    
    * ``"attributes"`` - if attributes are defined, they will be considered during the ignorance. They are defined by a dictionary of ``"<NAME>": "<VALUE>"`` pairs.

* ``"weights"`` - this section describes quantization scheme for weights and the way to estimate the quantization range for that. It is worth noting that changing the quantization scheme may lead to inability to infer such mode on the existing HW.
  
  * ``"bits"`` - bit-width, the default value is "8".
  
  * ``"mode"`` - a quantization mode (symmetric or asymmetric).
  
  * ``"level_low"`` - the minimum level in the integer range to quantize. The default is "0" for an unsigned range, and "-2^(bit-1)" for a signed one .
  
  * ``"level_high"`` - the maximum level in the integer range to quantize. The default is "2^bits-1" for an unsigned range, and "2^(bit-1)-1" for a signed one.
  
  * ``"granularity"`` - quantization scale granularity. It can take the following values:
    
    * ``"pertensor"`` (default) - per-tensor quantization with one scale factor and zero-point.
    
    * ``"perchannel"`` - per-channel quantization with per-channel scale factor and zero-point.
  
  * ``"range_estimator"`` - this section describes parameters of range estimator that is used in MinMaxQuantization method to get the quantization ranges and filter outliers based on the collected statistics. Below are the parameters that can be modified to get better accuracy results:
    
    * ``"max"`` - parameters to estimate top border of quantizing floating-point range:
      
      * ``"type"`` - a type of the estimator:
        
        * ``"max"`` (default) - estimates the maximum in the quantizing set of value.
        
        * ``"quantile"`` - estimates the quantile in the quantizing set of value.
      
      * ``"outlier_prob"`` - outlier probability used in the "quantile" estimator.
    
    * ``"min"`` - parameters to estimate bottom border of quantizing floating-point range:
      
      * ``"type"`` - a type of the estimator:
        
        * ``"min"`` (default) - estimates the minimum in the quantizing set of value.
        
        * ``"quantile"`` - estimates the quantile in the quantizing set of value.
      
      * ``"outlier_prob"`` - outlier probability used in the "quantile" estimator.

* ``"activations"`` - this section describes quantization scheme for activations and the way to estimate the quantization range for that. As before, changing the quantization scheme may lead to inability to infer such mode on the existing HW:
  
  * ``"bits"`` - bit-width, the default value is "8".
  
  * ``"mode"`` - a quantization mode (symmetric or asymmetric).
  
  * ``"level_low"`` - the minimum level in the integer range to quantize. The default is "0" for an unsigned range, and "-2^(bit-1)" for a signed one.
  
  * ``"level_high"`` - the maximum level in the integer range to quantize. The default is "2^bits-1" for an unsigned range, and "2^(bit-1)-1" for a signed one.
  
  * ``"granularity"`` - quantization scale granularity. It can take the following values:
    
    * ``"pertensor"`` (default) - per-tensor quantization with one scale factor and zero-point.
    
    * ``"perchannel"`` - per-channel quantization with per-channel scale factor and zero-point.
  
  * ``"range_estimator"`` - this section describes parameters of range estimator that is used in MinMaxQuantization method to get the quantization ranges and filter outliers based on the collected statistics. These are the parameters that can be modified to get better accuracy results:
    
    * ``"preset"`` - preset that defines the same estimator for both top and bottom borders of quantizing floating-point range. Possible value is ``"quantile"``.
    
    * ``"max"`` - parameters to estimate top border of quantizing floating-point range:
      
      * ``"aggregator"`` - a type of the function used to aggregate statistics obtained with the estimator over the calibration dataset to get a value of the top border:
        
        * ``"mean"`` (default) - aggregates mean value.
        
        * ``"max"`` - aggregates max value.
        
        * ``"min"`` - aggregates min value.
        
        * ``"median"`` - aggregates median value.
        
        * ``"mean_no_outliers"`` - aggregates mean value after removal of extreme quantiles.
        
        * ``"median_no_outliers"`` - aggregates median value after removal of extreme quantiles.
        
        * ``"hl_estimator"`` - Hodges-Lehmann filter based aggregator.
      
      * ``"type"`` - a type of the estimator:
        
        * ``"max"`` (default) - estimates the maximum in the quantizing set of value.
        
        * ``"quantile"`` - estimates the quantile in the quantizing set of value.
      
      * ``"outlier_prob"`` - outlier probability used in the "quantile" estimator.
    
    * ``"min"`` - parameters to estimate bottom border of quantizing floating-point range:
      
      * ``"type"`` - a type of the estimator:
        
        * ``"max"`` (default) - estimates the maximum in the quantizing set of value.
        
        * ``"quantile"`` - estimates the quantile in the quantizing set of value.
      
      * ``"outlier_prob"`` - outlier probability used in the "quantile" estimator.

* ``"use_layerwise_tuning"`` - enables layer-wise fine-tuning of model parameters (biases, Convolution/MatMul weights and FakeQuantize scales) by minimizing the mean squared error between original and quantized layer outputs. Enabling this option may increase compressed model accuracy, but will result in increased execution time and memory consumption.

Additional Resources
~~~~~~~~~~~~~~~~~~~~

Tutorials:

* `Quantization of Image Classification model <https://github.com/openvinotoolkit/openvino_notebooks/tree/main/notebooks/301-tensorflow-training-openvino>`__

* `Quantization of Object Detection model from Model Zoo <https://github.com/openvinotoolkit/openvino_notebooks/tree/main/notebooks/111-detection-quantization>`__

* `Quantization of Segmentation model for mediacal data <https://github.com/openvinotoolkit/openvino_notebooks/tree/main/notebooks/110-ct-segmentation-quantize>`__

* `Quantization of BERT for Text Classification <https://github.com/openvinotoolkit/openvino_notebooks/tree/main/notebooks/105-language-quantize-bert>`__

Examples:

* `Quantization of 3D segmentation model <https://github.com/openvinotoolkit/openvino/tree/master/tools/pot/openvino/tools/pot/api/samples/3d_segmentation>`__

* `Quantization of Face Detection model <https://github.com/openvinotoolkit/openvino/tree/master/tools/pot/openvino/tools/pot/api/samples/face_detection>`__

* `Quantizatin of speech model for GNA device <https://github.com/openvinotoolkit/openvino/tree/master/tools/pot/openvino/tools/pot/api/samples/speech>`__

Command-line example:

* `Quantization of Image Classification model <https://docs.openvino.ai/latest/pot_configs_examples_README.html>`__

Full specification and a template for DefaultQuantization algorithm for POT command-line inferface:

* `Full specification <https://github.com/openvinotoolkit/openvino/blob/master/tools/pot/configs/default_quantization_spec.json>`__

.. dropdown:: Template

   .. code-block:: javascript

        /* This configuration file is the fastest way to get started with the default
        quantization algorithm. It contains only mandatory options with commonly used
        values. All other options can be considered as an advanced mode and requires
        deep knowledge of the quantization process. An overall description of all possible
        parameters can be found in the default_quantization_spec.json */

        {
            /* Model parameters */

            "model": {
                "model_name": "model_name", // Model name
                "model": "<MODEL_PATH>", // Path to model (.xml format)
                "weights": "<PATH_TO_WEIGHTS>" // Path to weights (.bin format)
            },

            /* Parameters of the engine used for model inference */

            "engine": {
                "config": "<CONFIG_PATH>" // Path to Accuracy Checker config
            },

            /* Optimization hyperparameters */

            "compression": {
                "target_device": "ANY", // Target device, the specificity of which will be taken
                                        // into account during optimization
                "algorithms": [
                    {
                        "name": "DefaultQuantization", // Optimization algorithm name
                        "params": {
                            "preset": "performance", // Preset [performance, mixed, accuracy] which control the quantization
                                                    // mode (symmetric, mixed (weights symmetric and activations asymmetric)
                                                    // and fully asymmetric respectively)

                            "stat_subset_size": 300  // Size of subset to calculate activations statistics that can be used
                                                    // for quantization parameters calculation
                        }
                    }
                ]
            }
        }

