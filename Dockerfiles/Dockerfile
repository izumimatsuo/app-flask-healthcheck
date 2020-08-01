FROM python:3-alpine

RUN mkdir /app
WORKDIR /app

ADD entrypoint.sh /app/entrypoint.sh
ADD app/ /app

RUN apk update && \
    apk add postgresql-libs && \
    apk add --virtual .build-deps gcc musl-dev postgresql-dev && \
    pip install -r requirements.txt --no-cache-dir && \
    apk --purge del .build-deps

ENV PYTHONPATH "${PYTHONPATH}:/app/}"
ENV FLASK_APP "/app/healthcheck.py"
CMD ["/app/entrypoint.sh"]
