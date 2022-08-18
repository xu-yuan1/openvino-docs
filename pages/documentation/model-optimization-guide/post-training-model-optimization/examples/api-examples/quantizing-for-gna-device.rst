.. index:: pair: page; Quantizing for GNA Device
.. _doxid-pot_example_speech__r_e_a_d_m_e:


Quantizing for GNA Device
=========================

:target:`doxid-pot_example_speech__r_e_a_d_m_e_1md_openvino_tools_pot_openvino_tools_pot_api_samples_speech_readme` This example demonstrates the use of the :ref:`Post-training Optimization Tool API <doxid-pot_compression_api__r_e_a_d_m_e>` for the task of quantizing a speech model for :ref:`GNA <doxid-openvino_docs__o_v__u_g_supported_plugins__g_n_a>` device. Quantization for GNA is different from CPU quantization due to device specific: GNA supports quantized inputs in INT16 and INT32 (for activations) precision and quantized weights in INT8 and INT16 precision.

This example contains pre-selected quantization options based on the DefaultQuantization algorithm and created for models from `Kaldi <http://kaldi-asr.org/doc/>`__ framework, and its data format. A custom ``ArkDataLoader`` is created to load the dataset from files with .ark extension for speech analysis task.

How to prepare the data
~~~~~~~~~~~~~~~~~~~~~~~

To run this example, you will need to use the .ark files for each model input from your ``<DATA_FOLDER>``. For generating data from original formats to .ark, please, follow the `Kaldi data preparation tutorial <https://kaldi-asr.org/doc/data_prep.html>`__.

How to Run the example
~~~~~~~~~~~~~~~~~~~~~~

#. Launch :ref:`Model Optimizer <doxid-openvino_docs__m_o__d_g__deep__learning__model__optimizer__dev_guide>` with the necessary options (for details follow the :ref:`instructions for Kaldi <doxid-openvino_docs__m_o__d_g_prepare_model_convert_model__convert__model__from__kaldi>` to generate Intermediate Representation (IR) files for the model:
   
   .. ref-code-block:: cpp
   
   	mo --input_model <PATH_TO_KALDI_MODEL> [MODEL_OPTIMIZER_OPTIONS]

#. Launch the example script:
   
   .. ref-code-block:: cpp
   
   	python3 <POT_DIR>/api/examples/speech/gna_example.py -m <PATH_TO_IR_XML> -w <PATH_TO_IR_BIN> -d <DATA_FOLDER> --input_names [LIST_OF_MODEL_INPUTS] --files_for_input [LIST_OF_INPUT_FILES]
   
   Required parameters:
   
   * ``-i``, ``--input_names`` option. Defines list of model inputs;
   
   * ``-f``, ``--files_for_input`` option. Defines list of filenames (.ark) mapped with input names. You should define names without extension, for example: FILENAME_1, FILENAME_2 maps with INPUT_1, INPUT_2.
   
   Optional parameters:
   
   * ``-p``, ``--preset`` option. Defines preset for quantization: ``performance`` for INT8 weights, ``accuracy`` for INT16 weights;
   
   * ``-s``, ``--subset_size`` option. Defines subset size for calibration;
   
   * ``-o``, ``--output`` option. Defines output folder for quantized model.

#. Validate your INT8 model using ``./speech_example`` from the Inference Engine examples. Follow the :ref:`speech example description link <doxid-openvino_inference_engine_samples_speech_sample__r_e_a_d_m_e>` for details.

