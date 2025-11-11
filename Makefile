WEB_CONTAINER=django

run:
		docker exec -it $(WEB_CONTAINER) python manage.py runserver 0.0.0.0:8000
