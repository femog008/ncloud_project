FROM python:alpine

LABEL maintainer='femog008@yahoo.co.uk'

ADD . /code

WORKDIR /code

RUN pip install -r requirements.txt

ENTRYPOINT ["python", "app.py"]