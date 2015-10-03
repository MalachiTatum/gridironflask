./clean.sh
./build.sh
sudo docker run --name postgres-db -p 5432:5432 -d postgres
