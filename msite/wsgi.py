"""
WSGI config for msite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
"""

import os, sys
sys.path.append('/Users/orion/git/soyurt')
sys.path.append('/Users/orion/git/soyurt/myvenv/lib/python2.7/site-packages')

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "msite.settings")

application = get_wsgi_application()
