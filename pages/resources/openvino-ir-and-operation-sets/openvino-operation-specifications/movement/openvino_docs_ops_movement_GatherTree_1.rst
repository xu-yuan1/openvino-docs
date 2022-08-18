.. index:: pair: page; GatherTree
.. _doxid-openvino_docs_ops_movement__gather_tree_1:


GatherTree
==========

:target:`doxid-openvino_docs_ops_movement__gather_tree_1_1md_openvino_docs_ops_movement_gathertree_1` **Versioned name** : *GatherTree-1*

**Category** : *Data movement*

**Short description** : Generates the complete beams from the ids per each step and the parent beam ids.

**Detailed description**

*GatherTree* operation reorders token IDs of a given input tensor ``step_id`` representing IDs per each step of beam search, based on input tensor ``parent_ids`` representing the parent beam IDs. For a given beam, past the time step containing the first decoded ``end_token`` all values are filled in with end_token.

The algorithm in pseudocode is as follows:

.. ref-code-block:: cpp

	final_ids[ :, :, :] = end_token
	for batch in :ref:`range <doxid-namespacengraph_1_1runtime_1_1reference_1ad38dec78131946cded583cc1154a406d>`(BATCH_SIZE):
	    for beam in :ref:`range <doxid-namespacengraph_1_1runtime_1_1reference_1ad38dec78131946cded583cc1154a406d>`(BEAM_WIDTH):
	        max_sequence_in_beam = :ref:`min <doxid-namespacengraph_1_1runtime_1_1reference_1abc42885cb896b121ab5ac214cbf60935>`(MAX_TIME, max_seq_len[batch])
	
	        parent = parent_ids[max_sequence_in_beam - 1, batch, beam]
	
	        final_ids[max_sequence_in_beam - 1, batch, beam] = step_ids[max_sequence_in_beam - 1, batch, beam]
	
	        for level in reversed(:ref:`range <doxid-namespacengraph_1_1runtime_1_1reference_1ad38dec78131946cded583cc1154a406d>`(max_sequence_in_beam - 1)):
	            final_ids[level, batch, beam] = step_ids[level, batch, parent]
	
	            parent = parent_ids[level, batch, parent]
	
	        # For a given beam, past the time step containing the first decoded end_token
	        # all values are filled in with end_token.
	        finished = False
	        for time in :ref:`range <doxid-namespacengraph_1_1runtime_1_1reference_1ad38dec78131946cded583cc1154a406d>`(max_sequence_in_beam):
	            if(finished):
	                final_ids[time, batch, beam] = end_token
	            elif(final_ids[time, batch, beam] == end_token):
	                finished = True

*GatherTree* operation is equivalent to `GatherTree operation in TensorFlow <https://www.tensorflow.org/addons/api_docs/python/tfa/seq2seq/gather_tree>`__.

**Attributes** : *GatherTree* operation has no attributes.

**Inputs**

* **1** : ``step_ids`` - Indices per each step. A tensor of type *T* and rank 3. Layout is ``[MAX_TIME, BATCH_SIZE, BEAM_WIDTH]``. **Required.**

* **2** : ``parent_ids`` - Parent beam indices. A tensor of type *T* and rank 3. Layout is ``[MAX_TIME, BATCH_SIZE, BEAM_WIDTH]``. **Required.**

* **3** : ``max_seq_len`` - Maximum lengths for each sequence in the batch. A tensor of type *T* and rank 1. Layout is ``[BATCH_SIZE]``. **Required.**

* **4** : ``end_token`` - Value of the end marker in a sequence. A scalar of type *T*. **Required.**

* **Note** : Inputs should have integer values only.

**Outputs**

* **1** : ``final_ids`` - The reordered token IDs based on ``parent_ids`` input. A tensor of type *T* and rank 3. Layout is ``[MAX_TIME, BATCH_SIZE, BEAM_WIDTH]``.

**Types**

* *T* : any supported numeric type.

**Example**

.. ref-code-block:: cpp

	<layer type="GatherTree" ...>
	    <input>
	        <port id="0">
	            <dim>100</dim>
	            <dim>1</dim>
	            <dim>10</dim>
	        </port>
	        <port id="1">
	            <dim>100</dim>
	            <dim>1</dim>
	            <dim>10</dim>
	        </port>
	        <port id="2">
	            <dim>1</dim>
	        </port>
	        <port id="3">
	        </port>
	    </input>
	    <output>
	        <port id="0">
	            <dim>100</dim>
	            <dim>1</dim>
	            <dim>10</dim>
	        </port>
	    </output>
	</layer>

