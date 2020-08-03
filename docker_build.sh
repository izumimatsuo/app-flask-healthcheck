#!/bin/sh

rsync -av app Dockerfiles
echo 'psycopg2' >> Dockerfiles/app/requirements.txt
echo 'PyMySQL' >> Dockerfiles/app/requirements.txt
echo 'gunicorn' >> Dockerfiles/app/requirements.txt

docker build -t healthcheck-api Dockerfiles --build-arg HTTPS_PROXY=${HTTPS_PROXY} 
