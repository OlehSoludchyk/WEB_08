import pika, sys

from models import Contact


def main():
    credentials = pika.PlainCredentials('bjdnsbcp', '1fXFZaO7f_UYvejED0smkyvknGBuFVSq')
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(
            host='cow.rmq2.cloudamqp.com', port=5672, credentials=credentials, virtual_host='bjdnsbcp'))
    channel = connection.channel()

    channel.queue_declare(queue='test_campaign', durable=True)

    def callback(ch, method, properties, body):
        pk = body.decode()
        task = Contact.objects(id=pk, completed=False).first()
        if task:
            task.update(set__completed=True)
        ch.basic_ack(delivery_tag=method.delivery_tag)

    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(queue='test_campaign', on_message_callback=callback)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        sys.exit(0)