.. index:: pair: page; Atan
.. _doxid-openvino_docs_ops_arithmetic__atan_1:


Atan
====

:target:`doxid-openvino_docs_ops_arithmetic__atan_1_1md_openvino_docs_ops_arithmetic_atan_1` **Versioned name** : *Atan-1*

**Category** : *Arithmetic unary*

**Short description** : *Atan* performs element-wise inverse tangent (arctangent) operation with given tensor.

**Detailed description** : Operation takes one input tensor and performs the element-wise inverse tangent function on a given input tensor, based on the following mathematical formula:

.. math::

	a_{i} = atan(a_{i})

**Attributes** : *Atan* operation has no attributes.

**Inputs**

* **1** : A tensor of type *T* and arbitrary shape. **Required.**

**Outputs**

* **1** : The result of element-wise *Atan* applied to the input tensor. A tensor of type *T* and same shape as the input tensor.

**Types**

* *T* : any supported numeric type.

**Examples**

.. ref-code-block:: cpp

	<layer ... type="Atan">
	    <input>
	        <port id="0">
	            <dim>256</dim>
	            <dim>56</dim>
	        </port>
	    </input>
	    <output>
	        <port id="1">
	            <dim>256</dim>
	            <dim>56</dim>
	        </port>
	    </output>
	</layer>

