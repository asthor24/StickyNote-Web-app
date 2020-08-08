"""
WSGI config for try_django project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os
import try_django
from django.core.wsgi import get_wsgi_application

print("starting from here so its finding the wsgi.py file")
#os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'try_django.settings')

application = get_wsgi_application()
