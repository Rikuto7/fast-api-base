FROM python:3.9-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1
ENV PYTHONPATH /

WORKDIR /backend

RUN apt update \
    && apt-get -y install gcc libmariadb-dev \
    && apt install -y default-mysql-client \
    && apt-get install -y default-libmysqlclient-dev \
    && apt install --no-install-recommends -y tzdata \
    && apt-get install -y git \
    && apt clean

COPY /requirements.txt /requirements.txt
RUN pip install --upgrade pip
RUN pip install -r /requirements.txt --no-cache-dir

COPY . /backend

EXPOSE 80
CMD [ 'gunicorn',  'api.main:app', '--workers=4', '--worker-class=uvicorn.workers.UvicornWorker', '--bind=0.0.0.0:8000' ]
