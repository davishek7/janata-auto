release: python manage.py migrate
web: gunicorn janata.wsgi --log-file -
worker: python manage.py qcluster