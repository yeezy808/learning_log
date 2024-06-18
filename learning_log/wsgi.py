"""
WSGI config for learning_log project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from django.core.handlers.wsgi import WSGIHandler

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'learning_log.settings')

application = get_wsgi_application()
application = WSGIHandler()
application.load_middleware()

def serve_application(environ, start_response):
	return application(environ, start_response)

if __name__ == '__main__':
	from waitress import serve
	serve(serve_application, host='0.0.0.0', port=8000)
