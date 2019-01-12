FROM python:3.6

ENV DJANGO_SETTINGS_MODULE=heartstone.settings.dev

# COPY settings files
COPY requirements.txt /app/requirements.txt
COPY docker-entrypoint.sh /docker-entrypoint.sh

WORKDIR /app

RUN pip install -r requirements.txt

# COPY project in container
COPY . /app

# Execute migrations and server
RUN chmod +x /docker-entrypoint.sh
ENTRYPOINT ["/docker-entrypoint.sh"]

EXPOSE 8000

