docker ps -q | xargs docker stop # use rm -f to force.
docker ps --no-trunc -aq | xargs docker rm 
