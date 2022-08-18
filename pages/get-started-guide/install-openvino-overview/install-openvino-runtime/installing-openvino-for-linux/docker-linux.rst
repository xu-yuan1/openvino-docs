.. index:: pair: page; Install Intel® Distribution of OpenVINO™ toolkit for Linux from a Docker Image
.. _doxid-openvino_docs_install_guides_installing_openvino_docker_linux:


Install Intel® Distribution of OpenVINO™ toolkit for Linux from a Docker Image
=================================================================================

:target:`doxid-openvino_docs_install_guides_installing_openvino_docker_linux_1md_openvino_docs_install_guides_installing_openvino_docker_linux` This guide provides steps on creating a Docker image with Intel® Distribution of OpenVINO™ toolkit for Linux and using the image on different devices.

.. _system-requirments:

System Requirements
~~~~~~~~~~~~~~~~~~~

.. tab:: Target Operating Systems with Python Version

  +----------------------------------------------+--------------------------+
  | Operating System                             | Supported Python Version |
  +==============================================+==========================+
  | Ubuntu 18.04 long-term support (LTS), 64-bit |  3.6                     |
  +----------------------------------------------+--------------------------+
  | Ubuntu 20.04 long-term support (LTS), 64-bit |  3.8                     |
  +----------------------------------------------+--------------------------+
  | Red Hat Enterprise Linux 8, 64-bit           |  3.6                     |
  +----------------------------------------------+--------------------------+

.. tab:: Host Operating Systems

  * Linux
  * Windows Subsystem for Linux 2 (WSL2) on CPU or GPU
  * macOS on CPU only

  To launch a Linux image on WSL2 when trying to run inferences on a GPU, make sure that the following requirements are met:

  - Only Windows 10 with 21H2 update or above installed and Windows 11 are supported.
  - Intel GPU driver on Windows host with version 30.0.100.9684 or above need be installed. Please see `this article`_ for more details.
  - From 2022.1 release, the Docker images contain preinstalled recommended version of OpenCL Runtime with WSL2 support.

  .. _this article: https://www.intel.com/content/www/us/en/artificial-intelligence/harness-the-power-of-intel-igpu-on-your-machine.html#articleparagraph_983312434

Installation Flow
~~~~~~~~~~~~~~~~~

There are two ways to install OpenVINO with Docker. You can choose either of them according to your needs:

* Use a prebuilt image. Do the following steps:
  
  #. `Get a prebuilt image from provided sources <#get-prebuilt-image>`__.
  
  #. `Run the image on different devices <#run-image>`__. To run inferences on Intel® Vision Accelerator Design with Intel® Movidius™ VPUs, `configure the Docker image <#set-up-hddldaemon>`__ first before you run the image.
  
  #. `(Optional) Run samples in the Docker image <#run-samples>`__.

* If you want to customize your image, you can also build a Docker image manually by using the following steps:
  
  #. `Prepare a Dockerfile <#prepare-dockerfile>`__.
  
  #. `Configure the Docker image <#configure-image>`__.
  
  #. `Run the image on different devices <#run-image>`__.
  
  #. `(Optional) Run samples in the Docker image <#run-samples>`__.

.. _get-prebuilt-image:

Getting a Prebuilt Image from Provided Sources
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can find prebuilt images on:

* `Docker Hub <https://hub.docker.com/u/openvino>`__

* `Red Hat Quay.io <https://quay.io/organization/openvino>`__

* `Red Hat Ecosystem Catalog (runtime image) <https://catalog.redhat.com/software/containers/intel/openvino-runtime/606ff4d7ecb5241699188fb3>`__

* `Red Hat Ecosystem Catalog (development image) <https://catalog.redhat.com/software/containers/intel/openvino-dev/613a450dc9bc35f21dc4a1f7>`__

* `Azure Marketplace <https://azuremarketplace.microsoft.com/en-us/marketplace/apps/intel_corporation.openvino>`__

.. _prepare-dockerfile:

Preparing a Dockerfile
~~~~~~~~~~~~~~~~~~~~~~

You can use the `available Dockerfiles on GitHub <https://github.com/openvinotoolkit/docker_ci/tree/master/dockerfiles>`__ or generate a Dockerfile with your settings via `DockerHub CI Framework <https://github.com/openvinotoolkit/docker_ci>`__ which can generate a Dockerfile, build, test and deploy an image with the Intel® Distribution of OpenVINO™ toolkit. You can also try our `Tutorials <https://github.com/openvinotoolkit/docker_ci/tree/master/docs/tutorials>`__ which demonstrate the usage of Docker containers with OpenVINO.

.. _configure-image:

