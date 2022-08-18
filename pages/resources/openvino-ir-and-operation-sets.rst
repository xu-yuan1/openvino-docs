.. index:: pair: page; Deep Learning Network Intermediate Representation and Operation Sets in OpenVINO™
.. _doxid-openvino_docs__m_o__d_g__i_r_and_opsets:


Deep Learning Network Intermediate Representation and Operation Sets in OpenVINO™
===================================================================================

:target:`doxid-openvino_docs__m_o__d_g__i_r_and_opsets_1md_openvino_docs_mo_dg_ir_and_opsets` This article provides essential information on the format used for representation of deep learning models in OpenVINO toolkit and supported operation sets.


.. toctree::
   :maxdepth: 1
   :caption: OpenVINO IR and Operation Sets
   :hidden:

   ./openvino-ir-and-operation-sets/broadcast-rules-for-elementwise-operations.rst
   ./openvino-ir-and-operation-sets/IR-for-int8-inference.rst
   ./openvino-ir-and-operation-sets/openvino-operation-sets.rst
   ./openvino-ir-and-operation-sets/openvino-operation-specifications



Overview of Artificial Neural Networks Representation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A deep learning network is usually represented as a directed graph describing the flow of data from the network input data to the inference results. Input data can be in the form of images, video, audio, or preprocessed information representing objects from the target area of interest.

Here is an illustration of a small graph representing a model that consists of a single Convolutional layer and activation function:

.. image:: _assets/small_IR_graph_demonstration.png

Vertices in the graph represent layers or operation instances such as convolution, pooling, and element-wise operations with tensors. The terms of "layer" and "operation" are used interchangeably within OpenVINO documentation and define how input data is processed to produce output data for a node in a graph. An operation node in a graph may consume data at one or multiple input ports. For example, an element-wise addition operation has two input ports which accept tensors that are to be summed. Some operations do not have any input ports, for example the ``Const`` operation, which knows the data to be produced without any input. An edge between operations represents data flow or data dependency implied from one operation node to another.

Each operation produces data on one or multiple output ports. For example, convolution produces output tensor with activations at a single output port. Split operation usually has multiple output ports, each producing part of an input tensor.

Depending on a deep learning framework, the graph can also contain extra nodes that explicitly represent tensors between operations. In such representations, operation nodes are not connected to each other directly. They are rather using data nodes as intermediate stops for data flow. If data nodes are not used, the produced data is associated with an output port of a corresponding operation node that produces the data.

A set of various operations used in a network is usually fixed for each deep learning framework. It determines expressiveness and level of representation available in that framework. Sometimes, a network that can be represented in one framework is hard or impossible to be represented in another one or should use significantly different graph, because operation sets used in those two frameworks do not match.

Intermediate Representation Used in OpenVINO
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

OpenVINO toolkit introduces its own format of graph representation and its own operation set. A graph is represented with two files: an XML file and a binary file. This representation is commonly referred to as the *Intermediate Representation* or *IR*.

The XML file describes a network topology using a ``<layer>`` tag for an operation node and an ``<edge>`` tag for a data-flow connection. Each operation has a fixed number of attributes that define operation flavor used for a node. For example, the ``Convolution`` operation has such attributes as ``dilation``, ``stride``, ``pads_begin``, and ``pads_end``.

The XML file does not have big constant values like convolution weights. Instead, it refers to a part of the accompanying binary file that stores such values in a binary format.

Here is an example of a small IR XML file that corresponds to a graph from the previous section:

