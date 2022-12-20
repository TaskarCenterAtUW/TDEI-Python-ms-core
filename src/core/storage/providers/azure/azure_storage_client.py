from azure.storage.blob import BlobServiceClient
from core.storage.abstract import storage_client
from core.storage.providers.azure import azure_storage_config, azure_file_entity, azure_storage_container

class AzureStorageClient(storage_client.StorageClient):
    _blobServiceClient: BlobServiceClient
    def __init__(self,config:azure_storage_config.AzureStorageConfig):
        super().__init__()
        self._blobServiceClient = BlobServiceClient.from_connection_string(config.connection_string)
    def getContainer(self, name):
        clientContainer = self._blobServiceClient.get_container_client(name)
        return azure_storage_container.AzureStorageContainer(name,clientContainer)
    def getFile(self, containerName, fileName):
         containerClient = self._blobServiceClient.get_container_client(containerName)
         blobClient = containerClient.get_blob_client(fileName)
         properties = blobClient.get_blob_properties()
         return azure_file_entity.AzureFileEntity(fileName,properties.blob_type,blobClient=blobClient)
    def getFileFromUrl(self, fullUrl):
        return super().getFileFromUrl(fullUrl)
