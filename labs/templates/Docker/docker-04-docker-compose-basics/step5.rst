1. From your project directory, start up your application.

``docker-compose up``\ {{execute}}

Output:

.. code:: console

    Pulling image redis...
    Building web...
    Starting composetest_redis_1...
    Starting composetest_web_1...
    redis_1 | [8] 02 Jan 18:43:35.576 # Server started, Redis version 2.8.3
    web_1   |  * Running on http://0.0.0.0:5000/
    web_1   |  * Restarting with stat

Compose pulls a Redis image, builds an image for your code, and start
the services you defined.

2. Now that our containers are up and running, we can now click the
"Browser" tab alonside your terminal tab. This tab is set to
``localhost:5000``, which is just perfect for us.

    **NOTE:** If you’re using Docker on Linux natively, then the web app
    should now be listening on port 5000 on your Docker daemon host. If
    ``http://0.0.0.0:5000`` doesn’t resolve, you can also try
    ``http://localhost:5000``. If you’re using Docker Machine on a Mac,
    use ``docker-machine ip MACHINE_VM`` to get the IP address of your
    Docker host. Then, open ``http://MACHINE_VM_IP:5000`` in a browser.

You should see a message in your browser saying:

.. code:: console

    Hello World! I have been seen 1 times.

3. Refresh the page, and watch the number increment.
