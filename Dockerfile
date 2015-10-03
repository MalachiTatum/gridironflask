FROM ubuntu:14.04

RUN sudo apt-get update
RUN sudo apt-get install -y python python-pip python-virtualenv nginx gunicorn
RUN sudo pip install Flask==0.10.1
EXPOSE 5000

COPY . /gridironflask

WORKDIR /gridironflask
RUN pip install -r requirements.txt

CMD [ "python", "-u", "app.py" ] 
