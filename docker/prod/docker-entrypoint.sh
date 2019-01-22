#!/bin/bash

echo "Launch migrations..."
python manage.py makemigrations

echo "Update database..."
python manage.py migrate

# Start Gunicorn processes
echo "Starting Gunicorn..."
exec gunicorn heartstone.wsgi:application \
    --bind 0.0.0.0:8000 \
    --workers 3

exec "$@"