FROM python:3.7

ENV DJANGO_SETTINGS_MODULE=heartstone.settings.dev

# COPY settings files
COPY requirements.txt /app/requirements.txt
COPY docker-entrypoint.sh /docker-entrypoint.sh

WORKDIR /app

RUN pip install -r requirements.txt

# COPY project in container
COPY . /app

# Execute migrations
RUN chmod +x /docker-entrypoint.sh
ENTRYPOINT ["/docker-entrypoint.sh"]

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

EXPOSE 8000