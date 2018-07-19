from __future__ import absolute_import, unicode_literals
import os

from celery import Celery

from kombu import Exchange, Queue


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_rabbitmq_test.settings')


app = Celery('django_rabbitmq_test')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()


app.conf.task_queues = [
    Queue('celery', Exchange('tasks'), routing_key='tasks'), # queue_arguments={'x-max-priority': 10}),
]


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))


