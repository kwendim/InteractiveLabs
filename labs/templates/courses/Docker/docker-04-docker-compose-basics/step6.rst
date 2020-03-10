Because the application code is mounted into the container using a
volume, you can make changes to its code and see the changes instantly,
without having to rebuild the image.

1. Change the greeting in ``app.py`` and save it. For example:

::

    return 'Hello from Docker! I have been seen {} times.\n'.format(count)

2. Refresh the app in your browser. The greeting should be updated, and
the counter should still be incrementing.

3. Once you are done, before moving to the next step, be sure to bring
Compose down, by issuing the following:
``docker-compose down``\ {{execute}}
