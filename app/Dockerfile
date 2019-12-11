FROM python:3.6

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


RUN pip install --upgrade pip
COPY requirements.txt ./

RUN pip3 install -r requirements.txt

COPY . /usr/src/app/