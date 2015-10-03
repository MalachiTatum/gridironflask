source build.sh
docker run --name postgres-db -p 5432:5432 -d postgres
docker run -p 5000:5000 --link postgres-db:db -d flask
