1. Create a directory for the project:

``mkdir composetest``\ {{execute}}

``cd composetest``\ {{execute}}

2. Create a file called ``app.py`` in your project directory and paste
this in:

``touch app.py``\ {{execute}}

Then,

.. raw:: html

   <pre class="file" data-filename="app.py" data-target="replace">
   import time

   import redis
   from flask import Flask


   app = Flask(__name__)
   cache = redis.Redis(host='redis', port=6379)


   def get_hit_count():
       retries = 5
       while True:
           try:
               return cache.incr('hits')
           except redis.exceptions.ConnectionError as exc:
               if retries == 0:
                   raise exc
               retries -= 1
               time.sleep(0.5)


   @app.route('/')
   def hello():
       count = get_hit_count()
       return 'Hello World! I have been seen {} times.\n'.format(count)

   if __name__ == "__main__":
       app.run(host="0.0.0.0", debug=True)
   </pre>

3. Create another file called ``requirements.txt`` in your project
directory and paste the following lines in it, like this:

``touch requirements.txt``\ {{execute}}

.. raw:: html

   <pre class="file" data-filename="requirements.txt" data-target="replace">
   flask
   redis
   </pre>

    **NOTE:** These define the application’s dependencies.
