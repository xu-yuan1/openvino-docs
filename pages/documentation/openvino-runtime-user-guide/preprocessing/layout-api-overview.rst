.. index:: pair: page; Layout API Overview
.. _deploy_infer__layout_api_overview:

.. meta::
   :description: The layout enables the application to interpret each particular 
                 dimension of input/ output tensor properly and the input size 
                 can be resized to fit the model.
   :keywords: inference, model inference, input tensor, output tensor, input size, 
              layout syntax, model modification, model conversion, model input, 
              model output, specify dimension, short syntax, advanced syntax, 
              partially defined syntax, dynamic layout, ov::Layout, batch dimension, 
              channels dimension, batch size, width dimension, height dimension, 
              depth dimension, NCHW, serialization, batch_idx, channels_idx, depth_idx 
              height_idx, width_idx

Layout API Overview
===================

:target:`deploy_infer__layout_api_overview_1md_openvino_docs_ov_runtime_ug_layout_overview`

The concept of layout helps you (and your application) to understand what each particular dimension of input/output tensor means. For example, if your input has the ``{1, 3, 720, 1280}`` shape and the ``NCHW`` layout, it is clear that ``N(batch) = 1``, ``C(channels) = 3``, ``H(height) = 720``, and ``W(width) = 1280``. Without the layout information, the ``{1, 3, 720, 1280}`` tuple does not give any idea to your application on what these numbers mean and how to resize the input image to fit the expectations of the model.

With the ``NCHW`` layout, it is easier to understand what the ``{8, 3, 224, 224}`` model shape means. Without the layout, it is just a 4-dimensional tensor.

Below is a list of cases where input/output layout is important:

* Performing model modification:
  
  * Applying the :ref:`preprocessing <deploy_infer__preprocessing_overview>` steps, such as subtracting means, dividing by scales, resizing an image, and converting ``RGB`` <-> ``BGR``.
  
  * Setting/getting a batch for a model.

* Doing the same operations as used during the model conversion phase. For more information, refer to the :ref:`Model Optimizer Embedding Preprocessing Computation <doxid-openvino_docs__m_o__d_g__additional__optimization__use__cases>` guide.

* Improving the readability of a model input and output.

Syntax of Layout
~~~~~~~~~~~~~~~~

Short Syntax
------------

The easiest way is to fully specify each dimension with one alphabet letter.

.. raw:: html

   <div class='sphinxtabset'>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="C++">





.. ref-code-block:: cpp

	layout = :ref:`ov::Layout <doxid-namespace_inference_engine_1a246d143abc5ca07da8d2cadeeb88fdb8>`("NHWC");

.. raw:: html

   </div>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="Python">





.. ref-code-block:: cpp

	from openvino.runtime import Layout
	layout = :ref:`Layout <doxid-namespace_inference_engine_1a246d143abc5ca07da8d2cadeeb88fdb8>`('NCHW')

.. raw:: html

   </div>







.. raw:: html

   </div>



This assigns ``N`` to the first dimension, ``C`` to the second, ``H`` to the third, and ``W`` to the fourth.

Advanced Syntax
---------------

The advanced syntax allows assigning a word to a dimension. To do this, wrap a layout with square brackets ``[]`` and specify each name separated by a comma ``,``.

.. raw:: html

   <div class='sphinxtabset'>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="C++">





.. ref-code-block:: cpp

	// Each dimension has name separated by comma, layout is wrapped with square brackets
	layout = :ref:`ov::Layout <doxid-namespace_inference_engine_1a246d143abc5ca07da8d2cadeeb88fdb8>`("[time,temperature,humidity]");

.. raw:: html

   </div>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="Python">





.. ref-code-block:: cpp

	# Each dimension has name separated by comma
	# Layout is wrapped with square brackets
	layout = :ref:`Layout <doxid-namespace_inference_engine_1a246d143abc5ca07da8d2cadeeb88fdb8>`('[time,temperature,humidity]')

.. raw:: html

   </div>







.. raw:: html

   </div>

Partially Defined Layout
------------------------

If a certain dimension is not important, its name can be set to ``?``.

.. raw:: html

   <div class='sphinxtabset'>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="C++">





.. ref-code-block:: cpp

	// First dimension is batch, 4th is 'channels'. Others are not important for us
	layout = :ref:`ov::Layout <doxid-namespace_inference_engine_1a246d143abc5ca07da8d2cadeeb88fdb8>`("N??C");
	// Or the same using advanced syntax
	layout = :ref:`ov::Layout <doxid-namespace_inference_engine_1a246d143abc5ca07da8d2cadeeb88fdb8>`("[n,?,?,c]");

.. raw:: html

   </div>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="Python">





.. ref-code-block:: cpp

	# First dimension is batch, 4th is 'channels'.
	# Others are not important for us
	layout = :ref:`Layout <doxid-namespace_inference_engine_1a246d143abc5ca07da8d2cadeeb88fdb8>`('N??C')
	
	# Or the same using advanced syntax
	layout = :ref:`Layout <doxid-namespace_inference_engine_1a246d143abc5ca07da8d2cadeeb88fdb8>`('[n,?,?,c]')

.. raw:: html

   </div>







.. raw:: html

   </div>

Dynamic Layout
--------------

If several dimensions are not important, an ellipsis ``...`` can be used to specify those dimensions.

.. raw:: html

   <div class='sphinxtabset'>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="C++">





