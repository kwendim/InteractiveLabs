A Container is a runnable instance of an image. The image contains
everything required to launch the process without requiring any
configuration file or dependencies in the host.

You can find existing images at Docker Hub, https://hub.docker.com/ or
by typping the command ``docker search <image_name>``

In this example we will run a container that contains **whalesay** an
adaption of the Linux cowsay game.

Let's look for whalesay on the Docker Hub repository:
``docker search whalesay``\ {{execute}}

You can pull (download) the image locally:
``docker pull docker/whalesay``\ {{execute}}

The image should now be listed: ``docker images``\ {{execute}}

You can run it by typping:
``docker run docker/whalesay cowsay 'Hello world!'``\ {{execute}}

Note: if you forget to pull, docker run will also do that for you.

To check if the container is running use: ``docker ps``\ {{execute}}

Nothing is listed because its execution has finished, let's take a look
for containers that have been closed: ``docker ps -a``\ {{execute}}
