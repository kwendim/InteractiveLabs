Installing Docker
-----------------

In this tutorial, you will learn how to install docker on a Ubuntu
machine and run your first containers.

First we need to add Docker’s official GPG key:

``curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add``\ {{execute}}

Use the following command to set up the stable repository:
``sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"``\ {{execute}}

And update the package index files from the source:
``sudo apt-get update``\ {{execute}}

Now we can install docker from the official repository by typping:

``sudo apt-get install -y docker-ce docker-ce-cli containerd.io``\ {{execute}}
