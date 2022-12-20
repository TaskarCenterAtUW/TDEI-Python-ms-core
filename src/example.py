# Testing code
import os
from main import Core
# from core.queue.providers import azure_queue_config
from dotenv import load_dotenv
# from azure.storage.blob import BlobServiceClient, ContainerClient
# from core.storage.providers.azure import azure_storage_client

load_dotenv()

# Core.initialize()
# print('Hello')

# topic = 'gtfs-flex-upload'
# subscription = 'uploadprocessor'
# some_other_sub = 'usdufs'

# topic_config = azure_queue_config.AzureQueueConfig()

# a = Core.get_topic(topic)
# print(a)
# Find and get the list of files
# print(os.environ.get('STORAGECONNECTION',''))
# blob_service_client : BlobServiceClient = BlobServiceClient.from_connection_string(os.environ.get('STORAGECONNECTION',''))
# blob_container_client: ContainerClient = blob_service_client.get_container_client('gtfspathways')
# iterator = blob_container_client.list_blobs()
# for item in iterator:
#     print("\t"+item.name)
#     print("\t"+item.content_settings.content_type)

azureclient = Core.get_storage_client()
container = azureclient.getContainer('tdei-storage-test')
listOfFiles = container.listFiles()
for single in listOfFiles:
    print(single.name)

firstFile = listOfFiles[2]
# print(firstFile.name+'<><>')
fileContent = firstFile.getBodyText()
print(fileContent)
