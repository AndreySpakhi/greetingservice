FROM python:3.9-alpine
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /greetingservice
COPY requirements.txt /greetingservice/
RUN pip install -r requirements.txt
COPY . /code/


# FROM python:3.9-alpine
#
# ENV PYTHONUNBUFFERED 1
#
# COPY ./requirements.txt /requirements.txt
#
# # Install postgres client
# RUN apk add --update --no-cache postgresql-client
#
# # Install individual dependencies
# # so that we could avoid installing extra packages to the container
# RUN apk add --update --no-cache --virtual .tmp-build-deps \
# 	gcc libc-dev linux-headers postgresql-dev
# RUN pip install -r /requirements.txt
#
# # Remove dependencies
# RUN apk del .tmp-build-deps
#
# RUN mkdir /greetingservice
# WORKDIR /greetingservice
# COPY ./greetingservice /greetingservice
#
# # [Security] Limit the scope of user who run the docker image
# RUN adduser -D user
#
# USER user