FROM python:3.7-alpine

ADD tcp_server.py /

EXPOSE 6789

CMD [ "python", "-c", "./tcp_server.py" ]
