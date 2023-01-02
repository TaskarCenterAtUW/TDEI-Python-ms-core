import json
from .providers import azure_service_bus_topic
from ..resource_errors import ExceptionHandler
from .models.queue_message import QueueMessage


class Topic:
    def __init__(self, config, topic_name):
        self.topic = topic_name
        if config.provider == 'Azure':
            try:
                self.azure = azure_service_bus_topic.AzureServiceBusTopic(topic_name)
            except Exception as e:
                print(f'Failed to initialize Topic with error: {e}')
        else:
            print('Failed to initialize Topic')

    @ExceptionHandler.decorated
    def subscribe(self, subscription=None):
        messages = []
        with self.azure.client:
            receiver = self.azure.client.get_subscription_receiver(
                topic_name=self.azure.topic,
                subscription_name=subscription,
            )
            with receiver:
                received_msgs = receiver.receive_messages(max_message_count=10, max_wait_time=5)
                for message in received_msgs:
                    queue_message = QueueMessage.data_from(str(message))
                    messages.append(queue_message)
                    receiver.complete_message(message)

        return messages

    @ExceptionHandler.decorated
    def publish(self, data=None):
        message = QueueMessage.to_dict(data)
        with self.azure.client:
            sender = self.azure.client.get_topic_sender(topic_name=self.azure.topic, )
            with sender:
                sender.send_messages(self.azure.sender(json.dumps(message)))
                print('Message Sent')
