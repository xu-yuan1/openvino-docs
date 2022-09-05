.. index:: pair: page; Compressing a Model to FP16
.. _conv_prep__fp16_compression:

.. meta:: 
   :description: Model Optimizer can convert all floating-point weights to FP16 
                 data type and the resulting IR will be a compressed FP16 model.
   :keywords: Model Optimizer, FP16, floating-point weights, compression to FP16, 
              accuracy drop, FP16 precision, OpenVINO IR, OpenVINO Intermediate 
              Representation, FP16 compression

Compressing a Model to FP16
===========================

:target:`conv_prep__fp16_compression_1md_openvino_docs_mo_dg_prepare_model_fp16_compression` 

Model Optimizer can convert all floating-point weights to ``FP16`` data type. The resulting IR is called compressed ``FP16`` model.

To compress the model, use the ``--data_type`` option:

.. ref-code-block:: cpp

	mo --input_model INPUT_MODEL --data_type FP16

.. note:: Using ``--data_type FP32`` will give no result and will not force ``FP32`` precision in the model. If the model was ``FP16``, it will have ``FP16`` precision in IR as well.



The resulting model will occupy about twice as less space in the file system, but it may have some accuracy drop. The resulting model will occupy about half of the previous space in the file system, but lose some of its accuracy. For most models, the accuracy drop is negligible. For details on how plugins handle compressed ``FP16`` models, see :ref:`Working with devices <deploy_infer__working_with_devices>`.

.. note:: ``FP16`` compression is sometimes used as the initial step for ``INT8`` quantization. Refer to the :ref:`Post-training optimization <optim_perf__pot_intro>` guide for more information about that.

