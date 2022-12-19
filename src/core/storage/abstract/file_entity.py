from abc import ABC, abstractmethod

class FileEntity(ABC):
    name = ''
    mimetype = 'text/plain'
    filePath = ''
    @abstractmethod
    def __init__(self, name:str, mimetype:str = 'text/plain'):
        self.name = name
        self.mimetype = mimetype
        self.filePath = name
        pass
    @abstractmethod
    def getStream(self):
        pass
    @abstractmethod
    def getBodyText(self):
        pass
    @abstractmethod
    def upload(self, uploadStream):
        pass
