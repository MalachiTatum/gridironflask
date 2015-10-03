source clean.sh
source build.sh
sudo docker run -p 5000:5000 hello_world &
sudo docker run --name postgres-db -p 5432:5432 -d postgres
sudo docker run -p 5000:5001 --link postgres-db:db -d flask
