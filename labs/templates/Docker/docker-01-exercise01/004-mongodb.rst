Connect to the database and change its name to

``mongo localhost/mydb``\ {{execute}}

Now we will create a collection call ``cities`` and populate it with
some documents:

``db.createCollection('cities') db.cities.insert({ name: 'New York', country: 'USA' }) db.cities.insert({ name: 'Paris', country:'France'}``\ {{execute}}

You should be able to find them by typping:

``db.cities.find()``\ {{execute}}

Migrating data to a new container
---------------------------------

We want to migrate the data from our ``mongodb`` to a different one in
the port ``37017``.

First, we have to copy the data from the previous container (it is
locate in: ``~/data``)

``sudo cp -r ~/data ~/data_clone``\ {{execute}}

Now we just need to start another container (using the same image),
mapping the port 27017 from the container to the port 37017 in the host
and mount the data copied previously to ``/data/db``.

``docker run -d -p 37017:27017 -v ~/data_clone:/data/db mongo``\ {{execute}}
