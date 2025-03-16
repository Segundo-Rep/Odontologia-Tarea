#!/bin/bash
# start.sh

pip install -r requirements.txt

# Ejecutar migraciones
python manage.py makemigrations
python manage.py migrate

# Iniciar el servidor
