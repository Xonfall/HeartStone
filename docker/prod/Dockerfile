FROM python:3.6

ENV DJANGO_SETTINGS_MODULE=settings.prod

RUN git clone https://github.com/Xonfall/HeartStone-Django django

WORKDIR /django

RUN pip install -r requirements.txt

COPY docker-entrypoint.sh /docker-entrypoint.sh

RUN chmod +x /docker-entrypoint.sh
ENTRYPOINT ["/docker-entrypoint.sh"]

EXPOSE 8000