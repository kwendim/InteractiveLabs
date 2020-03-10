Basic configuration To configure the container, you can pass additional
or modified options to the docker run command.

The following sections provide basic guidelines for configuring your
registry. For more details, see the registry configuration reference.

Start the registry automatically If you want to use the registry as part
of your permanent infrastructure, you should set it to restart
automatically when Docker restarts or if it exits. This example uses the
--restart always flag to set a restart policy for the registry.

| $ docker run -d
| -p 5000:5000
| --restart=always
| --name registry
| registry:2 Customize the published port If you are already using port
  5000, or you want to run multiple local registries to separate areas
  of concern, you can customize the registry’s port settings. This
  example runs the registry on port 5001 and also names it
  registry-test. Remember, the first part of the -p value is the host
  port and the second part is the port within the container. Within the
  container, the registry listens on port 5000 by default.

| $ docker run -d
| -p 5001:5000
| --name registry-test
| registry:2 If you want to change the port the registry listens on
  within the container, you can use the environment variable
  REGISTRY\_HTTP\_ADDR to change it. This command causes the registry to
  listen on port 5001 within the container:

| $ docker run -d
| -e REGISTRY\_HTTP\_ADDR=0.0.0.0:5001
| -p 5001:5001
| --name registry-test
| registry:2
