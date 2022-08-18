.. index:: pair: page; LogicalOr
.. _doxid-openvino_docs_ops_logical__logical_or_1:


LogicalOr
=========

:target:`doxid-openvino_docs_ops_logical__logical_or_1_1md_openvino_docs_ops_logical_logicalor_1` **Versioned name** : *LogicalOr-1*

**Category** : *Logical binary*

**Short description** : *LogicalOr* performs element-wise logical OR operation with two given tensors applying multi-directional broadcast rules.

**Detailed description** : Before performing logical operation, input tensors *a* and *b* are broadcasted if their shapes are different and ``auto_broadcast`` attributes is not ``none``. Broadcasting is performed according to ``auto_broadcast`` value.

After broadcasting *LogicalOr* does the following with the input tensors *a* and *b* :

.. math::

	o_{i} = a_{i} \lor b_{i}

**Attributes** :

* *auto_broadcast*
  
  * **Description** : specifies rules used for auto-broadcasting of input tensors.
  
  * **Range of values** :
    
    * *none* - no auto-broadcasting is allowed, all input shapes must match
    
    * *numpy* - numpy broadcasting rules, description is available in :ref:`Broadcast Rules For Elementwise Operations <doxid-openvino_docs_ops_broadcast_rules>`,
    
    * *pdpd* - PaddlePaddle-style implicit broadcasting, description is available in :ref:`Broadcast Rules For Elementwise Operations <doxid-openvino_docs_ops_broadcast_rules>`.
  
  * **Type** : string
  
  * **Default value** : "numpy"
  
  * **Required** : *no*

**Inputs**

* **1** : A tensor of type *T_BOOL* and arbitrary shape. **Required.**

* **2** : A tensor of type *T_BOOL* and arbitrary shape. **Required.**

**Outputs**

* **1** : The result of element-wise *LogicalOr* operation. A tensor of type *T_BOOL* and the same shape equal to broadcasted shape of two inputs.

**Types**

* *T_BOOL* : ``boolean``.

**Examples**

*Example 1: no broadcast*

.. ref-code-block:: cpp

	<layer ... type="LogicalOr">
	    <input>
	        <port id="0">
	            <dim>256</dim>
	            <dim>56</dim>
	        </port>
	        <port id="1">
	            <dim>256</dim>
	            <dim>56</dim>
	        </port>
	    </input>
	    <output>
	        <port id="2">
	            <dim>256</dim>
	            <dim>56</dim>
	        </port>
	    </output>
	</layer>

*Example 2: numpy broadcast*

.. ref-code-block:: cpp

	<layer ... type="LogicalOr">
	    <input>
	        <port id="0">
	            <dim>8</dim>
	            <dim>1</dim>
	            <dim>6</dim>
	            <dim>1</dim>
	        </port>
	        <port id="1">
	            <dim>7</dim>
	            <dim>1</dim>
	            <dim>5</dim>
	        </port>
	    </input>
	    <output>
	        <port id="2">
	            <dim>8</dim>
	            <dim>7</dim>
	            <dim>6</dim>
	            <dim>5</dim>
	        </port>
	    </output>
	</layer>