.. ref-code-block:: cpp

	<?xml version="1.0" ?>
	<net name="model_file_name" version="10">
	    <layers>
	        <layer id="0" name="input" type="Parameter" version="opset1">
	            <data element_type="f32" shape="1,3,32,100"/> <!-- attributes of operation -->
	            <output>
	                <!-- description of output ports with type of element and tensor dimensions -->
	                <port id="0" precision="FP32">
	                    <dim>1</dim>
	                    <dim>3</dim>
	                    <dim>32</dim>
	                    <dim>100</dim>
	                </port>
	            </output>
	        </layer>
	        <layer id="1" name="conv1/weights" type="Const" version="opset1">
	            <!-- Const is only operation from opset1 that refers to the IR binary file by specifying offset and size in bytes relative to the beginning of the file. -->
	            <data element_type="f32" offset="0" shape="64,3,3,3" size="6912"/>
	            <output>
	                <port id="1" precision="FP32">
	                    <dim>64</dim>
	                    <dim>3</dim>
	                    <dim>3</dim>
	                    <dim>3</dim>
	                </port>
	            </output>
	        </layer>
	        <layer id="2" name="conv1" type="Convolution" version="opset1">
	            <data auto_pad="same_upper" dilations="1,1" output_padding="0,0" pads_begin="1,1" pads_end="1,1" strides="1,1"/>
	            <input>
	                <port id="0">
	                    <dim>1</dim>
	                    <dim>3</dim>
	                    <dim>32</dim>
	                    <dim>100</dim>
	                </port>
	                <port id="1">
	                    <dim>64</dim>
	                    <dim>3</dim>
	                    <dim>3</dim>
	                    <dim>3</dim>
	                </port>
	            </input>
	            <output>
	                <port id="2" precision="FP32">
	                    <dim>1</dim>
	                    <dim>64</dim>
	                    <dim>32</dim>
	                    <dim>100</dim>
	                </port>
	            </output>
	        </layer>
	        <layer id="3" name="conv1/activation" type="ReLU" version="opset1">
	            <input>
	                <port id="0">
	                    <dim>1</dim>
	                    <dim>64</dim>
	                    <dim>32</dim>
	                    <dim>100</dim>
	                </port>
	            </input>
	            <output>
	                <port id="1" precision="FP32">
	                    <dim>1</dim>
	                    <dim>64</dim>
	                    <dim>32</dim>
	                    <dim>100</dim>
	                </port>
	            </output>
	        </layer>
	        <layer id="4" name="output" type="Result" version="opset1">
	            <input>
	                <port id="0">
	                    <dim>1</dim>
	                    <dim>64</dim>
	                    <dim>32</dim>
	                    <dim>100</dim>
	                </port>
	            </input>
	        </layer>
	    </layers>
	    <edges>
	        <!-- Connections between layer nodes: based on ids for layers and ports used in the descriptions above -->
	        <edge from-layer="0" from-port="0" to-layer="2" to-port="0"/>
	        <edge from-layer="1" from-port="1" to-layer="2" to-port="1"/>
	        <edge from-layer="2" from-port="2" to-layer="3" to-port="0"/>
	        <edge from-layer="3" from-port="1" to-layer="4" to-port="0"/>
	    </edges>
	    <meta_data>
	        <!-- This section that is not related to a topology; contains auxiliary information that serves for the debugging purposes. -->
	        <MO_version value="2019.1"/>
	        <cli_parameters>
	            <blobs_as_inputs value="True"/>
	            <caffe_parser_path value="DIR"/>
	            <data_type value="float"/>
	
	            ...
	
	            <!-- Omitted a long list of CLI options that always are put here by MO for debugging purposes. -->
	
	        </cli_parameters>
	    </meta_data>
	</net>

The IR does not use explicit data nodes described in the previous section. In contrast, properties of data such as tensor dimensions and their data types are described as properties of input and output ports of operations.

Operation Sets
~~~~~~~~~~~~~~

Operations in OpenVINO Operation Sets are selected based on capabilities of supported deep learning frameworks and hardware capabilities of the target inference device. It consists of several groups of operations:

* Conventional deep learning layers such as ``Convolution``, ``MaxPool``, and ``MatMul`` (also known as ``FullyConnected``).

* Various activation functions such as ``ReLU``, ``Tanh``, and ``PReLU``.

* Generic element-wise arithmetic tensor operations such as ``Add``, ``Subtract``, and ``Multiply``.

* Comparison operations that compare two numeric tensors and produce boolean tensors, for example, ``Less``, ``Equeal``, ``Greater``.

* Logical operations that are dealing with boolean tensors, for example, ``And``, ``Xor``, ``Not``.

* Data movement operations which are dealing with parts of tensors, for example, ``Concat``, ``Split``, ``StridedSlice``, ``Select``.

* Specialized operations that implement complex algorithms dedicated for models of specific type, for example, ``DetectionOutput``, ``RegionYolo``, ``PriorBox``.

For more information, refer to the complete description of the supported operation sets in the :ref:`Available Operation Sets <doxid-openvino_docs_ops_opset>` article.

