FROM alpine:3.9.6

ENV TERM=linux

RUN apk add --no-cache bash mongodb

RUN mkdir -p /data/db && \
    chown -R mongodb /data/db

RUN apk add --update --no-cache python3 && ln -sf python3 /usr/bin/python
RUN python3 -m ensurepip
RUN pip3 install --no-cache --upgrade pip setuptools

RUN pip install flask \
    requests \ 
    pymongo

VOLUME /data/db
EXPOSE 5002

WORKDIR /app
COPY . /app/

RUN chmod +x /app/*

ENTRYPOINT [ "python","db.py" ]

CMD [ "mongod", "--bind_ip", "0.0.0.0"]