.. ref-code-block:: cpp

	// First dimension is 'batch' others are whatever
	layout = :ref:`ov::Layout <doxid-namespace_inference_engine_1a246d143abc5ca07da8d2cadeeb88fdb8>`("N...");
	
	// Second dimension is 'channels' others are whatever
	layout = :ref:`ov::Layout <doxid-namespace_inference_engine_1a246d143abc5ca07da8d2cadeeb88fdb8>`("?C...");
	
	// Last dimension is 'channels' others are whatever
	layout = :ref:`ov::Layout <doxid-namespace_inference_engine_1a246d143abc5ca07da8d2cadeeb88fdb8>`("...C");

.. raw:: html

   </div>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="Python">





.. ref-code-block:: cpp

	# First dimension is 'batch' others are whatever
	layout = :ref:`Layout <doxid-namespace_inference_engine_1a246d143abc5ca07da8d2cadeeb88fdb8>`('N...')
	
	# Second dimension is 'channels' others are whatever
	layout = :ref:`Layout <doxid-namespace_inference_engine_1a246d143abc5ca07da8d2cadeeb88fdb8>`('?C...')
	
	# Last dimension is 'channels' others are whatever
	layout = :ref:`Layout <doxid-namespace_inference_engine_1a246d143abc5ca07da8d2cadeeb88fdb8>`('...C')

.. raw:: html

   </div>







.. raw:: html

   </div>





Predefined Names
----------------

A layout has some pre-defined dimension names, widely used in computer vision:

* ``N`` / ``Batch`` - batch size

* ``C`` / ``Channels`` - channels

* ``D`` / ``Depth`` - depth

* ``H`` / ``Height`` - height

* ``W`` / ``Width`` - width

These names are used in :ref:`PreProcessing API <deploy_infer__preprocessing_overview>`. There is a set of helper functions to get appropriate dimension index from a layout.

.. raw:: html

   <div class='sphinxtabset'>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="C++">





.. ref-code-block:: cpp

	// returns 0 for batch
	:ref:`ov::layout::batch_idx <doxid-group__ov__layout__cpp__api_1gae57e9fcaa7d8eaa7ddbcdfece346bccb>`("NCDHW");
	
	// returns 1 for channels
	:ref:`ov::layout::channels_idx <doxid-group__ov__layout__cpp__api_1ga4c4a2d4a226d5b264a0f74c6c7839f4f>`("NCDHW");
	
	// returns 2 for depth
	:ref:`ov::layout::depth_idx <doxid-group__ov__layout__cpp__api_1ga69af957b8f6a69956f38dfa1afc7039a>`("NCDHW");
	
	// returns -2 for height
	:ref:`ov::layout::height_idx <doxid-group__ov__layout__cpp__api_1ga83da0183fe7f811912436ddb4aa4bb28>`("...HW");
	
	// returns -1 for width
	:ref:`ov::layout::width_idx <doxid-group__ov__layout__cpp__api_1ga8730a2b5c3fd24f752c550ee3d07b870>`("...HW");

.. raw:: html

   </div>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="Python">





.. ref-code-block:: cpp

	from openvino.runtime import layout_helpers
	# returns 0 for batch
	layout_helpers.batch_idx(:ref:`Layout <doxid-namespace_inference_engine_1a246d143abc5ca07da8d2cadeeb88fdb8>`('NCDHW'))
	
	# returns 1 for channels
	layout_helpers.channels_idx(:ref:`Layout <doxid-namespace_inference_engine_1a246d143abc5ca07da8d2cadeeb88fdb8>`('NCDHW'))
	
	# returns 2 for depth
	layout_helpers.depth_idx(:ref:`Layout <doxid-namespace_inference_engine_1a246d143abc5ca07da8d2cadeeb88fdb8>`('NCDHW'))
	
	# returns -2 for height
	layout_helpers.height_idx(:ref:`Layout <doxid-namespace_inference_engine_1a246d143abc5ca07da8d2cadeeb88fdb8>`('...HW'))
	
	# returns -1 for width
	layout_helpers.width_idx(:ref:`Layout <doxid-namespace_inference_engine_1a246d143abc5ca07da8d2cadeeb88fdb8>`('...HW'))

.. raw:: html

   </div>







.. raw:: html

   </div>





Equality
--------

Layout names are case-insensitive, which means that ``Layout("NCHW")`` = ``Layout("nChW") =`` Layout("[N,c,H,w]")`.

Dump Layout
-----------

A layout can be converted to a string in the advanced syntax format. It can be useful for debugging and serialization purposes.

.. raw:: html

   <div class='sphinxtabset'>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="C++">





.. ref-code-block:: cpp

	layout = :ref:`ov::Layout <doxid-namespace_inference_engine_1a246d143abc5ca07da8d2cadeeb88fdb8>`("NCHW");
	std::cout << layout.to_string(); // prints [N,C,H,W]

.. raw:: html

   </div>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="Python">





.. ref-code-block:: cpp

	layout = :ref:`Layout <doxid-namespace_inference_engine_1a246d143abc5ca07da8d2cadeeb88fdb8>`('NCHW')
	print(layout)    # prints [N,C,H,W]

.. raw:: html

   </div>







.. raw:: html

   </div>





See also
~~~~~~~~

* API Reference: ``:ref:`ov::Layout <doxid-classov_1_1_layout>``` C++ class

