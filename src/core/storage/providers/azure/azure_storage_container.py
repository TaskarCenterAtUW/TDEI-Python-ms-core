from core.storage.abstract import storage_container
from azure.storage.blob import ContainerClient
from core.storage.providers.azure import azure_file_entity

class AzureStorageContainer(storage_container.StorageContainer):
    containerClient = ContainerClient
    def __init__(self, name, containerClient:ContainerClient):
        super().__init__(name)
        self.containerClient = containerClient
    def listFiles(self):
        blobIterator = self.containerClient.list_blobs()
        filesList = [azure_file_entity.AzureFileEntity]
        for singleItem in blobIterator:
            blobClient = self.containerClient.get_blob_client(singleItem.name)
            filesList.append(azure_file_entity.AzureFileEntity(singleItem.name,singleItem.content_settings.content_type,blobClient=blobClient))
        return filesList
    def createFile(self, name, mimetype):
        return super().createFile(name, mimetype)
    