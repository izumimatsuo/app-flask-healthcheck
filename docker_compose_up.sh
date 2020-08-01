#!/bin/sh

./docker_build.sh

docker-compose -f Dockerfiles/docker-compose.yml up
docker-compose -f Dockerfiles/docker-compose.yml down
