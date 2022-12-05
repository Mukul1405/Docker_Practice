FROM python:3.7.15-alpine3.16

WORKDIR /app
ADD . /app/

EXPOSE 5002

RUN pip install flask \
    requests \
    pymongo 

ENTRYPOINT [ "python" ]
CMD ["db.py"]
