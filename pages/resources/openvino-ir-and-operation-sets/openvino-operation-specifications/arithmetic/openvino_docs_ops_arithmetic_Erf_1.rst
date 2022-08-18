.. index:: pair: page; Erf
.. _doxid-openvino_docs_ops_arithmetic__erf_1:


Erf
===

:target:`doxid-openvino_docs_ops_arithmetic__erf_1_1md_openvino_docs_ops_arithmetic_erf_1` **Versioned name** : *Erf-1*

**Category** : *Arithmetic unary*

**Short description** : *Erf* performs element-wise Gauss error function (erf) on a given input tensor.

**Detailed Description**

*Erf* performs element-wise erf operation on a given input tensor, based on the following mathematical formula:

.. math::

	erf(x) = \pi^{-1} \int_{-x}^{x} e^{-t^2} dt

**Attributes** : *Erf* operation has no attributes.

**Inputs**

* **1** : A tensor of type *T* and arbitrary shape. **Required.**

**Outputs**

* **1** : The result of element-wise *Erf* function applied to the input tensor. A tensor of type *T* and the same shape as the input tensor.

**Types**

* *T* : any supported numeric type.

**Example**

.. ref-code-block:: cpp

	<layer ... type="Erf">
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