IR Versions vs Operation Set Versions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The expressiveness of operations in OpenVINO is highly dependent on the supported frameworks and target hardware capabilities. As the frameworks and hardware capabilities grow over time, the operation set is constantly evolving to support new models. To maintain backward compatibility and growing demands, both IR format and operation set have versioning.

Version of IR specifies the rules which are used to read the XML and binary files that represent a model. It defines an XML schema and compatible operation set that can be used to describe operations.

Historically, there are two major IR version epochs:

#. The older one includes IR versions from version 1 to version 7 without versioning of the operation set. During that epoch, the operation set has been growing evolutionally accumulating more layer types and extending existing layer semantics. Changing of the operation set for those versions meant increasing of IR version.

#. OpenVINO 2020.1 is the starting point of the next epoch. With IR version 10 introduced in OpenVINO 2020.1, the versioning of the operation set is tracked separately from the IR versioning. Also, the operation set was significantly reworked as the result of nGraph integration to the OpenVINO.

The first supported operation set in the new epoch is ``opset1``. The number after ``opset`` is going to be increased each time new operations are added or old operations deleted at the release cadence.

The operations from the new epoch cover more TensorFlow and ONNX operators in a form that is closer to the original operation semantics from the frameworks in comparison to the operation set used in former versions of IR (7 and lower).

The name of the opset is specified for each operation in IR. The IR version is specified once per whole IR. Here is an example from the IR snippet:

.. ref-code-block:: cpp

	<?xml version="1.0" ?>
	<net name="model_file_name" version="10">  <!-- Version of the whole IR file is here; it is 10 -->
	    <layers>
	        <!-- Version of operation set that the layer belongs to is described in <layer>
	             tag attributes. For this operation, it is version="opset1". -->
	        <layer id="0" name="input" type="Parameter" version="opset1">
	            <data element_type="f32" shape="1,3,32,100"/> <!-- attributes of operation -->
	            <output>
	                <!-- description of output ports with type of element and tensor dimensions -->
	                <port id="0" precision="FP32">
	                    <dim>1</dim>
	                    <dim>3</dim>
	
	                    ...

The ``type="Parameter"`` and ``version="opset1"`` attributes in the example above mean "use that version of the `Parameter` operation that is included in the `opset1` operation set. "

When a new operation set is introduced, most of the operations remain unchanged and are just aliased from the previous operation set within a new one. The goal of operation set version evolution is to add new operations, and probably change small fractions of existing operations (fixing bugs and extending semantics). However, such changes affect only new versions of operations from a new operation set, while old operations are used by specifying an appropriate ``version``. When an old ``version`` is specified, the behavior will be kept unchanged from that specified version to provide backward compatibility with older IRs.

A single ``xml`` file with IR may contain operations from different opsets. An operation that is included in several opsets may be referred to with ``version`` which points to any opset that includes that operation. For example, the same ``Convolution`` can be used with ``version="opset1"`` and ``version="opset2"`` because both opsets have the same ``Convolution`` operations.

How to Read Opset Specification
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In the :ref:`Available Operation Sets <doxid-openvino_docs_ops_opset>` there are opsets and there are operations. Each opset specification has a list of links to operations descriptions that are included into that specific opset. Two or more opsets may refer to the same operation. That means an operation is kept unchanged from one operation set to another.

The description of each operation has a ``Versioned name`` field. For example, the ``ReLU`` entry point in :ref:``opset1` <doxid-openvino_docs_ops_opset1>` refers to :ref:``ReLU-1` <doxid-openvino_docs_ops_activation__re_l_u_1>` as the versioned name. Meanwhile, ``ReLU`` in ``opset2`` refers to the same ``ReLU-1`` and both ``ReLU`` operations are the same operation and it has a single :ref:`description <doxid-openvino_docs_ops_activation__re_l_u_1>`, which means that ``opset1`` and ``opset2`` share the same operation ``ReLU``.

To differentiate versions of the same operation type such as ``ReLU``, the ``-N`` suffix is used in a versioned name of the operation. The ``N`` suffix usually refers to the first occurrence of ``opsetN`` where this version of the operation is introduced. There is no guarantee that new operations will be named according to that rule. The naming convention might be changed, but not for old operations which are frozen completely.

