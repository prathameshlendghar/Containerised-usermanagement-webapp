FROM alpine:latest

RUN apk add python3

# ENV PYTHONUNBUFFERED 1

# ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /CRUD_webapp

COPY . .

RUN python3 -m venv .venv

RUN .venv/bin/pip install django psycopg2-binary

RUN chmod 777 RunScript.sh

CMD ["sh","RunScript.sh"]