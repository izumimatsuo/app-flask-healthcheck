FROM python:3-alpine

RUN mkdir /project
WORKDIR /project

ADD entrypoint.sh /project/app/entrypoint.sh
ADD app/ /project/app

RUN apk update && \
    apk add postgresql-libs && \
    apk add --virtual .build-deps gcc musl-dev postgresql-dev && \
    pip install -r app/requirements.txt --no-cache-dir && \
    apk --purge del .build-deps

ENV PYTHONPATH "${PYTHONPATH}:app/"
ENV FLASK_APP "app/healthcheck.py"
CMD ["/project/app/entrypoint.sh"]
