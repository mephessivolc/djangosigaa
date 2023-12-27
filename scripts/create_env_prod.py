#!/usr/bin/env python
import os

"""
    Django SECRET_KEY generator.
"""
from django.utils.crypto import get_random_string

chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(_-=+)'
char = 'abcdefghijklmnopqrstuvwxyz'
sql_password = get_random_string(10, char)

CONFIG_STRING = """
ALLOWED_HOSTS=127.0.0.1, .localhost, 192.168.0.20, 0.0.0.0
DEBUG=False
SECRET_KEY=%s
POSTGRES_USER=home_app
POSTGRES_PASSWORD=home_app_%s
POSTGRES_DB=home_app_dev

SQL_ENGINE=django.db.backends.postgresql
SQL_DATABASE=home_app_dev
SQL_USER=home_app
SQL_PASSWORD=home_app_%s
SQL_HOST=db
SQL_PORT=5432
DATABASE=postgres

EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
EMAIL_PORT=587
EMAIL_HOST=smtp.gmail.com
EMAIL_HOST_USER=localhostEmail
EMAIL_HOST_PASSWORD=localhostSenhas
DEFAULT_FROM_EMAIL=sacola@gmail.com
EMAIL_USE_TLS=True
""".strip()%(get_random_string(50, chars),
             sql_password,
             sql_password
            )

# Writing our configuration file to ".env"
if not os.path.isfile('.env.prod'):
    print("Criando arquivo de configuraoes de ambiente")
    with open('.env.prod', 'w') as configfiles:
        configfiles.write(CONFIG_STRING)
