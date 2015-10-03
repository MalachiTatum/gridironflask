# Clean out the migrations dir
rm -r db/migrations

# Reset the databse (drop and re-create). NOTE: Currently only creates, can't seem to drop from same connection connected with
python manage.py resetdb

# regenerate database migrations based on
python manage.py db init -d db/migrations
python manage.py db migrate -d db/migrations
python manage.py db upgrade -d db/migrations
python -u app.py
