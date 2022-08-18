.. index:: pair: page; FakeQuantize
.. _doxid-openvino_docs_ops_quantization__fake_quantize_1:


FakeQuantize
============

:target:`doxid-openvino_docs_ops_quantization__fake_quantize_1_1md_openvino_docs_ops_quantization_fakequantize_1` **Versioned name** : *FakeQuantize-1*

**Category** : *Quantization*

**Short description** : *FakeQuantize* is element-wise linear quantization of floating-point input values into a discrete set of floating-point values.

**Detailed description** : Input and output ranges as well as the number of levels of quantization are specified by dedicated inputs and attributes. There can be different limits for each element or groups of elements (channels) of the input tensors. Otherwise, one limit applies to all elements. It depends on shape of inputs that specify limits and regular broadcasting rules applied for input tensors. The output of the operator is a floating-point number of the same type as the input tensor. In general, there are four values that specify quantization for each element: *input_low*, *input_high*, *output_low*, *output_high*. *input_low* and *input_high* attributes specify the input range of quantization. All input values that are outside this range are clipped to the range before actual quantization. *output_low* and *output_high* specify minimum and maximum quantized values at the output.

*Fake* in *FakeQuantize* means the output tensor is of the same floating point type as an input tensor, not integer type.

Each element of the output is defined as the result of the following expression:

.. ref-code-block:: cpp

	if x <= :ref:`min <doxid-namespacengraph_1_1runtime_1_1reference_1abc42885cb896b121ab5ac214cbf60935>`(input_low, input_high):
	    output = output_low
	elif x > :ref:`max <doxid-namespacengraph_1_1runtime_1_1reference_1a92cfabd79e866544fb35d44884e7adfd>`(input_low, input_high):
	    output = output_high
	else:
	    # input_low < x <= input_high
	    output = :ref:`round <doxid-namespacengraph_1_1runtime_1_1reference_1a8ea383ca6ce01d26eabe1c27a0e1bd37>`((x - input_low) / (input_high - input_low) \* (levels-1)) / (levels-1) \* (output_high - output_low) + output_low

**Attributes**

* *levels*
  
  * **Description** : *levels* is the number of quantization levels (e.g. 2 is for binarization, 255/256 is for int8 quantization)
  
  * **Range of values** : an integer greater than or equal to 2
  
  * **Type** : ``int``
  
  * **Required** : *yes*

* *auto_broadcast*
  
  * **Description** : specifies rules used for auto-broadcasting of input tensors.
  
  * **Range of values** :
    
    * *none* - no auto-broadcasting is allowed, all input shapes should match
    
    * *numpy* - numpy broadcasting rules, description is available in :ref:`Broadcast Rules For Elementwise Operations <doxid-openvino_docs_ops_broadcast_rules>`,
    
    * *pdpd* - PaddlePaddle-style implicit broadcasting, description is available in :ref:`Broadcast Rules For Elementwise Operations <doxid-openvino_docs_ops_broadcast_rules>`.
  
  * **Type** : string
  
  * **Default value** : "numpy"
  
  * **Required** : *no*

**Inputs** :

* **1** : ``X`` - tensor of type *T_F* and arbitrary shape. **Required.**

* **2** : ``input_low`` - tensor of type *T_F* with minimum limit for input value. The shape must be broadcastable to the shape of *X*. **Required.**

* **3** : ``input_high`` - tensor of type *T_F* with maximum limit for input value. Can be the same as ``input_low`` for binarization. The shape must be broadcastable to the shape of *X*. **Required.**

* **4** : ``output_low`` - tensor of type *T_F* with minimum quantized value. The shape must be broadcastable to the shape of *X*. **Required.**

* **5** : ``output_high`` - tensor of type *T_F* with maximum quantized value. The shape must be broadcastable to the of *X*. **Required.**

**Outputs** :

* **1** : output tensor of type *T_F* with shape and type matching the 1st input tensor *X*.

**Types**

* *T_F* : any supported floating point type.

**Example**

.. ref-code-block:: cpp

	<layer … type="FakeQuantize"…>
	    <data levels="2"/>
	    <input>
	        <port id="0">
	            <dim>1</dim>
	            <dim>64</dim>
	            <dim>56</dim>
	            <dim>56</dim>
	        </port>
	        <port id="1">
	            <dim>1</dim>
	            <dim>64</dim>
	            <dim>1</dim>
	            <dim>1</dim>
	        </port>
	        <port id="2">
	            <dim>1</dim>
	            <dim>64</dim>
	            <dim>1</dim>
	            <dim>1</dim>
	        </port>
	        <port id="3">
	            <dim>1</dim>
	            <dim>1</dim>
	            <dim>1</dim>
	            <dim>1</dim>
	        </port>
	        <port id="4">
	            <dim>1</dim>
	            <dim>1</dim>
	            <dim>1</dim>
	            <dim>1</dim>
	        </port>
	    </input>
	    <output>
	        <port id="5">
	            <dim>1</dim>
	            <dim>64</dim>
	            <dim>56</dim>
	            <dim>56</dim>
	        </port>
	    </output>
	</layer>

