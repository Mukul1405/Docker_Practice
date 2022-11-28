FROM python:3.7.15-alpine3.16

WORKDIR /app
COPY . /app/

RUN pip install requests

ENTRYPOINT ["python"]
CMD ["main.py"]