FROM python:3.7.15-alpine3.16

COPY . .

EXPOSE 5002

RUN pip install flask \
    requests \
    pymongo \
    flask_pymongo

# ENTRYPOINT [ "python","db.py" ]
CMD ["sh", "-c", "python db.py --MONGODB_DATABASE ${MONGODB_DATABASE} --MONGODB_USERNAME ${MONGODB_USERNAME} --MONGODB_PASSWORD: ${MONGODB_PASSWORD} --MONGODB_HOSTNAME: ${MONGODB_HOSTNAME} "]
