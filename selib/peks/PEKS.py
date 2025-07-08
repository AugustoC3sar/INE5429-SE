from selib.scheme import Scheme
from selib.peks.peksKey import PEKSKey
from selib.data import Data
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.backends import default_backend
import hashlib


class PEKS(Scheme):

    def keygen(self):
        return PEKSKey()
    
    def build_index(self, data:Data, key:bytes):
        public_key = serialization.load_pem_public_key(key, default_backend())
        pad = padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None)
        
        encrypt_data = public_key.encrypt(data.keyword().encode(), pad)
        return hashlib.sha256(encrypt_data).hexdigest()
    
    def trapdoor(self, key:PEKSKey, keyword:str):
        encrypted_keyword = key.sign(keyword.encode())
        trapdoor = hashlib.sha256(encrypted_keyword).hexdigest()
        return trapdoor