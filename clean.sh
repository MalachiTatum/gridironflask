sudo docker ps -q | xargs sudo docker stop # use rm -f to force.
sudo docker ps --no-trunc -aq | xargs sudo docker rm
