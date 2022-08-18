.. index:: pair: page; Converting a Kaldi Model
.. _doxid-openvino_docs__m_o__d_g_prepare_model_convert_model__convert__model__from__kaldi:


Converting a Kaldi Model
========================

:target:`doxid-openvino_docs__m_o__d_g_prepare_model_convert_model__convert__model__from__kaldi_1md_openvino_docs_mo_dg_prepare_model_convert_model_convert_model_from_kaldi`

.. note:: Model Optimizer supports the `nnet1 <http://kaldi-asr.org/doc/dnn1.html>`__ and `nnet2 <http://kaldi-asr.org/doc/dnn2.html>`__ formats of Kaldi models. The support of the `nnet3 <http://kaldi-asr.org/doc/dnn3.html>`__ format is limited.



:target:`doxid-openvino_docs__m_o__d_g_prepare_model_convert_model__convert__model__from__kaldi_1convert_from_kaldi` To convert a Kaldi model, run Model Optimizer with the path to the input model ``.nnet`` or ``.mdl`` file:

.. ref-code-block:: cpp

	mo --input_model <INPUT_MODEL>.nnet

.. _kaldi_specific_conversion_params:

Using Kaldi-Specific Conversion Parameters
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The following list provides the Kaldi-specific parameters.

.. ref-code-block:: cpp

	Kaldi-specific parameters:
	  --counts COUNTS       A file name with full path to the counts file or empty string to utilize count values from the model file
	  --remove_output_softmax
	                        Removes the Softmax that is the output layer
	  --remove_memory       Remove the Memory layer and add new inputs and outputs instead

Examples of CLI Commands
~~~~~~~~~~~~~~~~~~~~~~~~

* To launch Model Optimizer for the ``wsj_dnn5b_smbr`` model with the specified ``.nnet`` file:
  
  .. ref-code-block:: cpp
  
  	mo --input_model wsj_dnn5b_smbr.nnet

* To launch Model Optimizer for the ``wsj_dnn5b_smbr`` model with the existing file that contains counts for the last layer with biases:
  
  .. ref-code-block:: cpp
  
  	mo --input_model wsj_dnn5b_smbr.nnet --counts wsj_dnn5b_smbr.counts
  
  
  
  * The Model Optimizer normalizes сounts in the following way:
    
    .. math::
    
    	S = \frac{1}{\sum_{j = 0}^{|C|}C_{j}}
    
    
    
    .. math::
    
    	C_{i}=log(S\*C_{i})
    
    where :math:`C` - the counts array, :math:`C_{i} - i^{th}` element of the counts array, :math:`|C|` - number of elements in the counts array;
  
  * The normalized counts are subtracted from biases of the last or next to last layer (if last layer is SoftMax).
    
    > **NOTE** : Model Optimizer will show a warning if a model contains values of counts and the ``--counts`` option is not used.

* If you want to remove the last SoftMax layer in the topology, launch the Model Optimizer with the ``--remove_output_softmax`` flag:
  
  .. ref-code-block:: cpp
  
  	mo --input_model wsj_dnn5b_smbr.nnet --counts wsj_dnn5b_smbr.counts --remove_output_softmax
  
  The Model Optimizer finds the last layer of the topology and removes this layer only if it is a SoftMax layer.

.. note:: Model Optimizer can remove SoftMax layer only if the topology has one output.





* You can use the *OpenVINO Speech Recognition* sample application for the sample inference of Kaldi models. This sample supports models with only one output. If your model has several outputs, specify the desired one with the ``--output`` option.

Converting a Model for Intel® Movidius™ Myriad™ VPU
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you want to convert a model for inference on Intel® Movidius™ Myriad™ VPU, use the ``--remove_memory`` option. It removes the Memory layers from the OpenVINO IR files. Additional inputs and outputs will appear in the IR files instead. Model Optimizer will output the mapping between inputs and outputs. For example:

.. ref-code-block:: cpp

	[ WARNING ]  Add input/output mapped Parameter_0_for_Offset_fastlstm2.r_trunc__2Offset_fastlstm2.r_trunc__2_out -> Result_for_Offset_fastlstm2.r_trunc__2Offset_fastlstm2.r_trunc__2_out
	[ WARNING ]  Add input/output mapped Parameter_1_for_Offset_fastlstm2.r_trunc__2Offset_fastlstm2.r_trunc__2_out -> Result_for_Offset_fastlstm2.r_trunc__2Offset_fastlstm2.r_trunc__2_out
	[ WARNING ]  Add input/output mapped Parameter_0_for_iteration_Offset_fastlstm3.c_trunc__3390 -> Result_for_iteration_Offset_fastlstm3.c_trunc__3390

Based on this mapping, link inputs and outputs in your application manually as follows:

#. Initialize inputs from the mapping as zeros in the first frame of an utterance.

#. Copy output blobs from the mapping to the corresponding inputs. For example, data from ``Result_for_Offset_fastlstm2.r_trunc__2Offset_fastlstm2.r_trunc__2_out`` must be copied to ``Parameter_0_for_Offset_fastlstm2.r_trunc__2Offset_fastlstm2.r_trunc__2_out``.

Supported Kaldi Layers
~~~~~~~~~~~~~~~~~~~~~~

For the list of supported standard layers, refer to the :ref:`Supported Framework Layers <doxid-openvino_docs__m_o__d_g_prepare_model__supported__frameworks__layers>` page.

See Also
~~~~~~~~

:ref:`Model Conversion Tutorials <doxid-openvino_docs__m_o__d_g_prepare_model_convert_model_tutorials>`

