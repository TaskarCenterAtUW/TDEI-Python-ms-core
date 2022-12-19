from core.storage.abstract import storage_client
from azure.storage.blob import BlobServiceClient
from core.storage.providers.azure import azure_storage_config

class AzureStorageClient(storage_client.StorageClient):
    blobServiceClient: BlobServiceClient
    def __init__(self,config:azure_storage_config.AzureStorageConfig):
        super().__init__()
        self.blobServiceClient = BlobServiceClient.from_connection_string(config.connection_string)
    def getContainer(self, name):
        return super().getContainer(name)
    def getFile(self, containerName, fileName):
        return super().getFile(containerName, fileName)
    def getFileFromUrl(self, fullUrl):
        return super().getFileFromUrl(fullUrl)
