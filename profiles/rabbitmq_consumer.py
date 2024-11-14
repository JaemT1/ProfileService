import json
import pika
from django.conf import settings
from django.core.management.base import BaseCommand
from .models import Perfil


def process_message(ch, method, properties, body):
    # Decodificar el mensaje recibido
    message = json.loads(body)
    opcion = message.get('opcion')
    id_usuario = message.get('id')

    # Procesar el mensaje de acuerdo al tipo de evento
    if opcion == 'signup':
        # Crear un nuevo perfil cuando se crea un usuario
        Perfil.objects.create(id=id_usuario)
        print(f'Perfil creado para el usuario con ID {id_usuario}')
    elif opcion == 'delete':
        # Eliminar el perfil cuando se elimina un usuario
        Perfil.objects.filter(id=id_usuario).delete()
        print(f'Perfil eliminado para el usuario con ID {id_usuario}')


class Command(BaseCommand):
    help = 'Start RabbitMQ consumer'

    def handle(self, *args, **options):
        # Configurar la conexión a RabbitMQ
        credentials = pika.PlainCredentials(settings.RABBITMQ_USER, settings.RABBITMQ_PASSWORD)
        connection = pika.BlockingConnection(
            pika.ConnectionParameters(host=settings.RABBITMQ_HOST, port=settings.RABBITMQ_PORT, credentials=credentials)
        )
        channel = connection.channel()

        # Declarar la cola a la que este servicio estará suscrito
        channel.queue_declare(queue=settings.RABBITMQ_QUEUE, durable=True)

        # Consumir mensajes de la cola
        channel.basic_consume(queue=settings.RABBITMQ_QUEUE, on_message_callback=process_message, auto_ack=True)

        print('Esperando mensajes de RabbitMQ...')
        channel.start_consuming()