.. index:: pair: page; ReLU
.. _doxid-openvino_docs_ops_activation__re_l_u_1:


ReLU
====

:target:`doxid-openvino_docs_ops_activation__re_l_u_1_1md_openvino_docs_ops_activation_relu_1` **Versioned name** : *ReLU-1*

**Category** : *Activation function*

**Short description** : ReLU element-wise activation function. (`Reference <http://caffe.berkeleyvision.org/tutorial/layers/relu.html>`__)

**Detailed description** : `Reference <https://github.com/Kulbear/deep-learning-nano-foundation/wiki/ReLU-and-Softmax-Activation-Functions#rectified-linear-units>`__

**Attributes** : *ReLU* operation has no attributes.

**Mathematical Formulation**

For each element from the input tensor calculates corresponding element in the output tensor with the following formula:

.. math::

	Y_{i}^{( l )} = max(0,\ Y_{i}^{( l - 1 )})

**Inputs** :

* **1** : Multidimensional input tensor *x* of any supported numeric type. **Required.**

**Outputs** :

* **1** : Result of ReLU function applied to the input tensor *x*. Tensor with shape and type matching the input tensor.

**Example**

.. ref-code-block:: cpp

	<layer ... type="ReLU">
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

