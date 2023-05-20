FROM python:3.11-slim

COPY ./src /app/src
COPY ./alembic /app/alembic
COPY ./requirements.txt /app
COPY ./docker /app/docker
COPY ./alembic.ini /app
WORKDIR /app
RUN chmod a+x docker/*.sh
RUN pip3 install -r requirements.txt
EXPOSE 8000





