.. index:: pair: page; Step 1. Prerequisites Transformations
.. _plugin_lpt__step1_prerequisites:

.. meta::
   :description: Step 1 of low precision transformations. Feature a list of transforamtions used to 
                 fuse and propagate used to fuse and propagate operations in the model.
   :keywords: low precision transformations, lpt, prerequisites transformations, PullReshapeThroughDequantization,
              PullTransposeThroughDequantization, LinOpSequenceFusion


Step 1. Prerequisites Transformations
=====================================

:target:`plugin_lpt__step1_prerequisites_1md_openvino_docs_ie_plugin_dg_plugin_transformation_pipeline_low_precision_transformations_pipeline_step1_prerequisites` Prerequisites transformations are optional. The transformations prepare a model before running other low precision transformations. The transformations do not operate with dequantization operations or update precisions. Prerequisites transformations include:

* :ref:`PullReshapeThroughDequantization <doxid-openvino_docs__o_v__u_g_lpt__pull_reshape_through_dequantization>`

* :ref:`PullTransposeThroughDequantization <doxid-openvino_docs__o_v__u_g_lpt__pull_transpose_through_dequantization>`

* :ref:`LinOpSequenceFusion <lpt_transformations__lin_op_sequence_fusion>`

