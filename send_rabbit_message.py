import base64
import json
import pika
import uuid


args = dict()

args['server'] = 'localhost'
args['port'] = '5672'
args['virtual_host'] = 'testhost'
args['username'] = 'testuser'
args['password'] = 'testpassword'


# set amqp credentials
credentials = pika.PlainCredentials(args['username'], args['password'])
# set amqp connection parameters
parameters = pika.ConnectionParameters(host=args['server'], port=args['port'], virtual_host=args['virtual_host'], credentials=credentials)#, ssl=args['ssl'])

# try to establish connection and check its status
try:
  connection = pika.BlockingConnection(parameters)
  if connection.is_open:
    print('OK')
    connection.close()
    # exit(0)
except Exception as error:
  print('Error:', error.__class__.__name__)
  exit(1)


connection = pika.BlockingConnection(parameters)
channel = connection.channel()

channel.queue_declare(queue='celery', durable=True)

body = {'task': 'myapp.tasks.add', 'id': '54086c5e-6193-4575-8308-dbab76798756', 'args': [4, 4], 'kwargs': {}}


message_string = json.dumps(body)
byte_message = base64.b64encode(message_string.encode('utf-8'))
base64_json_string = byte_message.decode()


channel.basic_publish(exchange='tasks',
                      routing_key='tasks',
                      body=message_string,
                      properties=pika.BasicProperties(
                          correlation_id=str(uuid.uuid4()),
                          content_encoding='utf-8',
                          content_type='application/json',
                          headers={
                            'lang': 'py',
                            'task': 'myapp.tasks.add',
                            }
                          ),
                      )


print(" [x] Sent 'Hello World!'")

connection.close()
