#!/usr/bin/env bash
# starts a Gunicorn process to serve python apps
cd /AirBnB_clone_v4

GUNICORN_CMD_ARGS="--bind=0.0.0.0:5003 --workers=3 --access-logfile=/tmp/airbnb-access.log --error-logfile=/tmp/airbnb-error.log" gunicorn web_dynamic.2-hbnb:app
