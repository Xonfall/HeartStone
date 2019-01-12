FROM python:3.6

ENV DJANGO_SETTINGS_MODULE=settings.prod

RUN git clone https://github.com/Xonfall/HeartStone-Django  /django/
RUN mkdir /app; cp -R /django/* /app/

WORKDIR /app

RUN pip install -r docker/prod/requirements.txt

COPY docker-entrypoint.sh /docker-entrypoint.sh

RUN chmod +x /docker-entrypoint.sh
ENTRYPOINT ["/docker-entrypoint.sh"]

EXPOSE 8000