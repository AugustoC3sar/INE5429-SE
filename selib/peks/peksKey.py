from selib.key import Key
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes

class PEKSKey(Key):
    def __init__(self):
        self._key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    
    def serialize(self):
        return self._key.public_key().public_bytes(encoding=serialization.Encoding.PEM, format=serialization.PublicFormat.SubjectPublicKeyInfo)

    def encrypt(self, data:bytes):
        pad = padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None)
        
        return self._key.public_key().encrypt(data, pad)
    
    def sign(self, data:bytes):
        pad = padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None)
        
        return self._key.sign(data, pad)