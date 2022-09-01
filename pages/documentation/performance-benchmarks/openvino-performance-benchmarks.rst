.. index:: pair: page; Intel® Distribution of OpenVINO™ toolkit Benchmark Results
.. _openvino_benchmarks:

.. meta::
   :description: The benchmark application loads OpenVINO™ Runtime and does 
                 inference on hardware, then it measures the inference time 
                 and reports on the inferences per second.
   :keyword: benchmark application, performance benchmarks, benchmark_app, 
             Intel CPU, Intel GPU, Intel VPU, OpenVINO™ Runtime, inference, 
             deep learning inference, neural networks, benchmark results, 
             benchmark performance results, benchmark setup, throughput, 
             efficiency, latency, synchronous execution, inference request


Intel® Distribution of OpenVINO™ toolkit Benchmark Results
=============================================================

:target:`openvino_benchmarks_1md_openvino_docs_benchmarks_performance_benchmarks_openvino`


.. toctree::
   :maxdepth: 1
   :hidden:

   ./openvino-performance-benchmarks/performance-benchmarks-faq
   ./openvino-performance-benchmarks/model-accuracy-for-int8-fp32

Features and benefits of Intel® technologies depend on system configuration and 
may require enabled hardware, software or service activation. More information 
on this subject may be obtained from the original equipment manufacturer (OEM), 
official `Intel® web page <https://www.intel.com>`__ or retailer.

Benchmark Setup Information
~~~~~~~~~~~~~~~~~~~~~~~~~~~

This benchmark setup includes a single machine on which both the benchmark 
application and the OpenVINO™ installation reside. The presented performance 
benchmark numbers are based on release 2022.1 of Intel® Distribution of 
OpenVINO™ toolkit.

The benchmark application loads the OpenVINO™ Runtime and executes inferences 
on the specified hardware (CPU, GPU or VPU). It measures the time spent on 
actual inference (excluding any pre or post processing) and then reports on 
the inferences per second (or Frames Per Second - FPS). For additional 
information on the benchmark application, refer to the entry 5 in the 
:ref:`FAQ section <performance_benchmarks_faq>`.

Measuring inference performance involves many variables and is extremely use 
case and application dependent. Below are four parameters used for measurements, 
which are key elements to consider for a successful deep learning inference application:

* **Throughput** - Measures the number of inferences delivered within a latency 
  threshold (for example, number of FPS). When deploying a system with deep 
  learning inference, select the throughput that delivers the best trade-off 
  between latency and power for the price and performance that meets your requirements.

* **Value** - While throughput is important, what is more critical in edge AI 
  deployments is the performance efficiency or performance-per-cost. Application 
  performance in throughput per dollar of system cost is the best measure of value.

* **Efficiency** - System power is a key consideration from the edge to the data 
  center. When selecting deep learning solutions, power efficiency (throughput/watt) 
  is a critical factor to consider. Intel designs provide excellent power 
  efficiency for running deep learning workloads.

* **Latency** - This parameter measures the synchronous execution of inference 
  requests and is reported in milliseconds. Each inference request (i.e., 
  pre-process, infer, post-process) is allowed to complete before the next one is 
  started. This performance metric is relevant in usage scenarios where a single 
  image input needs to be acted upon as soon as possible. An example of that 
  kind of a scenario would be real-time or near real-time applications, i.e., 
  the response of an industrial robot to its environment or obstacle 
  avoidance for autonomous vehicles.

Benchmark Performance Results
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Benchmark performance results below are based on testing as of March 17, 2022. 
They may not reflect all publicly available updates at the time of testing.

Performance varies by use, configuration and other factors, which are elaborated 
further in `here <https://www.intel.com/PerformanceIndex>`__. Used Intel 
optimizations (for Intel® compilers or other products) may not optimize to the 
same degree for non-Intel products.

bert-base-cased [124]
---------------------

.. raw:: html

    <div class="chart-block" data-loadcsv="../../../_static/benchmarks_csv/bert-base-cased124.csv"></div>

bert-large-uncased-whole-word-masking-squad-int8-0001 [384]
-----------------------------------------------------------

.. raw:: html

    <div class="chart-block" data-loadcsv="../../../_static/benchmarks_csv/bert-large-uncased-whole-word-masking-squad-int8-0001-384.csv"></div>

deeplabv3-TF [513x513]
----------------------

.. raw:: html

    <div class="chart-block" data-loadcsv="../../../_static/benchmarks_csv/deeplabv3-TF-513x513.csv"></div>

densenet-121-TF [224x224]
-------------------------

.. raw:: html

    <div class="chart-block" data-loadcsv="../../../_static/benchmarks_csv/densenet-121-TF-224x224.csv"></div>

efficientdet-d0 [512x512]
-------------------------

.. raw:: html

    <div class="chart-block" data-loadcsv="../../../_static/benchmarks_csv/efficientdet-d0-512x512.csv"></div>

faster-rcnn-resnet50-coco-TF [600x1024]
---------------------------------------

.. raw:: html

    <div class="chart-block" data-loadcsv="../../../_static/benchmarks_csv/faster_rcnn_resnet50_coco-TF-600x1024.csv"></div>

inception-v4-TF [299x299]
-------------------------

.. raw:: html

    <div class="chart-block" data-loadcsv="../../../_static/benchmarks_csv/inception-v4-TF-299x299.csv"></div>

mobilenet-ssd-CF [300x300]
--------------------------

.. raw:: html

    <div class="chart-block" data-loadcsv="../../../_static/benchmarks_csv/mobilenet-ssd-CF-300x300.csv"></div>

mobilenet-v2-pytorch [224x224]
------------------------------

.. raw:: html

    <div class="chart-block" data-loadcsv="../../../_static/benchmarks_csv/mobilenet-v2-pytorch-224x224.csv"></div>

resnet-18-pytorch [224x224]
---------------------------

.. raw:: html

    <div class="chart-block" data-loadcsv="../../../_static/benchmarks_csv/resnet-18-pytorch-224x224.csv"></div>

resnet_50_TF [224x224]
----------------------

.. raw:: html

    <div class="chart-block" data-loadcsv="../../../_static/benchmarks_csv/resnet-50-TF-224x224.csv"></div>

ssd-resnet34-1200-onnx [1200x1200]
----------------------------------

.. raw:: html

    <div class="chart-block" data-loadcsv="../../../_static/benchmarks_csv/ssd-resnet34-1200-onnx-1200x1200.csv"></div>

unet-camvid-onnx-0001 [368x480]
-------------------------------

.. raw:: html

    <div class="chart-block" data-loadcsv="../../../_static/benchmarks_csv/unet-camvid-onnx-0001-368x480.csv"></div>

yolo-v3-tiny-tf [416x416]
-------------------------

.. raw:: html

    <div class="chart-block" data-loadcsv="../../../_static/benchmarks_csv/yolo-v3-tiny-tf-416x416.csv"></div>

yolo_v4-tf [608x608]
--------------------

.. raw:: html

    <div class="chart-block" data-loadcsv="../../../_static/benchmarks_csv/yolo_v4-tf-608x608.csv"></div>


Platform Configurations
~~~~~~~~~~~~~~~~~~~~~~~
Download a full list of HW platforms and their configurations used for testing:
:download:`HW platforms used for testing (PDF)<./_assets/Platform_list.pdf>`

For more specific information, refer to 
`Configuration Details <https://docs.openvino.ai/resources/benchmark_files/system_configurations_2022.1.html>`__ .


© Intel Corporation. Intel, the Intel logo, and other Intel marks are 
trademarks of Intel Corporation or its subsidiaries. Other names and brands 
may be claimed as the property of others.
