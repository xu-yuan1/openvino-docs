.. index:: pair: page; Add
.. _doxid-openvino_docs_ops_arithmetic__add_1:


Add
===

:target:`doxid-openvino_docs_ops_arithmetic__add_1_1md_openvino_docs_ops_arithmetic_add_1` **Versioned name** : *Add-1*

**Category** : *Arithmetic binary*

**Short description** : *Add* performs element-wise addition operation with two given tensors applying broadcasting rule specified in the *auto_broacast* attribute.

**Detailed description** Before performing arithmetic operation, input tensors *a* and *b* are broadcasted if their shapes are different and ``auto_broadcast`` attribute is not ``none``. Broadcasting is performed according to ``auto_broadcast`` value. After broadcasting *Add* performs addition operation for the input tensors *a* and *b* using the formula below:

.. math::

	o_{i} = a_{i} + b_{i}

**Attributes** :

* *auto_broadcast*
  
  * **Description** : specifies rules used for auto-broadcasting of input tensors.
  
  * **Range of values** :
    
    * *none* - no auto-broadcasting is allowed, all input shapes must match,
    
    * *numpy* - numpy broadcasting rules, description is available in :ref:`Broadcast Rules For Elementwise Operations <doxid-openvino_docs_ops_broadcast_rules>`,
    
    * *pdpd* - PaddlePaddle-style implicit broadcasting, description is available in :ref:`Broadcast Rules For Elementwise Operations <doxid-openvino_docs_ops_broadcast_rules>`.
  
  * **Type** : string
  
  * **Default value** : "numpy"
  
  * **Required** : *no*

**Inputs**

* **1** : A tensor of type *T* and arbitrary shape and rank. **Required.**

* **2** : A tensor of type *T* and arbitrary shape and rank. **Required.**

**Outputs**

* **1** : The result of element-wise addition operation. A tensor of type *T* with shape equal to broadcasted shape of the two inputs.

**Types**

* *T* : any numeric type.

**Examples**

*Example 1*

.. ref-code-block:: cpp

	<layer ... type="Add">
	    <data auto_broadcast="none"/>
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

*Example 2: broadcast*

.. ref-code-block:: cpp

	<layer ... type="Add">
	    <data auto_broadcast="numpy"/>
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