Configuring the Image for Different Devices
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you want to run inferences on a CPU or Intel® Neural Compute Stick 2, no extra configuration is needed. Go to `Running the image on different devices <#run-image>`__ for the next step.

Configuring Docker Image for GPU
--------------------------------

By default, the distributed Docker image for OpenVINO has the recommended version of Intel® Graphics Compute Runtime for oneAPI Level Zero and OpenCL Driver for the operating system installed inside. If you want to build an image with a custom version of OpenCL Runtime included, you need to modify the Dockerfile using the lines below (the 19.41.14441 version is used as an example) and build the image manually:

**Ubuntu 18.04/20.04** :

.. ref-code-block:: cpp

	WORKDIR /tmp/opencl
	RUN useradd -ms /bin/bash -G video,users openvino && \
	    chown openvino -R /home/openvino
	
	RUN apt-get update && \
	    apt-get install -y --no-install-recommends ocl-icd-libopencl1 && \
	    rm -rf /var/lib/apt/lists/\* && \
	    curl -L "https://github.com/intel/compute-runtime/releases/download/19.41.14441/intel-gmmlib_19.3.2_amd64.deb" --output "intel-gmmlib_19.3.2_amd64.deb" && \
	    curl -L "https://github.com/intel/compute-runtime/releases/download/19.41.14441/intel-igc-core_1.0.2597_amd64.deb" --output "intel-igc-core_1.0.2597_amd64.deb" && \
	    curl -L "https://github.com/intel/compute-runtime/releases/download/19.41.14441/intel-igc-opencl_1.0.2597_amd64.deb" --output "intel-igc-opencl_1.0.2597_amd64.deb" && \
	    curl -L "https://github.com/intel/compute-runtime/releases/download/19.41.14441/intel-opencl_19.41.14441_amd64.deb" --output "intel-opencl_19.41.14441_amd64.deb" && \
	    curl -L "https://github.com/intel/compute-runtime/releases/download/19.41.14441/intel-ocloc_19.41.14441_amd64.deb" --output "intel-ocloc_19.04.12237_amd64.deb" && \
	    dpkg -i /tmp/opencl/\*.deb && \
	    ldconfig && \
	    rm /tmp/opencl

**RHEL 8** :

.. ref-code-block:: cpp

	WORKDIR /tmp/opencl
	RUN useradd -ms /bin/bash -G video,users openvino && \
	    chown openvino -R /home/openvino
	RUN groupmod -g 44 video
	
	RUN yum update -y && yum install -y https://dl.fedoraproject.org/pub/epel/epel-release-latest-8.noarch.rpm && \
	    yum update -y && yum install -y ocl-icd ocl-icd-devel && \
	    yum clean all && rm -rf /var/cache/yum && \
	    curl -L https://sourceforge.net/projects/intel-compute-runtime/files/19.41.14441/centos-7/intel-gmmlib-19.3.2-1.el7.x86_64.rpm/download -o intel-gmmlib-19.3.2-1.el7.x86_64.rpm && \
	    curl -L https://sourceforge.net/projects/intel-compute-runtime/files/19.41.14441/centos-7/intel-gmmlib-devel-19.3.2-1.el7.x86_64.rpm/download -o intel-gmmlib-devel-19.3.2-1.el7.x86_64.rpm && \
	    curl -L https://sourceforge.net/projects/intel-compute-runtime/files/19.41.14441/centos-7/intel-igc-core-1.0.2597-1.el7.x86_64.rpm/download -o intel-igc-core-1.0.2597-1.el7.x86_64.rpm && \
	    curl -L https://sourceforge.net/projects/intel-compute-runtime/files/19.41.14441/centos-7/intel-igc-opencl-1.0.2597-1.el7.x86_64.rpm/download -o intel-igc-opencl-1.0.2597-1.el7.x86_64.rpm && \
	    curl -L https://sourceforge.net/projects/intel-compute-runtime/files/19.41.14441/centos-7/intel-igc-opencl-devel-1.0.2597-1.el7.x86_64.rpm/download -o  intel-igc-opencl-devel-1.0.2597-1.el7.x86_64.rpm && \
	    curl -L https://sourceforge.net/projects/intel-compute-runtime/files/19.41.14441/centos-7/intel-opencl-19.41.14441-1.el7.x86_64.rpm/download -o intel-opencl-19.41.14441-1.el7.x86_64.rpm \
	    rpm -ivh ${TEMP_DIR}/\*.rpm && \
	    ldconfig && \
	    rm -rf ${TEMP_DIR} && \
	    yum remove -y epel-release

.. _set-up-hddldaemon:

