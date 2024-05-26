APP_PATH := app
HURL_URL := http://localhost:8000

dev-deps: deps data

deps:
	cd $(APP_PATH) && poetry install

data: static migrations superuser

static:
	cd $(APP_PATH) && python manage.py collectstatic --clear --noinput

migrations:
	cd $(APP_PATH) && python manage.py flush --no-input && python manage.py migrate

superuser:
	cd $(APP_PATH) && echo "from django.contrib.auth import get_user_model; User = get_user_model(); \
      User.objects.filter(email='admin@test.com').exists() or \
      User.objects.create_superuser('admin@test.com', 'admin_Root', \
      first_name='Admin', last_name='Lord', user_phone='+79998889999')" | python manage.py shell

run-app:
	cd $(APP_PATH) && gunicorn amedice.wsgi:application --bind 0.0.0.0:8000 --workers=2 --reload

db-filling:
	export HURL_URL=$(HURL_URL) && hurl --retry 5 --test --very-verbose hurl/dev/*.hurl

.PHONY: dev-deps deps data static migrations superuser db_filling
