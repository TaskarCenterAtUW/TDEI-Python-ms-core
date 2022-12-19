from abc import ABC, abstractmethod

class StorageClient(ABC):
    @abstractmethod
    def getContainer(self, name:str): pass
    @abstractmethod
    def getFile(self,containerName:str, fileName:str):pass
    @abstractmethod
    def getFileFromUrl(self,fullUrl:str):pass