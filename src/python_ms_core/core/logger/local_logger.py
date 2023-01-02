from .providers.azure_logger_config import AzureLoggerConfig
from ..queue.models.queue_message import QueueMessage
from ..queue.queue import Queue
from .abstracts.logger_abstract import LoggerAbstract


class LocalLogger(LoggerAbstract):

    def __init__(self, provider_config=None):
        super().__init__(provider_config=None)
        self.config = AzureLoggerConfig(provider_config=provider_config)
        self.queue_client = Queue(self.config, queue_name=None)

    def add_request(self, request_data):
        message = QueueMessage.data_from({
            'message': 'Add Request',
            'messageType': 'addRequest',
            'data': request_data
        })
        self.queue_client.send_local(message)

    def info(self, message: str):
        message = QueueMessage.data_from({
            'message': message,
            'messageType': 'info',
        })
        self.queue_client.send_local(message)

    def debug(self, message: str):
        message = QueueMessage.data_from({
            'message': message,
            'messageType': 'debug',
        })
        self.queue_client.send_local(message)

    def record_metric(self, name: str, value: str):
        message = QueueMessage.data_from({
            'message': 'metric',
            'messageType': 'metric',
            'data': {
                'name': name,
                'value': value
            }
        })
        self.queue_client.send_local(message)
