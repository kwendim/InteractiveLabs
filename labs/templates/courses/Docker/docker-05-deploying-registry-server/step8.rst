Deploy your registry using a Compose file If your registry invocation is
advanced, it may be easier to use a Docker compose file to deploy it,
rather than relying on a specific docker run invocation. Use the
following example docker-compose.yml as a template.

registry: restart: always image: registry:2 ports: - 5000:5000
environment: REGISTRY\_HTTP\_TLS\_CERTIFICATE: /certs/domain.crt
REGISTRY\_HTTP\_TLS\_KEY: /certs/domain.key REGISTRY\_AUTH: htpasswd
REGISTRY\_AUTH\_HTPASSWD\_PATH: /auth/htpasswd
REGISTRY\_AUTH\_HTPASSWD\_REALM: Registry Realm volumes: -
/path/data:/var/lib/registry - /path/certs:/certs - /path/auth:/auth
Replace /path with the directory which contains the certs/ and auth/
directories.

Start your registry by issuing the following command in the directory
containing the docker-compose.yml file:

$ docker-compose up -d
