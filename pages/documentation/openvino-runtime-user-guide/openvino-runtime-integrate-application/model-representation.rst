.. index:: pair: page; Model Representation in OpenVINO™ Runtime
.. _deploy_infer__model_representation:

.. meta::
   :description: In OpenVINO™ Runtime a model is represented by special classes to work with model data types and shapes.
   :keywords: OpenVINO™ Runtime, model representation, ov::Model, ov:Model class, 
              model inputs, model outputs, representation of shapes, representation 
              of operations, representation of operation sets, tensor, ov::Shape, 
              ov:Shape class, ov::PartialShape, ov:PartialShape class, static shapes, 
              dynamic shapes, operation set, ov::OpSet, model debugging

Model Representation in OpenVINO™ Runtime
===========================================

:target:`deploy_infer__model_representation_1md_openvino_docs_ov_runtime_ug_model_representation` 

In OpenVINO™ Runtime, a model is represented by the ``:ref:`ov::Model <doxid-classov_1_1_model>``` 
class.

The ``:ref:`ov::Model <doxid-classov_1_1_model>``` object stores shared pointers 
to ``:ref:`ov::op::v0::Parameter <doxid-classov_1_1op_1_1v0_1_1_parameter>```, 
``:ref:`ov::op::v0::Result <doxid-classov_1_1op_1_1v0_1_1_result>```, and 
``:ref:`ov::op::Sink <doxid-classov_1_1op_1_1_sink>``` operations, which are 
inputs, outputs, and sinks of the graph. Sinks of the graph have no consumers 
and are not included in the results vector. All other operations hold each 
other via shared pointers, in which a child operation holds its parent via a 
hard link. If an operation has no consumers and is neither the ``Result`` nor 
the ``Sink`` operation whose shared pointer counter is zero, the operation will 
be destructed and not be accessible anymore.

Each operation in ``:ref:`ov::Model <doxid-classov_1_1_model>``` has the 
``std::shared_ptr<:ref:`ov::Node <doxid-classov_1_1_node>`>`` type.

How OpenVINO Runtime Works with Models
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

OpenVINO™ Runtime enables you to use different approaches to work with model 
inputs/outputs:

* The ``:ref:`ov::Model::inputs() <doxid-classov_1_1_model_1ac28a4c66071e165c4f98906ab489e5d5>``` 
  / ``:ref:`ov::Model::outputs() <doxid-classov_1_1_model_1af6e381008712ce22d6f4b93b87303dd8>``` 
  methods are used to get vectors of all input/output ports.

* For a model that has only one input or output, you can use the 
  ``:ref:`ov::Model::input() <doxid-classov_1_1_model_1a5deeced6688795bc6cdad9ce74d972e7>``` 
  or ``:ref:`ov::Model::output() <doxid-classov_1_1_model_1a54c76c98bc7dd8fb04e866d06134efc7>``` 
  methods without any arguments to get input or output port respectively.

* The ``:ref:`ov::Model::input() <doxid-classov_1_1_model_1a5deeced6688795bc6cdad9ce74d972e7>``` 
  and ``:ref:`ov::Model::output() <doxid-classov_1_1_model_1a54c76c98bc7dd8fb04e866d06134efc7>``` 
  methods can be used with the index of inputs or outputs from the framework 
  model to get specific ports by index.

* You can use the tensor name of input or output from the original framework 
  model together with the ``:ref:`ov::Model::input() <doxid-classov_1_1_model_1a5deeced6688795bc6cdad9ce74d972e7>``` 
  or ``:ref:`ov::Model::output() <doxid-classov_1_1_model_1a54c76c98bc7dd8fb04e866d06134efc7>``` 
  methods to get specific ports. It means that you do not need to have any 
  additional mapping of names from framework to OpenVINO as it was before. 
  OpenVINO™ Runtime allows the usage of native framework tensor names, 
  for example:

.. tab:: C++

   .. doxygensnippet:: ../../../snippets/ov_model_snippets.cpp
      :language: cpp
      :fragment: all_inputs_ouputs

.. tab:: Python

   .. doxygensnippet:: ../../../snippets/ov_model_snippets.py
      :language: python
      :fragment: all_inputs_ouputs


For details on how to build a model in OpenVINO™ Runtime, see the 
:ref:`Build a Model in OpenVINO™ Runtime <deploy_infer__model_representation_1ov_ug_build_model>` 
section.

OpenVINO™ Runtime model representation uses special classes to work with model 
data types and shapes. The ``:ref:`ov::element::Type <doxid-classov_1_1element_1_1_type>``` 
is used for data types. See the section below for representation of shapes.

