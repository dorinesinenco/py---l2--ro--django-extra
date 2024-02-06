#!/bin/bash
source venv/bin/activate
docker-compose up --detach
python3 e-shop---rest-api/manage.py runserver
