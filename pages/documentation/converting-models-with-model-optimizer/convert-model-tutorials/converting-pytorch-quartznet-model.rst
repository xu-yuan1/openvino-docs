.. index:: pair: page; Converting a PyTorch QuartzNet Model
.. _doxid-openvino_docs__m_o__d_g_prepare_model_convert_model_pytorch_specific__convert__quartz_net:


Converting a PyTorch QuartzNet Model
====================================

:target:`doxid-openvino_docs__m_o__d_g_prepare_model_convert_model_pytorch_specific__convert__quartz_net_1md_openvino_docs_mo_dg_prepare_model_convert_model_pytorch_specific_convert_quartznet` `NeMo project <https://github.com/NVIDIA/NeMo>`__ provides the QuartzNet model.

Downloading the Pretrained QuartzNet Model
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To download the pretrained model, refer to the `NeMo Speech Models Catalog <https://ngc.nvidia.com/catalog/models/nvidia:nemospeechmodels>`__. Here are the instructions on how to obtain QuartzNet in ONNX format.

#. Install the NeMo toolkit, using the `instructions <https://github.com/NVIDIA/NeMo/tree/main#installation>`__.

#. Run the following code:

.. ref-code-block:: cpp

	import nemo
	import nemo.collections.asr as nemo_asr
	
	quartznet = nemo_asr.models.EncDecCTCModel.from_pretrained(model_name="QuartzNet15x5Base-En")
	# Export QuartzNet model to ONNX format
	quartznet.decoder.export('decoder_qn.onnx')
	quartznet.encoder.export('encoder_qn.onnx')
	quartznet.export('qn.onnx')

This code produces 3 ONNX model files: ``encoder_qn.onnx``, ``decoder_qn.onnx``, ``qn.onnx``. They are ``decoder``, ``encoder``, and a combined ``decoder(encoder(x))`` models, respectively.

Converting an ONNX QuartzNet model to IR
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If using a combined model:

.. ref-code-block:: cpp

	mo --input_model <MODEL_DIR>/qt.onnx --input_shape [B,64,X]

If using separate models:

.. ref-code-block:: cpp

	mo --input_model <MODEL_DIR>/encoder_qt.onnx --input_shape [B,64,X]
	mo --input_model <MODEL_DIR>/decoder_qt.onnx --input_shape [B,1024,Y]

Where shape is determined by the audio file Mel-Spectrogram length: B - batch dimension, X - dimension based on the input length, Y - determined by encoder output, usually ``X / 2``.

