FROM python:3.7

ENV DJANGO_SETTINGS_MODULE=settings.prod

# Import project
RUN git clone https://github.com/Xonfall/HeartStone-Django  /django

WORKDIR /django

RUN pip install -r docker/prod/requirements.txt

COPY docker-entrypoint.sh /docker-entrypoint.sh

# Execute migrations and server
RUN chmod +x /docker-entrypoint.sh
ENTRYPOINT ["/docker-entrypoint.sh"]

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

EXPOSE 8000