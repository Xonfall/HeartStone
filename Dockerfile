FROM python:3.6

ARG requirements=requirements.txt
ENV DJANGO_SETTINGS_MODULE=heartstone.settings.prod

RUN git clone https://github.com/Xonfall/HeartStone-Django django
WORKDIR /django

#COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

#COPY . /app
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]