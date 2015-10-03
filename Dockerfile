FROM ubuntu:14.04

USER root
RUN echo "jenkins ALL=NOPASSWD: ALL" >> /etc/sudoers
RUN echo "DOCKER_OPTS=' -G jenkins'" >> /etc/default/docker
USER jenkins

RUN sudo apt-get update
RUN sudo apt-get install -y python python-pip python-virtualenv nginx gunicorn
RUN sudo pip install Flask==0.10.1

EXPOSE 5000

COPY . /gridironflask

WORKDIR /gridironflask

CMD [ "python", "-u", "app.py" ] 
