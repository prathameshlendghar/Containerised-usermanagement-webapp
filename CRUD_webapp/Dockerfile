FROM alpine:latest

RUN apk add python3

WORKDIR /CRUD_webapp

COPY . .

RUN python3 -m venv .venv

RUN .venv/bin/pip install django psycopg2-binary

RUN chmod +x RunScript.sh

RUN ls -l /CRUD_webapp

CMD ["sh","RunScript.sh"]