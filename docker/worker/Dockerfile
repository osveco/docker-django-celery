# use base python image with python 3.7
FROM python:3.6

USER root

# add requirements.txt to the image
ADD requirements.txt /app/requirements.txt

# Project Files and Settings
COPY myproject/manage.py /app/manage.py
RUN mkdir -p /app/myproject
COPY myproject/myproject/* /app/myproject/
WORKDIR /app

# install python dependencies
RUN pip install -r /app/requirements.txt

# create unprivileged user
RUN adduser --disabled-password --gecos '' myuser

# Server
EXPOSE 8000
STOPSIGNAL SIGINT

CMD su -m myuser -c "celery worker -A myproject.celeryconf -Q default -n default@%h"
