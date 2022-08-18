.. index:: pair: page; LogicalNot
.. _doxid-openvino_docs_ops_logical__logical_not_1:


LogicalNot
==========

:target:`doxid-openvino_docs_ops_logical__logical_not_1_1md_openvino_docs_ops_logical_logicalnot_1` **Versioned name** : *LogicalNot-1*

**Category** : *Logical unary*

**Short description** : *LogicalNot* performs element-wise logical negation operation with given tensor.

**Detailed description** : *LogicalNot* performs element-wise logical negation operation with given tensor, based on the following mathematical formula:

.. math::

	a_{i} = \lnot a_{i}

**Attributes** : *LogicalNot* operation has no attributes.

**Inputs**

* **1** : A tensor of type *T_BOOL* and arbitrary shape. **Required.**

**Outputs**

* **1** : The result of element-wise logical negation operation. A tensor of type *T_BOOL* and the same shape as input tensor.

**Types**

* *T_BOOL* : ``boolean``.
  
  .. math::
  
  	a_{i} = \lnot a_{i}

**Example**

.. ref-code-block:: cpp

	<layer ... type="LogicalNot">
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

