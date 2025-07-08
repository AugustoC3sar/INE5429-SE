from selib.key import Key
from cryptography.fernet import Fernet

class SymmetricKey(Key):
    def __init__(self):
        self._key = Fernet.generate_key()
    
    def serialize(self):
        return self._key
    
    def encrypt(self, data:bytes):
        return Fernet(self._key).encrypt(data)
