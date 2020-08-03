#!/bin/sh

sleep 30
gunicorn healthcheck:api -b 0.0.0.0:5000 --access-logfile - --capture-output
