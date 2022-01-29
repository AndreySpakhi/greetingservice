FROM python:3.9-alpine
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /greetingservice
COPY requirements.txt /greetingservice/
RUN pip install -r requirements.txt
COPY . /greetingservice/