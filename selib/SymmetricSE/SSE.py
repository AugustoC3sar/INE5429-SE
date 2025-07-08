from selib.scheme import Scheme
from selib.SymmetricSE.symmetricKey import SymmetricKey
from selib.data import Data
import hashlib

class SSE(Scheme):

    def keygen(self):
        return SymmetricKey()

    def build_index(self, data:Data, key:SymmetricKey):
        encrypted_keyword = key.encrypt(data.keyword().encode())
        return hashlib.sha256(encrypted_keyword).hexdigest()

    def trapdoor(self, key:SymmetricKey, keyword:str):
        encrypted_keyword = key.encrypt(keyword.encode())
        trapdoor = hashlib.sha256(encrypted_keyword).hexdigest()
        return trapdoor