Representation of Shapes
~~~~~~~~~~~~~~~~~~~~~~~~

OpenVINO™ Runtime provides two types for shape representation:

* ``:ref:`ov::Shape <doxid-classov_1_1_shape>``` - Represents static (fully 
  defined) shapes.

* ``:ref:`ov::PartialShape <doxid-classov_1_1_partial_shape>``` - Represents 
  dynamic shapes. This means that the rank or some of dimensions are dynamic 
  (dimension defines an interval or undefined).

``:ref:`ov::PartialShape <doxid-classov_1_1_partial_shape>``` can be converted 
to ``:ref:`ov::Shape <doxid-classov_1_1_shape>``` by using the ``get_shape()`` 
method if all dimensions are static; otherwise, the conversion will throw an 
exception. For example:

.. tab:: C++

   .. ref-code-block:: cpp

      :ref:`ov::Shape <doxid-classov_1_1_shape>` static_shape;
      :ref:`ov::PartialShape <doxid-classov_1_1_partial_shape>` partial_shape = node->output(0).get_partial_shape(); // get zero output partial shape
      if (!partial_shape.:ref:`is_dynamic <doxid-classov_1_1_partial_shape_1a3c2f6e07a5415648ce1654831d6be035>`() /\* or partial_shape.is_static() \*/) {
          static_shape = partial_shape.:ref:`get_shape <doxid-classov_1_1_partial_shape_1a7973b448c76e208993190d2e1e5d7a4a>`();
      }

.. tab:: Python

   .. ref-code-block:: cpp

      partial_shape = node.output(0).get_partial_shape() # get zero output partial shape
      if not partial_shape.is_dynamic: # or partial_shape.is_static
          static_shape = partial_shape.get_shape()


However, in most cases, before getting static shape using the ``get_shape()`` 
method, you need to check if that shape is static.

Representation of Operations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The ``ov::Op`` class represents any abstract operation in the model 
representation. Use this class to create :ref:`custom operations <extensibility__custom_operations>`.

Representation of Operation Sets
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

An operation set (opset) is a collection of operations that can be used to 
construct a model. The ``:ref:`ov::OpSet <doxid-classov_1_1_op_set>``` class 
provides the functionality to work with operation sets. For each operation set, 
OpenVINO™ Runtime provides a separate namespace, for example ``opset8``.

Each OpenVINO™ Release introduces new operations and adds them to new operation 
sets, within which the new operations would change the behavior of previous 
operations. Using operation sets helps you avoid changing your application when 
new operations are introduced. For a complete list of operation sets supported 
in OpenVINO™ toolkit, see the :ref:`Available Operations Sets <doxid-openvino_docs_ops_opset>`. 
To add the support for custom operations, see :ref:`OpenVINO Extensibility Mechanism <extensibility__api_introduction>`.

.. _deploy_infer__model_representation_1ov_ug_build_model:

Building a Model in OpenVINO™ Runtime
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can create a model from source. This section illustrates how to construct 
a model composed of operations from an available operation set.

Operation set ``opsetX`` integrates a list of pre-compiled operations that 
work for this purpose. In other words, ``opsetX`` defines a set of operations 
for building a graph.

To build an ``:ref:`ov::Model <doxid-classov_1_1_model>``` instance from 
``opset8`` operations, include the following files:

.. tab:: C++

   .. ref-code-block:: cpp
   
      #include <openvino/core/model.hpp>
      #include <openvino/opsets/opset8.hpp>

.. tab:: Python

   .. ref-code-block:: cpp
   
      import openvino.runtime as ov

The following code demonstrates how to create a simple model:

