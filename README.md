# CS3219-Assignment-1
Docker + ngix server set-up

## Installation of nginx server + docker

1) Clone or download the repo
2) Type `docker-compose build` to build the necessary containers and set up nginx configurations
3) Type `docker-compose up` to launch the server.
4) Type `localhost` or `localhost:80` (same thing) to launch default route.
5) Type `localhost/alternative` for the alternative route.
6) Nginx reverse_proxy uses port 80!

## Closing the server and removing container

- Simply type `docker-compose down` to remove and stop all containers that were built and created from the `docker-compose.yml` file.
