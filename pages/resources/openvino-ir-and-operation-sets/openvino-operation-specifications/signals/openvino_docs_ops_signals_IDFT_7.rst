.. index:: pair: page; Inverse Discrete Fourier Transformation (IDFT)
.. _doxid-openvino_docs_ops_signals__i_d_f_t_7:


Inverse Discrete Fourier Transformation (IDFT)
==============================================

:target:`doxid-openvino_docs_ops_signals__i_d_f_t_7_1md_openvino_docs_ops_signals_idft_7` **Versioned name** : *IDFT-7*

**Category** : *Signal processing*

**Short description** : *IDFT* operation performs the inverse discrete Fourier transformation of input tensor by specified dimensions.

**Attributes** :

.. code-block:: cpp

	No attributes available.

**Inputs**

* **1** : ``data`` - Input tensor of type *T* with data for the IDFT transformation. Type of elements is any supported floating-point type. The last dimension of the input tensor must be equal to 2, that is the input tensor shape must have the form ``[D_0, D_1, ..., D_{N-1}, 2]``, representing the real and imaginary components of complex numbers in ``[:, ..., :, 0]`` and in ``[:, ..., :, 1]`` correspondingly. **Required.**

* **2** : **2** : ``axes`` - 1D tensor of type *T_IND* specifying dimension indices where IDFT is applied, and ``axes`` is any unordered list of indices of different dimensions of input tensor, for example, ``[0, 4]``, ``[4, 0]``, ``[4, 2, 1]``, ``[1, 2, 3]``, ``[-3, 0, -2]``. These indices should be integers from ``-(r - 1)`` to ``(r - 2)`` inclusively, where ``r = rank(data)``. A negative axis ``a`` is interpreted as an axis ``r - 1 + a``. Other dimensions do not change. The order of elements in ``axes`` attribute matters, and is mapped directly to elements in the third input ``signal_size``. **Required.**

* **NOTE** : The following constraint must be satisfied: ``rank(data) >= len(axes) + 1 and input_shape[-1] == 2 and (rank(data) - 1) not in axes and (-1) not in axes``.

* **3** : ``signal_size`` - 1D tensor of type *T_SIZE* describing signal size with respect to axes from the input ``axes``. If ``signal_size[i] == -1``, then IDFT is calculated for full size of the axis ``axes[i]``. If ``signal_size[i] > input_shape[: r - 1][axes[i]]``, then input data are zero-padded with respect to the axis ``axes[i]`` at the end. Finally, if ``signal_size[i] < input_shape[: r - 1][axes[i]]``, then input data are trimmed with respect to the axis ``axes[i]``. More precisely, if ``signal_size[i] < input_shape[: r - 1][axes[i]]``, the slice ``0: signal_size[i]`` of the axis ``axes[i]`` is considered. Optional, with default value ``[input_shape[: r - 1][a] for a in axes]``.

* **NOTE** : If the input ``signal_size`` is specified, then the size of ``signal_size`` must be the same as the size of ``axes``.

**Outputs**

* **1** : Resulting tensor with elements of the same type as input ``data`` tensor. The shape of the output is calculated as follows. If the input ``signal_size`` is not specified, then the shape of output is the same as the shape of ``data``. Otherwise, ``output_shape[axis] = input_shape[axis]`` for ``axis not in axes``, and if ``signal_size[i] == -1``, then ``output_shape[: r - 1][axes[i]] = input_shape[: r - 1][axes[i]]``, else ``output_shape[: r - 1][axes[i]] = signal_size[i]``.

**Types**

* *T* : floating-point type.

* *T_IND* : ``int64`` or ``int32``.

* *T_SIZE* : ``int64`` or ``int32``.

**Detailed description** : *IDFT* performs the discrete Fourier transformation of input tensor, according to the following rules.

For simplicity, assume that an input tensor ``A`` has the shape ``[B_0, ..., B_{k-1}, M_0, ..., M_{r-1}, 2]``, ``axes=[k+1,...,k+r]``, and ``signal_size=[S_0,...,S_{r-1}]``.

Let ``D`` be an input tensor ``A``, taking into account the ``signal_size``, and, hence, ``D`` has the shape ``[B_0, ..., B_{k-1}, S_0, ..., S_{r-1}, 2]``.

Next, put

.. math::

	X[j_0,\dots,j_{k-1},j_k,\dots,j_{k+r}]=D[j_0,\dots,j_{k-1},j_k,\dots,j_{k+r},0]+iD[j_0,\dots,j_{k-1},j_k,\dots,j_{k+r},1]

for all indices ``j_0,...,j_{k+r}``, where ``i`` is an imaginary unit, that is ``X`` is a complex tensor.

Then the inverse discrete Fourier transform is the tensor ``Y`` of the same shape as the tensors ``X``, such that

.. math::

	Y[n_0,\dots,n_{k-1},m_0,\dots,m_{r-1}]=\frac{1}{\prod\limits_{j=0}^{r-1}S_j}\sum\limits_{p_0=0}^{S_0}\cdots\sum\limits_{p_{r-1}=0}^{S_{r-1}}X[n_0,\dots,n_{k-1},j_0,\dots,j_{r-1}]\exp\left(2\pi i\sum\limits_{q=0}^{r-1}\frac{m_qj_q}{S_s}\right)

