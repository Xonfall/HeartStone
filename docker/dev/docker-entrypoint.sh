#!/bin/bash

echo "Launch migrations..."
python manage.py makemigrations

echo "Update database..."
python manage.py migrate

echo "Start server..."
python manage.py runserver 0.0.0.0:8000