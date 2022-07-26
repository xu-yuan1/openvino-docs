.. index:: pair: page; Converting a PyTorch Model
.. _doxid-openvino_docs__m_o__d_g_prepare_model_convert_model__convert__model__from__py_torch:


Converting a PyTorch Model
==========================

:target:`doxid-openvino_docs__m_o__d_g_prepare_model_convert_model__convert__model__from__py_torch_1md_openvino_docs_mo_dg_prepare_model_convert_model_convert_model_from_pytorch` The PyTorch framework is supported through export to the ONNX format. In order to optimize and deploy a model that was trained with it:

#. `Export a PyTorch model to ONNX <#export-to-onnx>`__.

#. :ref:`Convert the ONNX model <doxid-openvino_docs__m_o__d_g_prepare_model_convert_model__convert__model__from__o_n_n_x>` to produce an optimized :ref:`Intermediate Representation <doxid-openvino_docs__m_o__d_g__i_r_and_opsets>` of the model based on the trained network topology, weights, and biases values.

.. _export-to-onnx:

Exporting a PyTorch Model to ONNX Format
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

PyTorch models are defined in Python. To export them, use the ``torch.onnx.export()`` method. The code to evaluate or test the model is usually provided with its code and can be used for its initialization and export. The export to ONNX is crucial for this process, but it is covered by PyTorch framework, therefore, It will not be covered here in detail. For more information, refer to the `Exporting PyTorch models to ONNX format <https://pytorch.org/docs/stable/onnx.html>`__ guide.

To export a PyTorch model, you need to obtain the model as an instance of ``torch.nn.Module`` class and call the ``export`` function.

.. ref-code-block:: cpp

	import torch
	
	# Instantiate your model. This is just a regular PyTorch model that will be exported in the following steps.
	model = SomeModel()
	# Evaluate the model to switch some operations from training mode to inference.
	model.eval()
	# Create dummy input for the model. It will be used to run the model inside export function.
	dummy_input = torch.randn(1, 3, 224, 224)
	# Call the export function
	torch.onnx.export(model, (dummy_input, ), 'model.onnx')

Known Issues
~~~~~~~~~~~~

* As of version 1.8.1, not all PyTorch operations can be exported to ONNX opset 9 which is used by default. It is recommended to export models to opset 11 or higher when export to default opset 9 is not working. In that case, use ``opset_version`` option of the ``torch.onnx.export``. For more information about ONNX opset, refer to the `Operator Schemas <https://github.com/onnx/onnx/blob/master/docs/Operators.md>`__ page.

See Also
~~~~~~~~

:ref:`Model Conversion Tutorials <doxid-openvino_docs__m_o__d_g_prepare_model_convert_model_tutorials>`

