from abc import ABC, abstractmethod

class Key(ABC):

    def __str__(self):
        return self.serialize().decode()

    @abstractmethod
    def serialize(self) -> bytes:
        raise NotImplementedError

    @abstractmethod
    def encrypt(self, data:bytes):
        raise NotImplementedError