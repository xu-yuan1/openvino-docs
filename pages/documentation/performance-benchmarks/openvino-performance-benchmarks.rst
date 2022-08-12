.. index:: pair: page; Intel® Distribution of OpenVINO™ toolkit Benchmark Results
.. _doxid-openvino_docs_performance_benchmarks_openvino:


Intel® Distribution of OpenVINO™ toolkit Benchmark Results
=============================================================

:target:`doxid-openvino_docs_performance_benchmarks_openvino_1md_openvino_docs_benchmarks_performance_benchmarks_openvino`


.. toctree::
   :maxdepth: 1
   :hidden:

   ./openvino-performance-benchmarks/performance-benchmarks-faq
   Download Performance Data Spreadsheet in MS Excel Format <https://docs.openvino.ai/downloads/benchmark_files/OV-2022.1-Download-Excel.xlsx>
   ./openvino-performance-benchmarks/model-accuracy-for-int8-fp32

Features and benefits of Intel® technologies depend on system configuration and may require enabled hardware, software or service activation. More information on this subject may be obtained from the original equipment manufacturer (OEM), official `Intel® web page <https://www.intel.com>`__ or retailer.

Platform Configurations
~~~~~~~~~~~~~~~~~~~~~~~

:download:`A full list of HW platforms used for testing (along with their configuration)<../../../docs/benchmarks/files/Platform_list.pdf>`

For more specific information, refer to the `Configuration Details <https://docs.openvino.ai/resources/benchmark_files/system_configurations_2022.1.html>`__ document.

Benchmark Setup Information
~~~~~~~~~~~~~~~~~~~~~~~~~~~

This benchmark setup includes a single machine on which both the benchmark application and the OpenVINO™ installation reside. The presented performance benchmark numbers are based on realease 2022.1 of Intel® Distribution of OpenVINO™ toolkit.

The benchmark application loads the OpenVINO™ Runtime and executes inferences on the specified hardware (CPU, GPU or VPU). It measures the time spent on actual inferencing (excluding any pre or post processing) and then reports on the inferences per second (or Frames Per Second - FPS). For additional information on the benchmark application, refer to the entry 5 in the :ref:`FAQ section <doxid-openvino_docs_performance_benchmarks_faq>`.

Measuring inference performance involves many variables and is extremely use case and application dependent. Below are four parameters used for measurements, which are key elements to consider for a successful deep learning inference application:

* **Throughput** - Measures the number of inferences delivered within a latency threshold (for example, number of FPS). When deploying a system with deep learning inference, select the throughput that delivers the best trade-off between latency and power for the price and performance that meets your requirements.

* **Value** - While throughput is important, what is more critical in edge AI deployments is the performance efficiency or performance-per-cost. Application performance in throughput per dollar of system cost is the best measure of value.

* **Efficiency** - System power is a key consideration from the edge to the data center. When selecting deep learning solutions, power efficiency (throughput/watt) is a critical factor to consider. Intel designs provide excellent power efficiency for running deep learning workloads.

* **Latency** - This parameter measures the synchronous execution of inference requests and is reported in milliseconds. Each inference request (i.e., preprocess, infer, postprocess) is allowed to complete before the next one is started. This performance metric is relevant in usage scenarios where a single image input needs to be acted upon as soon as possible. An example of that kind of a scenario would be real-time or near real-time applications, i.e., the response of an industrial robot to its environment or obstacle avoidance for autonomous vehicles.

Benchmark Performance Results
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Benchmark performance results below are based on testing as of March 17, 2022. They may not reflect all publicly available updates at the time of testing.

Performance varies by use, configuration and other factors, which are elaborated further in `here <https://www.intel.com/PerformanceIndex>`__. Used Intel optimizations (for Intel® compilers or other products) may not optimize to the same degree for non-Intel products.

bert-base-cased [124]
---------------------

.. raw:: html

    <div class="chart-block" data-loadcsv="./_assets/bert-base-cased124.csv"></div>

bert-large-uncased-whole-word-masking-squad-int8-0001 [384]
-----------------------------------------------------------

.. raw:: html

    <div class="chart-block" data-loadcsv="./_assets/bert-large-uncased-whole-word-masking-squad-int8-0001-384.csv"></div>

deeplabv3-TF [513x513]
----------------------

.. raw:: html

    <div class="chart-block" data-loadcsv="./_assets/deeplabv3-TF-513x513.csv"></div>

densenet-121-TF [224x224]
-------------------------

.. raw:: html

    <div class="chart-block" data-loadcsv="./_assets/densenet-121-TF-224x224.csv"></div>

efficientdet-d0 [512x512]
-------------------------

.. raw:: html

    <div class="chart-block" data-loadcsv="./_assets/efficientdet-d0-512x512.csv"></div>

faster-rcnn-resnet50-coco-TF [600x1024]
---------------------------------------

.. raw:: html

    <div class="chart-block" data-loadcsv="./_assets/faster_rcnn_resnet50_coco-TF-600x1024.csv"></div>

inception-v4-TF [299x299]
-------------------------

.. raw:: html

    <div class="chart-block" data-loadcsv="./_assets/inception-v4-TF-299x299.csv"></div>

mobilenet-ssd-CF [300x300]
--------------------------

.. raw:: html

    <div class="chart-block" data-loadcsv="./_assets/mobilenet-ssd-CF-300x300.csv"></div>

mobilenet-v2-pytorch [224x224]
------------------------------

.. raw:: html

    <div class="chart-block" data-loadcsv="./_assets/mobilenet-v2-pytorch-224x224.csv"></div>

resnet-18-pytorch [224x224]
---------------------------

.. raw:: html

    <div class="chart-block" data-loadcsv="./_assets/resnet-18-pytorch-224x224.csv"></div>

resnet_50_TF [224x224]
----------------------

.. raw:: html

    <div class="chart-block" data-loadcsv="./_assets/resnet-50-TF-224x224.csv"></div>

ssd-resnet34-1200-onnx [1200x1200]
----------------------------------

.. raw:: html

    <div class="chart-block" data-loadcsv="./_assets/ssd-resnet34-1200-onnx-1200x1200.csv"></div>

unet-camvid-onnx-0001 [368x480]
-------------------------------

.. raw:: html

    <div class="chart-block" data-loadcsv="./_assets/unet-camvid-onnx-0001-368x480.csv"></div>

yolo-v3-tiny-tf [416x416]
-------------------------

.. raw:: html

    <div class="chart-block" data-loadcsv="./_assets/yolo-v3-tiny-tf-416x416.csv"></div>

yolo_v4-tf [608x608]
--------------------

.. raw:: html

    <div class="chart-block" data-loadcsv="./_assets/yolo_v4-tf-608x608.csv"></div>

© Intel Corporation. Intel, the Intel logo, and other Intel marks are trademarks of Intel Corporation or its subsidiaries. Other names and brands may be claimed as the property of others.

