from __future__ import absolute_import, unicode_literals
import os

from celery import Celery
from celery.utils.log import get_logger


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_rabbitmq_test.settings')


app = Celery('django_rabbitmq_test')
# include=['django_rabbitmq_test.tasks'])

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))


