import os
import sys

os.environ['DJANGO_SETTINGS_MODULE'] = 'upthere.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
path = '/home/ubuntu/srv/upthere/upthere'
if path not in sys.path:
    sys.path.append(path)
