# Backend API

[![Build Status](https://travis-ci.org/comp490-group3/backend-api.svg?branch=master)](https://travis-ci.org/comp490-group3/backend-api)

## Django Commands
python manage.py makemigrations punchd
python manage.py migrate
python manage.py createsuperuser

## Docker Usage
```
docker build -t comp490-group3/api .
docker run -it --rm -p 5000:5000 comp490-group3/api
```
API will now be running on ${DOCKER_HOST}:5000
