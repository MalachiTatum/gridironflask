FROM ubuntu:14.04
RUN sudo apt-get update
RUN  sudo apt-get install -y python python-pip python-virtualenv nginx gunicorn

RUN sudo pip install Flask==0.10.1

# Dependencies for talking to and migrating postgres db
RUN sudo apt-get install -y python-psycopg2
RUN sudo pip install Flask-SQLAlchemy Flask-Migrate
RUN sudo pip freeze > requirements.txt

EXPOSE 5000

COPY . /gridironflask

WORKDIR /gridironflask

CMD ["/bin/bash", "start-app.sh"]
