In this step, you write a Dockerfile that builds a Docker image. The
image contains all the dependencies the Python application requires,
including Python itself.

1. In your project directory, create a file named Dockerfile and paste
the following: ``touch Dockerfile``\ {{execute}}

.. raw:: html

   <pre class="file" data-filename="Dockerfile" data-target="replace">
   FROM python:3.4-alpine
   ADD . /code
   WORKDIR /code
   RUN pip install -r requirements.txt
   CMD ["python", "app.py"]
   </pre>

This tells Docker to: - Build an image starting with the Python 3.4
image. - Add the current directory ``.`` into the path /code in the
image. - Set the working directory to ``/code``. - Install the Python
dependencies. - Set the default command for the container to ``python``
``app.py``.
