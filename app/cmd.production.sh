#!/usr/bin/env bash

set -e
set -x

# Make sure that the static volume is updated if the image has been rebuilt
python manage.py collectstatic --noinput

# Migrate any database changes
python manage.py migrate

# Exec so that gunicorn replaces this process and gets all of the signals from Docker
exec gunicorn hellodjocker.wsgi --bind 0.0.0.0:9000 --workers 2
