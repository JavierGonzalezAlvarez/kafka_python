FROM python:3.9
ENV PYTHONUNBUFFERED 1

RUN mkdir -p /app
WORKDIR /app
COPY . /app/
COPY requirements.txt /app/
RUN pip install -r requirements.txt

