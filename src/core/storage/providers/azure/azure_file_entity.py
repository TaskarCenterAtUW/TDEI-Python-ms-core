from core.storage.abstract import file_entity
from azure.storage.blob import BlobClient

class AzureFileEntity(file_entity.FileEntity):
    blobClient = BlobClient
    def __init__(self, name, mimetype, blobClient):
        super().__init__(name, mimetype)
        self.blobClient = blobClient
    def getStream(self):
        return self.blobClient.download_blob(self.name).readall()
    def getBodyText(self):
        return self.blobClient.download_blob(self.name).content_as_text()
    def upload(self, uploadStream):
        self.blobClient.upload_blob(self.filePath,uploadStream)
    