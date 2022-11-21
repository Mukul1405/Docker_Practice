FROM python:3.7.15-alpine3.16

COPY . .

EXPOSE 5001

RUN pip install flask 
ENTRYPOINT [ "python" ]
CMD [ "main.py" ]