Configuring Docker Image for Intel® Vision Accelerator Design with Intel® Movidius™ VPUs
--------------------------------------------------------------------------------------------

.. note:: When building the Docker image, create a user in the Dockerfile that has the same UID (User Identifier) and GID (Group Identifier) as the user which that runs hddldaemon on the host, and then run the application in the Docker image with this user. This step is necessary to run the container as a non-root user.



To use the Docker container for inference on Intel® Vision Accelerator Design with Intel® Movidius™ VPUs, do the following steps:

#. Set up the environment on the host machine to be used for running Docker. It is required to execute ``hddldaemon``, which is responsible for communication between the HDDL plugin and the board. To learn how to set up the environment (the OpenVINO package or HDDL package must be pre-installed), see `Configuration guide for HDDL device <https://github.com/openvinotoolkit/docker_ci/blob/master/install_guide_vpu_hddl.md>`__ or :ref:`Configurations for Intel® Vision Accelerator Design with Intel® Movidius™ VPUs on Linux <doxid-openvino_docs_install_guides_installing_openvino_ivad_vpu>`.

#. Run ``hddldaemon`` on the host in a separate terminal session using the following command:
   
   .. ref-code-block:: cpp
   
   	$HDDL_INSTALL_DIR/hddldaemon

.. _run-image:

Running the Docker Image on Different Devices
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Running the Image on CPU
------------------------

Run the Docker image with the following command:

.. ref-code-block:: cpp

	docker run -it --rm <image_name>

Note the following things:

* Kernel reports the same information for all containers as for native application, for example, CPU, memory information.

* All instructions that are available to host process available for process in container, including, for example, AVX2, AVX512. No restrictions.

* Docker does not use virtualization or emulation. The process in Docker is just a regular Linux process, but it is isolated from external world on kernel level. Performance loss is minor.

Running the Image on GPU
------------------------

.. note:: Only Intel® integrated graphics are supported.



Note the following things:

* GPU is not available in the container by default. You must attach it to the container.

* Kernel driver must be installed on the host.

* In the container, non-root user must be in the ``video`` and ``render`` groups. To add a user to the render group, follow the `Configuration Guide for the Intel® Graphics Compute Runtime for OpenCL™ on Ubuntu 20.04 <https://github.com/openvinotoolkit/docker_ci/blob/master/configure_gpu_ubuntu20.md>`__.

To make GPU available in the container, attach the GPU to the container using ``--device /dev/dri`` option and run the container:

* Ubuntu 18 or RHEL 8:
  
  .. ref-code-block:: cpp
  
  	docker run -it --rm --device /dev/dri <image_name>
  
  
  
  .. note:: If your host system is Ubuntu 20, follow the `Configuration Guide for the Intel® Graphics Compute Runtime for OpenCL™ on Ubuntu\* 20.04 <https://github.com/openvinotoolkit/docker_ci/blob/master/configure_gpu_ubuntu20.md>`__.

* WSL2:
  
  .. ref-code-block:: cpp
  
  	docker run -it --rm --device /dev/dxg --volume /usr/lib/wsl:/usr/lib/wsl <image_name>
  
  
  
  .. note:: To launch a Linux image on WSL2, make sure that the additional requirements in `System Requirements <#system-requirements>`__ are met.

Running the Image on Intel® Neural Compute Stick 2
---------------------------------------------------

Run the Docker image with the following command:

.. ref-code-block:: cpp

	docker run -it --rm --device-cgroup-rule='c 189:\* rmw' -v /dev/bus/usb:/dev/bus/usb <image_name>

While the command above is not working, you can also run container in the privileged mode, enable the Docker network configuration as host, and mount all devices to the container. Run the following command:

.. ref-code-block:: cpp

	docker run -it --rm --privileged -v /dev:/dev --network=host <image_name>

.. note:: This option is not recommended, as conflicts with Kubernetes and other tools that use orchestration and private networks may occur. Please use it with caution and only for troubleshooting purposes.





Known Limitations
+++++++++++++++++

* Intel® Neural Compute Stick 2 device changes its VendorID and DeviceID during execution and each time looks for a host system as a brand new device. It means it cannot be mounted as usual.

* UDEV events are not forwarded to the container by default, and it does not know about the device reconnection. The prebuilt Docker images and provided Dockerfiles include ``libusb`` rebuilt without UDEV support.

* Only one NCS2 device connected to the host can be used when running inference in a container.

Running the Image on Intel® Vision Accelerator Design with Intel® Movidius™ VPUs
------------------------------------------------------------------------------------

.. note:: To run inferences on Intel® Vision Accelerator Design with Intel® Movidius™ VPUs, make sure that you have `configured the Docker image <#set-up-hddldaemon>`__ first.



