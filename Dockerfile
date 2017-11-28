FROM gliderlabs/alpine:latest

RUN apk add --update \
    python \
    py-pip \
  && pip install flask -U \
  && pip install pyyaml -U \
  && rm -rf /var/cache/apk/* \
  && adduser -D app \
  && mkdir /app  \
  && chown -R app:app /app

USER app
WORKDIR /app
ADD app.py app.py
ADD laptimes.yml laptimes.yml

VOLUME /tmp

ENV FLASK_APP=app.py
ENTRYPOINT flask run

