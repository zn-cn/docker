FROM molscar/python_flask_uwsgi:python3.6

COPY . /app
WORKDIR /app/src

CMD [ "uwsgi", "--ini", "uwsgi/uwsgi.ini" ]
