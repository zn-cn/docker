FROM python:3.6

COPY src /app/src
WORKDIR /app/src

RUN pip install pymongo flask uwsgi

CMD [ "--ini", "uwsgi/uwsgi.ini" ]
ENTRYPOINT [ "uwsgi" ]