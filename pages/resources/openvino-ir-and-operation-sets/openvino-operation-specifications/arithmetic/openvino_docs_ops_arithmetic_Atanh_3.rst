.. index:: pair: page; Atanh
.. _doxid-openvino_docs_ops_arithmetic__atanh_3:


Atanh
=====

:target:`doxid-openvino_docs_ops_arithmetic__atanh_3_1md_openvino_docs_ops_arithmetic_atanh_3` **Versioned name** : *Atanh-3*

**Category** : *Arithmetic unary*

**Short description** : *Atanh* performs element-wise hyperbolic inverse tangent (arctangenth) operation with a given tensor.

**Detailed description** : *Atanh* performs element-wise hyperbolic inverse tangent (arctangenth) operation on a given input tensor, based on the following mathematical formula:

Float type input:

.. math::

	a_{i} = atanh(a_{i})

Signed Intragral type put:

.. math::

	a_{i} = (i <= -1) ? std::numeric_limits<T>::min() : (i >= 1) ? std::numeric_limits<T>::max() : atanh(a_{i})

Unsigned Intragral type put:

.. math::

	a_{i} = (i > 0) ? std::numeric_limits<T>::max() : atanh(a_{i})

**Attributes** : Atanh operation has no attributes.

**Inputs**

* **1** : A tensor of type *T*. **Required.**

**Outputs**

* **1** : The result of element-wise atanh operation applied to the input tensor. A tensor of type *T* and the same shape as input tensor.

**Types**

* *T* : any supported numeric type.

**Examples**

.. ref-code-block:: cpp

	<layer ... type="Atanh">
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

