.. index:: pair: page; SoftSign
.. _doxid-openvino_docs_ops_activation__soft_sign_9:


SoftSign
========

:target:`doxid-openvino_docs_ops_activation__soft_sign_9_1md_openvino_docs_ops_activation_softsign_9` **Versioned name** : *SoftSign-9*

**Category** : *Activation function*

**Short description** : *SoftSign* performs element-wise activation on a given input tensor.

**Detailed description** :

*SoftSign* operation is introduced in this `article <https://arxiv.org/abs/2010.09458>`__.

*SoftSign Activation Function* is a neuron activation function based on the mathematical function:

.. math::

	SoftSign(x) = \frac{x}{1+|x|}

**Inputs** :

* **1** : ``data``. Input tensor of type *T*

**Outputs** :

* **1** : The resulting tensor of the same shape and type as the input tensor.

**Types** :

* **T** : Arbitrary supported floating-point type.

**Example**

.. ref-code-block:: cpp

	<layer ... type="SoftSign">
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

