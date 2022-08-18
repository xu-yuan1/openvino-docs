.. index:: pair: page; Abs
.. _doxid-openvino_docs_ops_arithmetic__abs_1:


Abs
===

:target:`doxid-openvino_docs_ops_arithmetic__abs_1_1md_openvino_docs_ops_arithmetic_abs_1` **Versioned name** : *Abs-1*

**Category** : *Arithmetic unary*

**Short description** : *Abs* performs element-wise the absolute value with given tensor.

**Attributes** :

.. code-block:: cpp

	No attributes available.

**Inputs**

* **1** : An tensor of type *T*. **Required.**

**Outputs**

* **1** : The result of element-wise abs operation. A tensor of type *T*.

**Types**

* *T* : any numeric type.

*Abs* does the following with the input tensor *a* :

.. math::

	a_{i} = \vert a_{i} \vert

**Examples**

*Example 1*

.. ref-code-block:: cpp

	<layer ... type="Abs">
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

