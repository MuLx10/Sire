FROM ubuntu:18.04
FROM python:3.7 
LABEL maintainer="Mehul Kumar Nirala <mehulkumarnirala@gmail.com>"

ADD . /app
WORKDIR /app

RUN pip install -r requirements.txt

RUN chmod +x /app/app.py
CMD python3 /app/app.py