for all indices ``n_0,...,n_{k-1}``, ``m_0,...,m_{r-1}``, and the result of the operation is the real tensor ``Z`` with the shape ``[B_0, ..., B_{k-1}, S_0, ..., S_{r-1}, 2]`` and such that

.. math::

	Z[n_0,\dots,n_{k-1},m_0,\dots,m_{r-1}, 0]=Re Y[n_0,\dots,n_{k-1},m_0,\dots,m_{r-1}],



.. math::

	Z[n_0,\dots,n_{k-1},m_0,\dots,m_{r-1}, 1]=Im Y[n_0,\dots,n_{k-1},m_0,\dots,m_{r-1}].

Calculations for the generic case of axes and signal sizes are similar.

**Example** :

There is no ``signal_size`` input (4D input tensor):

.. ref-code-block:: cpp

	<layer ... type="IDFT" ... >
	    <input>
	        <port id="0">
	            <dim>1</dim>
	            <dim>320</dim>
	            <dim>320</dim>
	            <dim>2</dim>
	        </port>
	        <port id="1">
	            <dim>2</dim> <!-- [1, 2] -->
	        </port>
	    <output>
	        <port id="2">
	            <dim>1</dim>
	            <dim>320</dim>
	            <dim>320</dim>
	            <dim>2</dim>
	        </port>
	    </output>
	</layer>

There is no ``signal_size`` input (3D input tensor):

.. ref-code-block:: cpp

	<layer ... type="IDFT" ... >
	    <input>
	        <port id="0">
	            <dim>320</dim>
	            <dim>320</dim>
	            <dim>2</dim>
	        </port>
	        <port id="1">
	            <dim>2</dim> <!-- [0, 1] -->
	        </port>
	    <output>
	        <port id="2">
	            <dim>320</dim>
	            <dim>320</dim>
	            <dim>2</dim>
	        </port>
	    </output>
	</layer>

There is ``signal_size`` input (4D input tensor):

.. ref-code-block:: cpp

	<layer ... type="IDFT" ... >
	    <input>
	        <port id="0">
	            <dim>1</dim>
	            <dim>320</dim>
	            <dim>320</dim>
	            <dim>2</dim>
	        </port>
	        <port id="1">
	            <dim>2</dim> <!-- [1, 2] -->
	        </port>
	        <port id="2">
	            <dim>2</dim> <!-- [512, 100] -->
	        </port>
	    <output>
	        <port id="3">
	            <dim>1</dim>
	            <dim>512</dim>
	            <dim>100</dim>
	            <dim>2</dim>
	        </port>
	    </output>
	</layer>

There is ``signal_size`` input (3D input tensor):

.. ref-code-block:: cpp

	<layer ... type="IDFT" ... >
	    <input>
	        <port id="0">
	            <dim>320</dim>
	            <dim>320</dim>
	            <dim>2</dim>
	        </port>
	        <port id="1">
	            <dim>2</dim> <!-- [0, 1] -->
	        </port>
	        <port id="2">
	            <dim>2</dim> <!-- [512, 100] -->
	        </port>
	    <output>
	        <port id="3">
	            <dim>512</dim>
	            <dim>100</dim>
	            <dim>2</dim>
	        </port>
	    </output>
	</layer>

There is ``signal_size`` input (5D input tensor, ``-1`` in ``signal_size``, unsorted axes):

.. ref-code-block:: cpp

	<layer ... type="IDFT" ... >
	    <input>
	        <port id="0">
	            <dim>16</dim>
	            <dim>768</dim>
	            <dim>580</dim>
	            <dim>320</dim>
	            <dim>2</dim>
	        </port>
	        <port id="1">
	            <dim>3</dim> <!-- axes input contains  [3, 1, 2] -->
	        </port>
	        <port id="2">
	            <dim>3</dim> <!-- signal_size input contains [170, -1, 1024] -->
	        </port>
	    <output>
	        <port id="3">
	            <dim>16</dim>
	            <dim>768</dim>
	            <dim>1024</dim>
	            <dim>170</dim>
	            <dim>2</dim>
	        </port>
	    </output>
	</layer>

There is ``signal_size`` input (5D input tensor, ``-1`` in ``signal_size``, unsorted axes, the second example):

.. ref-code-block:: cpp

	<layer ... type="IDFT" ... >
	    <input>
	        <port id="0">
	            <dim>16</dim>
	            <dim>768</dim>
	            <dim>580</dim>
	            <dim>320</dim>
	            <dim>2</dim>
	        </port>
	        <port id="1">
	            <dim>3</dim> <!-- axes input contains  [3, 0, 2] -->
	        </port>
	        <port id="2">
	            <dim>3</dim> <!-- signal_size input contains [258, -1, 2056] -->
	        </port>
	    <output>
	        <port id="3">
	            <dim>16</dim>
	            <dim>768</dim>
	            <dim>2056</dim>
	            <dim>258</dim>
	            <dim>2</dim>
	        </port>
	    </output>
	</layer>

