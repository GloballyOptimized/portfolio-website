web: python manage.py collectstatic --noinput && python manage.py migrate --noinput && gunicorn portfolio.wsgi --bind 0.0.0.0:$PORT --workers 2 --timeout 120
