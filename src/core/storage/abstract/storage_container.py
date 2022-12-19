from abc import ABC, abstractmethod

class StorageContainer(ABC):
    @abstractmethod
    def __init__(self, name):
        self.name = name
        pass
    @abstractmethod
    def listFiles(self):
        pass
    @abstractmethod
    def createFile(self,name,mimetype):
        pass