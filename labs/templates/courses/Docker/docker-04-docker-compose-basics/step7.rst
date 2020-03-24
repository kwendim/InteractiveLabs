1. If you want to run your services in the background, you can pass the
``-d`` flag (for “detached” mode) to ``docker-compose up`` and use
``docker-compose ps`` to see what is currently running:

``docker-compose up -d``\ {{execute}}

Output:

::

    Starting composetest_redis_1...
    Starting composetest_web_1...

2. Just to confirm you've been successful, run the following:

``docker-compose ps``\ {{execute}}

See it? Make sure you do, before moving on. The output should look like
this:

.. code:: console

    Name                   Command                  State         Ports
    -------------------------------------------------------------------
    composetest_redis_1   /usr/local/bin/run         Up
    composetest_web_1     /bin/sh -c python app.py   Up    5000->5000/tcp

3. The ``docker-compose run`` command allows you to run one-off commands
for your services. For example, to see what environment variables are
available to the web service:

``docker-compose run web env``\ {{execute}}

    **NOTE:** See ``docker-compose --help`` to see other available
    commands.

4. If you started Compose with docker-compose up -d, you’ll probably
want to stop your services once you’ve finished with them:

``docker-compose stop``\ {{execute}}

5. You can bring everything down, removing the containers entirely, with
the down command. Pass ``--volumes`` to also remove the data volume used
by the Redis container:

``docker-compose down --volumes``\ {{execute}}

At this point, you have seen the basics of how Compose works.
