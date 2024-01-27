#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."
    while ! nc -z $DB_HOST $DB_PORT; do
      sleep 0.1
    done
    echo "PostgreSQL started"
fi
python manage.py flush --no-input
python manage.py makemigrations
python manage.py migrate

echo "from django.contrib.auth import get_user_model; User = get_user_model(); \
      User.objects.filter(email='admin@test.com').exists() or \
      User.objects.create_superuser('admin@test.com', 'admin_Root', \
      first_name='Admin', last_name='Lord', user_phone='+79998889999')" | python manage.py shell

exec "$@"