.. tab:: C++

   .. ref-code-block:: cpp

      std::shared_ptr<ov::Model> create_simple_model() {
          // This example shows how to create ov::Model
          //
          // Parameter--->Multiply--->Add--->Result
          //    Constant---'          /
          //              Constant---'
      
          // Create opset8::Parameter operation with static shape
          auto data = std::make_shared<ov::opset8::Parameter>(:ref:`ov::element::f32 <doxid-group__ov__element__cpp__api_1gadc8a5dda3244028a5c0b024897215d43>`, :ref:`ov::Shape <doxid-classov_1_1_shape>`{3, 1, 2});
      
          auto mul_constant = ov::opset8::Constant::create(:ref:`ov::element::f32 <doxid-group__ov__element__cpp__api_1gadc8a5dda3244028a5c0b024897215d43>`, :ref:`ov::Shape <doxid-classov_1_1_shape>`{1}, {1.5});
          auto mul = std::make_shared<ov::opset8::Multiply>(data, mul_constant);
      
          auto add_constant = ov::opset8::Constant::create(:ref:`ov::element::f32 <doxid-group__ov__element__cpp__api_1gadc8a5dda3244028a5c0b024897215d43>`, :ref:`ov::Shape <doxid-classov_1_1_shape>`{1}, {0.5});
          auto :ref:`add <doxid-namespacengraph_1_1runtime_1_1reference_1a12956a756feab4106f4f12a6a372db41>` = std::make_shared<ov::opset8::Add>(mul, add_constant);
      
          // Create opset8::Result operation
          auto res = std::make_shared<ov::opset8::Result>(mul);
      
          // Create nGraph function
          return std::make_shared<ov::Model>(:ref:`ov::ResultVector <doxid-namespaceov_1adf9015702d0f2f7e69c705651f19b72a>`{res}, :ref:`ov::ParameterVector <doxid-namespaceov_1a2fd9bce881f1d37b496cf2e098274098>`{data});
      }

.. tab:: Python

   .. ref-code-block:: cpp

      def create_simple_model():
          # This example shows how to create ov::Function
          #
          # Parameter--->Multiply--->Add--->Result
          #    Constant---'          /
          #              Constant---'
          data = ov.opset8.parameter([3, 1, 2], ov.Type.f32)
          mul_constant = ov.opset8.constant([1.5], ov.Type.f32)
          mul = ov.opset8.multiply(data, mul_constant)
          add_constant = ov.opset8.constant([0.5], ov.Type.f32)
          add = ov.opset8.add(mul, add_constant)
          res = ov.opset8.result(add)
          return :ref:`ov.Model <doxid-classov_1_1_model>`([res], [data], "model")

The following code creates a model with several outputs:

.. tab:: C++

   .. ref-code-block:: cpp

      std::shared_ptr<ov::Model> create_advanced_model() {
          // Advanced example with multi output operation
          //
          // Parameter->Split---0-->Result
          //               | `--1-->Relu-->Result
          //               `----2-->Result

          auto data = std::make_shared<ov::opset8::Parameter>(:ref:`ov::element::f32 <doxid-group__ov__element__cpp__api_1gadc8a5dda3244028a5c0b024897215d43>`, :ref:`ov::Shape <doxid-classov_1_1_shape>`{1, 3, 64, 64});

          // Create Constant for axis value
          auto axis_const = ov::opset8::Constant::create(:ref:`ov::element::i64 <doxid-group__ov__element__cpp__api_1ga6c86a9a54d44fc205ad9cbf28ca556a6>`, :ref:`ov::Shape <doxid-classov_1_1_shape>`{} /\*scalar shape\*/, {1});

          // Create opset8::Split operation that splits input to three slices across 1st dimension
          auto :ref:`split <doxid-namespaceov_1_1util_1a128965e0b428278d28f9fa805b767137>` = std::make_shared<ov::opset8::Split>(data, axis_const, 3);
      
          // Create opset8::Relu operation that takes 1st Split output as input
          auto :ref:`relu <doxid-namespaceov_1_1op_1_1util_1_1detail_1a17863cb19970ed8fa653f7fd0442bcab>` = std::make_shared<ov::opset8::Relu>(:ref:`split <doxid-namespaceov_1_1util_1a128965e0b428278d28f9fa805b767137>`->output(1) /\*specify explicit output\*/);

          // Results operations will be created automatically based on provided OutputVector
          return std::make_shared<ov::Model>(:ref:`ov::OutputVector <doxid-namespaceov_1a0a3841455b82c164b1b04b61a9c7c560>`{:ref:`split <doxid-namespaceov_1_1util_1a128965e0b428278d28f9fa805b767137>`->output(0), :ref:`relu <doxid-namespaceov_1_1op_1_1util_1_1detail_1a17863cb19970ed8fa653f7fd0442bcab>`, :ref:`split <doxid-namespaceov_1_1util_1a128965e0b428278d28f9fa805b767137>`->output(2)},
                                             :ref:`ov::ParameterVector <doxid-namespaceov_1a2fd9bce881f1d37b496cf2e098274098>`{data});
      }