Use the following command:

.. ref-code-block:: cpp

	docker run -it --rm --device=/dev/ion:/dev/ion -v /var/tmp:/var/tmp <image_name>

If your application runs inference of a network with a big size (>4MB) of input/output, the HDDL plugin will use shared memory. In this case, you must mount ``/dev/shm`` as volume:

.. ref-code-block:: cpp

	docker run -it --rm --device=/dev/ion:/dev/ion -v /var/tmp:/var/tmp -v /dev/shm:/dev/shm <image_name>

Note the following things:

* The device ``/dev/ion`` needs to be shared to be able to use ion buffers among the plugin, ``hddldaemon`` and the kernel.

* Since separate inference tasks share the same HDDL service communication interface (the service creates mutexes and a socket file in ``/var/tmp``), ``/var/tmp`` needs to be mounted and shared among them.

If the ion Driver is Not Enabled
++++++++++++++++++++++++++++++++

In some cases, the ion driver is not enabled (for example, due to a newer kernel version or iommu (Input-Output Memory Management Unit) incompatibility). ``lsmod | grep myd_ion`` returns empty output. To resolve this issue, use the following command:

.. ref-code-block:: cpp

	docker run -it --rm --ipc=host --net=host -v /var/tmp:/var/tmp <image_name>

If that still does not solve the issue, try starting ``hddldaemon`` with the root user on host. However, this approach is not recommended. Please use with caution.

.. _run-samples:

Running Samples in Docker Image
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To run the ``Hello Classification Sample`` on a specific inference device, run the following commands:

**CPU** :

.. ref-code-block:: cpp

	docker run -it --rm <image_name>
	/bin/bash -c "cd ~ && omz_downloader --name googlenet-v1 --precisions FP16 && omz_converter --name googlenet-v1 --precision FP16 && curl -O https://storage.openvinotoolkit.org/data/test_data/images/car_1.bmp && python3 /opt/intel/openvino/samples/python/hello_classification/hello_classification.py public/googlenet-v1/FP16/googlenet-v1.xml car_1.bmp CPU"

**GPU** :

.. ref-code-block:: cpp

	docker run -itu root:root  --rm --device /dev/dri:/dev/dri <image_name>
	/bin/bash -c "omz_downloader --name googlenet-v1 --precisions FP16 && omz_converter --name googlenet-v1 --precision FP16 && curl -O https://storage.openvinotoolkit.org/data/test_data/images/car_1.bmp && python3 samples/python/hello_classification/hello_classification.py public/googlenet-v1/FP16/googlenet-v1.xml car_1.bmp GPU"

**MYRIAD** :

.. ref-code-block:: cpp

	docker run -itu root:root --rm --device-cgroup-rule='c 189:\* rmw' -v /dev/bus/usb:/dev/bus/usb <image_name>
	/bin/bash -c "omz_downloader --name googlenet-v1 --precisions FP16 && omz_converter --name googlenet-v1 --precision FP16 && curl -O https://storage.openvinotoolkit.org/data/test_data/images/car_1.bmp && python3 samples/python/hello_classification/hello_classification.py public/googlenet-v1/FP16/googlenet-v1.xml car_1.bmp MYRIAD"

**HDDL** :

.. ref-code-block:: cpp

	docker run -itu root:root --rm --device=/dev/ion:/dev/ion -v /var/tmp:/var/tmp -v /dev/shm:/dev/shm <image_name>
	/bin/bash -c "omz_downloader --name googlenet-v1 --precisions FP16 && omz_converter --name googlenet-v1 --precision FP16 && curl -O https://storage.openvinotoolkit.org/data/test_data/images/car_1.bmp && umask 000 && python3 samples/python/hello_classification/hello_classification.py public/googlenet-v1/FP16/googlenet-v1.xml car_1.bmp HDDL"

Additional Resources
~~~~~~~~~~~~~~~~~~~~

* `DockerHub CI Framework <https://github.com/openvinotoolkit/docker_ci>`__ for Intel® Distribution of OpenVINO™ toolkit. The Framework can generate a Dockerfile, build, test, and deploy an image with the Intel® Distribution of OpenVINO™ toolkit. You can reuse available Dockerfiles, add your layer and customize the image of OpenVINO™ for your needs.

* Intel® Distribution of OpenVINO™ toolkit home page: `https://software.intel.com/en-us/openvino-toolkit <https://software.intel.com/en-us/openvino-toolkit>`__

* Intel® Neural Compute Stick 2 Get Started: `https://software.intel.com/en-us/neural-compute-stick/get-started <https://software.intel.com/en-us/neural-compute-stick/get-started>`__

