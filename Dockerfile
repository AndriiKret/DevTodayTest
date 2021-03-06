FROM python:3.8

RUN mkdir api
WORKDIR api
COPY requirements.txt requirements.txt

RUN pip install --upgrade pip && \
    pip install -r requirements.txt
