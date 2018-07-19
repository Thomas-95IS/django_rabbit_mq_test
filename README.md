`$ sudo apt-get install rabbitmq-server`

`$ pipenv shell`

`$ pip install celery`

```
$ sudo rabbitmqctl add_user testuser testpassword

$ sudo rabbitmqctl add_vhost testhost

$ sudo rabbitmqctl set_user_tags testuser mytag

$ sudo rabbitmqctl set_permissions -p testhost testuser ".*" ".*" ".*"
```


CHeck it's running:

ps aux | grep epmd

Stop it:

sudo rabbitmqctl stop

Run it:

sudo rabbitmq-server


http://docs.celeryproject.org/en/latest/django/first-steps-with-django.html


celery -A django_rabbitmq_test worker --loglevel=info -E

sudo rabbitmqctl list_queues name messages messages_ready messages_unacknowledged  # default virtualhost

sudo rabbitmqctl list_queues name messages messages_ready messages_unacknowledged -p testhost


python send_rabbit_message.py 


If it breaks: sudo service rabbitmq-server restart 
