.. index:: pair: page; Quantizing Cascaded Face detection Model
.. _pot_api_example_face_detection:

.. meta::
   :description: The example demonstrates how to infer a cascaded model and
                 use Post-training Optimization Tool API to quantize MTCNN 
                 face detection model from Caffe.
   :keywords: Post-training Optimization Tool, Post-training Optimization Tool API,
              POT, POT API, quantizing models, post-training quantization, Model Downloader,
              Open Model Zoo, Model Converter, omz_converter, omz_downloader, 
              OpenVINO IR, OpenVINO Intermediate Representation, converting models,
              face detection, face detection model, MTCNN, Caffe, WIDER FACE,
              WIDER FACE dataset, cascaded model

Quantizing Face Detection Model
===============================

:target:`pot_api_example_face_detection_1md_openvino_tools_pot_openvino_tools_pot_api_samples_face_detection_readme` 

This example demonstrates the use of the :ref:`Post-training Optimization Tool API <pot_api_reference>` 
for the task of quantizing a face detection model. 
The `MTCNN <https://github.com/openvinotoolkit/open_model_zoo/blob/master/models/public/mtcnn/mtcnn.md>`__ 
model from Caffe is used for this purpose. A custom ``DataLoader`` is created 
to load `WIDER FACE <http://shuoyang1213.me/WIDERFACE/>`__ dataset for a face 
detection task and the implementation of Recall metric is used for the model 
evaluation. In addition, this example demonstrates how one can implement an engine 
to infer a cascaded (composite) model that is represented by multiple submodels in 
an OpenVino Intermediate Representation (IR) and has a complex staged inference 
pipeline. The code of the example is available on 
`GitHub <https://github.com/openvinotoolkit/openvino/tree/master/tools/pot/openvino/tools/pot/api/samples/face_detection>`__.

How to prepare the data
~~~~~~~~~~~~~~~~~~~~~~~

To run this example, you need to download the validation part of the Wider 
Face dataset `http://shuoyang1213.me/WIDERFACE/ <http://shuoyang1213.me/WIDERFACE/>`__. 
Images with faces divided into categories are placed in the ``WIDER_val/images`` 
folder. Annotations in .txt format containing the coordinates of the face 
bounding boxes of the validation part of the dataset can be downloaded separately 
and are located in the ``wider_face_split/wider_face_val_bbx_gt.txt`` file.

How to Run the example
~~~~~~~~~~~~~~~~~~~~~~

#. Launch `Model Downloader <https://github.com/openvinotoolkit/open_model_zoo/blob/master/tools/model_tools/README.md>`__ 
   tool to download ``mtcnn`` model from the Open Model Zoo repository.

   .. ref-code-block:: cpp

      omz_downloader --name mtcnn\*

#. Launch `Model Converter <https://github.com/openvinotoolkit/open_model_zoo/blob/master/tools/model_tools/README.md#model-converter-usage>`__ 
   tool to generate Intermediate Representation (IR) files for the model:

   .. ref-code-block:: cpp

      omz_converter --name mtcnn\* --mo <PATH_TO_MODEL_OPTIMIZER>/mo.py

#. Launch the example script from the example directory:

   .. ref-code-block:: cpp

      python3 ./face_detection_example.py -pm <PATH_TO_IR_XML_OF_PNET_MODEL> 
      -rm <PATH_TO_IR_XML_OF_RNET_MODEL> -om <PATH_TO_IR_XML_OF_ONET_MODEL> -d <WIDER_val/images> -a <wider_face_split/wider_face_val_bbx_gt.txt>

   Optional: you can specify .bin files of corresponding IRs directly using 
   the ``-pw/--pnet-weights``, ``-rw/--rnet-weights`` and ``-ow/--onet-weights`` options.
