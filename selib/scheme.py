from abc import ABC, abstractmethod
from typing import Any
from selib.key import Key
from selib.data import Data

class Scheme(ABC):

    @abstractmethod
    def keygen(self) -> Key:
        raise NotImplementedError
    
    @abstractmethod
    def build_index(self, data:Any, key:Key) -> bytes:
        raise NotImplementedError
    
    @abstractmethod
    def trapdoor(self, key:Key, keyword:str) -> bytes:
        raise NotImplementedError
    
