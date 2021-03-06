"""
WSGI config for mysite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import newrelic.agent
newrelic.agent.initialize()

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")

application = get_wsgi_application()
application = newrelic.agent.WSGIApplicationWrapper(application)

from whitenoise.django import DjangoWhiteNoise
application = DjangoWhiteNoise(application)
