.. index:: pair: page; QuantizationAlignment attribute
.. _lpt_attributes__quantizationalignment:

.. meta::
   :description: Information about QuantizationAlignment attribute.
   :keywords: low precision transformation, lpt, low precision transformation attributes,
              QuantizationAlignment


QuantizationAlignment attribute
===============================

:target:`lpt_attributes__quantizationalignment_1md_openvino_docs_ie_plugin_dg_plugin_transformation_pipeline_low_precision_transformations_attributes_quantization_alignment` :ref:`ngraph::QuantizationAlignmentAttribute <doxid-classngraph_1_1_quantization_alignment_attribute>` 
class represents the ``QuantizationAlignment`` attribute.

The attribute defines a subgraph with the same quantization alignment. ``FakeQuantize`` operations are not included. 
The attribute is used by quantization operations.

.. list-table::
    :header-rows: 1

    * - Property name
      - Values
    * - Required
      - Yes
    * - Defined
      - Operation
    * - Properties
      - value (boolean)

