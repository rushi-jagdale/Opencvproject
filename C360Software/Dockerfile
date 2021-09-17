FROM python:3

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirement.txt requirement.txt
RUN pip3 install -r requirement.txt

COPY . /app
