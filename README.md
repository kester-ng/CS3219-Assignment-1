# CS3219-Assignment-1

Docker + ngix server set-up

## Installation of nginx server + docker

1. Clone or download the repo
2. Type `docker-compose build` to build the necessary containers and set up nginx configurations
3. Type `docker-compose up` to launch the server.
4. Type `localhost` or `localhost:80` (same thing) to launch default route. You should see a webpage with `ASSIGNMENT 1 DEFAULT ROUTE`.
5. Type `localhost/alternate` for the alternative route. You should see a webpage with `ASSIGNMENT 1 ALTERNATE ROUTE`.
6. Nginx reverse_proxy uses port 80!
7. The reverse proxy configurations is at `nginx.conf`. Please take a look!
8. The server is now acting as a gateway where default path `/` directs to default route webpage whereas `/alternate` directs to alternate route webpage and both webpages are powered by different docker images!

## Closing the server and removing container

- Simply type `docker-compose down` to remove and stop all containers that were built and created from the `docker-compose.yml` file.
