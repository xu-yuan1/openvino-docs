.. index:: pair: page; SquaredDifference
.. _doxid-openvino_docs_ops_arithmetic__squared_difference_1:


SquaredDifference
=================

:target:`doxid-openvino_docs_ops_arithmetic__squared_difference_1_1md_openvino_docs_ops_arithmetic_squareddifference_1` **Versioned name** : *SquaredDifference-1*

**Category** : *Arithmetic binary*

**Short description** : *SquaredDifference* performs element-wise subtract and square the result operation with two given tensors applying broadcasting rule specified in the *auto_broadcast* attribute.

**Detailed description** As a first step input tensors *a* and *b* are broadcasted if their shapes differ. Broadcasting is performed according to ``auto_broadcast`` attribute specification. As a second step *Substract* and *Square* the result operation is computed element-wise on the input tensors *a* and *b* according to the formula below:

.. math::

	o_{i} = (a_{i} - b_{i})^2

**Attributes** :

* *auto_broadcast*
  
  * **Description** : specifies rules used for auto-broadcasting of input tensors.
  
  * **Range of values** :
    
    * *none* - no auto-broadcasting is allowed, all input shapes must match
    
    * *numpy* - numpy broadcasting rules, description is available in :ref:`Broadcast Rules For Elementwise Operations <doxid-openvino_docs_ops_broadcast_rules>`
  
  * **Type** : string
  
  * **Default value** : "numpy"
  
  * **Required** : *no*

**Inputs**

* **1** : A tensor of type *T* and arbitrary shape. **Required.**

* **2** : A tensor of type *T* and arbitrary shape. **Required.**

**Outputs**

* **1** : The result of element-wise subtract and square the result operation. A tensor of type *T* with shape equal to broadcasted shape of two inputs.

**Types**

* *T* : any numeric type.

**Examples**

*Example 1 - no broadcasting*

.. ref-code-block:: cpp

	<layer ... type="SquaredDifference">
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

*Example 2: numpy broadcasting*

.. ref-code-block:: cpp

	<layer ... type="SquaredDifference">
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

