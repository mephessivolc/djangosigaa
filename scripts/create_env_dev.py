#!/usr/bin/env python
import os

"""
    Django SECRET_KEY generator.
"""
from django.utils.crypto import get_random_string

chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(_-=+)'

CONFIG_STRING = """
ALLOWED_HOSTS=
SECRET_KEY=%s
""".strip()%get_random_string(50, chars)

# Writing our configuration file to ".env"
if not os.path.isfile('.env.dev'):
    print("Criando arquivo de configuraoes de ambiente")
    with open('.env.dev', 'w') as configfiles:
        configfiles.write(CONFIG_STRING)
