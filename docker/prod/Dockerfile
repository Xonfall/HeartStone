FROM python:3.7

ENV DJANGO_SETTINGS_MODULE=settings.prod
ENV URL_DJANGO_PROJECT=https://github.com/Xonfall/HeartStone-Django

# Import project
RUN git clone $URL_DJANGO_PROJECT /django

WORKDIR /django

RUN pip install -r docker/prod/requirements.txt
RUN pip install gunicorn

COPY docker-entrypoint.sh /docker-entrypoint.sh

# Execute migrations and server
RUN chmod +x /docker-entrypoint.sh
ENTRYPOINT ["/docker-entrypoint.sh"]

EXPOSE 8000