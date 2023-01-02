import os
import json
import requests
from dotenv import load_dotenv
from .providers import azure_service_bus_queue
from ..resource_errors import ExceptionHandler
from .models.queue_message import QueueMessage

load_dotenv()


class Queue:
    queue = list()

    def __init__(self, config, queue_name=None):
        self.queue_name = queue_name
        if config.provider == 'Azure':
            try:
                self.azure = azure_service_bus_queue.AzureServiceBusQueue(config, queue_name)
            except Exception as e:
                print(f'Failed to initialize queue with error: {e}')
        elif config.provider == 'Local':
            print('Will send massages to localhost')
        else:
            print('Failed to initialize queue')

    @ExceptionHandler.decorated
    def send(self, data=None):
        if data:
            message = QueueMessage.to_dict(data)
            with self.azure.client:
                sender = self.azure.client.get_queue_sender(queue_name=self.azure.queue_name)
                with sender:
                    sender.send_messages(self.azure.sender(json.dumps(message)))
        self.queue = list()

    def send_local(self, data=None):
        if data:
            message = QueueMessage.to_dict(data)
            url = os.environ.get('CALLBACK_URL', 'http://127.0.0.1:8000/logs')
            resp = requests.post(url, json=message)
            print(resp.status_code)
        self.queue = list()

    def add(self, data):
        if data is not None:
            self.queue.insert(0, json.dumps(data))

    def remove(self):
        if len(self.queue) > 0:
            self.queue.pop()

    def get_items(self):
        return self.queue
