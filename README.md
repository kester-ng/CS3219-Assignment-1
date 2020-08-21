# CS3219-Assignment-1
Docker + ngix server set-up

## Installation of nginx server + docker

1) Clone or download the repo
2) Type `docker-compose build` to build the necessary containers and set up nginx configurations
3) Type `docker-compose up` to launch the server.
4) Go to any browser and type `localhost` or `localhost:80` to launch a simple web page.

## Closing the server and removing container

- Simply type `docker-compose down` to remove and stop all containers that were built and created from the `docker-compose.yml` file.