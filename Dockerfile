FROM python:3

ENV PYTHONUNBUFFERED 1
RUN mkdir /justwork
RUN mkdir /justwork/staticfiles
RUN mkdir /justwork/mediafiles

WORKDIR /justwork

RUN pip install --upgrade pip
COPY requirements.txt /justwork/
RUN pip install -r requirements.txt

COPY . /justwork/