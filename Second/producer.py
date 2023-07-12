import pika

from models import Contact

credentials = pika.PlainCredentials('bjdnsbcp', '1fXFZaO7f_UYvejED0smkyvknGBuFVSq')
connection = pika.BlockingConnection(
    pika.ConnectionParameters(
        host='cow.rmq2.cloudamqp.com', port=5672, credentials=credentials, virtual_host='bjdnsbcp'))
channel = connection.channel()

channel.exchange_declare(exchange='test_service', exchange_type='direct')
channel.queue_declare(queue='test_campaign', durable=True)
channel.queue_bind(exchange='test_service', queue='test_campaign')


def main():
    for i in range(1, 11):
        task = Contact(consumer=f"Name{i}", email=f"email@com{i}").save()

        channel.basic_publish(exchange='test_service', routing_key='test_campaign', body=str(task.id).encode(),
                              properties=pika.BasicProperties(delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE))

    connection.close()


if __name__ == '__main__':
    main()