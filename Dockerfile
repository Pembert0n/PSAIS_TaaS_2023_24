FROM python:latest

COPY package.json /app/
COPY *source dest*

WORKDIR /app

RUN *command to start services*

CMD [*final command to start the app*]

