1. Create a file called ``docker-compose.yml`` in your project directory
and paste the following:

``touch docker-compose.yml``\ {{execute}}

.. raw:: html

   <pre class="file" data-filename="docker-compose.yml" data-target="replace">
   version: '3'
   services:
     web:
       build: .
       ports:
        - "5000:5000"
     redis:
       image: "redis:alpine"
   </pre>

This Compose file defines two services, ``web`` and ``redis``. The web
service: - Uses an image that’s built from the ``Dockerfile`` in the
current directory. - Forwards the exposed port 5000 on the container to
port 5000 on the host machine. - Mounts the project directory on the
host to ``/code`` inside the container, allowing you to modify the code
without having to rebuild the image. - The ``redis`` service uses a
public Redis image pulled from the Docker Hub registry.