.. tab:: Python

   .. ref-code-block:: cpp

      def create_advanced_model():
          # Advanced example with multi output operation
          #
          # Parameter->Split---0-->Result
          #               | `--1-->Relu-->Result
          #               `----2-->Result
          data = ov.opset8.parameter(:ref:`ov.Shape <doxid-classov_1_1_shape>`([1, 3, 64, 64]), ov.Type.f32)
          # Create Constant for axis value
          axis_const = ov.opset8.constant(ov.Type.i64, :ref:`ov.Shape <doxid-classov_1_1_shape>`({}), [1])
      
          # Create opset8::Split operation that splits input to three slices across 1st dimension
          split = ov.opset8.split(data, axis_const, 3)
      
          # Create opset8::Relu operation that takes 1st Split output as input
          relu = ov.opset8.relu(split.output(1))
      
          # Results operations will be created automatically based on provided OutputVector
          return :ref:`ov.Model <doxid-classov_1_1_model>`([split.output(0), relu, split.output[2]], [data], "model")

Model Debugging Capabilities
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

OpenVINO™ provides several debug capabilities:

* To receive additional messages about applied model modifications, rebuild the 
  OpenVINO™ Runtime library with the ``-DENABLE_OPENVINO_DEBUG=ON`` option.

* Model can be visualized to image from the xDot format:

  .. tab:: C++

     .. ref-code-block:: cpp

        void visualize_example(const std::shared_ptr<ov::Model>& m) {
            // Need include:
            // \* openvino/pass/manager.hpp
            // \* openvino/pass/visualize_tree.hpp
            :ref:`ov::pass::Manager <doxid-classov_1_1pass_1_1_manager>` manager;

            // Serialize ov::Model to before.svg file before transformation
            manager.:ref:`register_pass <doxid-classov_1_1pass_1_1_manager_1a3c4834680de7b43557783e8500795da3>`<:ref:`ov::pass::VisualizeTree <doxid-classov_1_1pass_1_1_visualize_tree>`>("image.svg");

            manager.:ref:`run_passes <doxid-classov_1_1pass_1_1_manager_1a8b155191130f2c15e294cfd259d4ca0d>`(m);
        }

  .. tab:: Python

     .. ref-code-block:: cpp

        def visualize_example(m : ov.Model):
            # Need import:
            # \* import openvino.runtime.passes as passes
            pass_manager = passes.Manager()
            pass_manager.register_pass(pass_name="VisualTree", file_name='image.svg')
            pass_manager.run_passes(m)

  .. code-block:: cpp

     `ov::pass::VisualizeTree` can be parametrized via environment variables:

     OV_VISUALIZE_TREE_OUTPUT_SHAPES=1       - visualize shapes

     OV_VISUALIZE_TREE_OUTPUT_TYPES=1        - visualize types

     OV_VISUALIZE_TREE_MIN_MAX_DENORMAL=1    - pretty denormal values

     OV_VISUALIZE_TREE_RUNTIME_INFO=1        - print runtime information

     OV_VISUALIZE_TREE_IO=1                  - print I/O ports

     OV_VISUALIZE_TREE_MEMBERS_NAME=1        - print member names

* Also model can be serialized to IR:

  .. tab:: C++

     .. ref-code-block:: cpp

        void serialize_example(const std::shared_ptr<ov::Model>& :ref:`f <doxid-namespacengraph_1_1runtime_1_1reference_1a4582949bb0b6082a5159f90c43a71ca9>`) {
            // Need include:
            // \* openvino/pass/manager.hpp
            // \* openvino/pass/serialize.hpp
            :ref:`ov::pass::Manager <doxid-classov_1_1pass_1_1_manager>` manager;

            // Serialize ov::Model to IR
            manager.:ref:`register_pass <doxid-classov_1_1pass_1_1_manager_1a3c4834680de7b43557783e8500795da3>`<:ref:`ov::pass::Serialize <doxid-classov_1_1pass_1_1_serialize>`>("/path/to/file/model.xml", "/path/to/file/model.bin");

            manager.:ref:`run_passes <doxid-classov_1_1pass_1_1_manager_1a8b155191130f2c15e294cfd259d4ca0d>`(:ref:`f <doxid-namespacengraph_1_1runtime_1_1reference_1a4582949bb0b6082a5159f90c43a71ca9>`);
        }

  .. tab:: Python

     .. ref-code-block:: cpp

        def serialize_example(m : ov.Model):
            # Need import:
            # \* import openvino.runtime.passes as passes
            pass_manager = passes.Manager()
            pass_manager.register_pass(pass_name="Serialize", xml_path='model.xml', bin_path='model.bin')
            pass_manager.run_passes(m)

See Also
~~~~~~~~

:ref:`Available Operation Sets <doxid-openvino_docs_ops_opset>`

* :ref:`OpenVINO™ Runtime Extensibility Developer Guide <extensibility__api_introduction>`

* :ref:`Transformations Developer Guide <extensibility_transformations__overview>`.
