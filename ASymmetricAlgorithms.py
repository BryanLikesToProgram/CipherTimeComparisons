import os
import cryptography
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import utils
from cryptography.hazmat.primitives.asymmetric import padding

### Error Handling ###
class SymmEncryptionError(Exception):
    ## Errors/Exceptions in cipher encryption ##
    pass
class SymmDecryptionError(Exception):
    ## Errors/Exceptions in cipher encryption ##
    pass

class ASymmetricAlgorithms:
    def __init__(self, fileData) :
        self.fileData = fileData

    ### ELLIPTIC CURVE ###
    def ELLIPTICCURVE_Sign(self):
        ## Init Cipher ##
        privKey = ec.generate_private_key(
            ec.SECP384R1(), default_backend() # ECDSA SECP394R1 w/ SHA 256 Hash
        )
        pubKey = privKey.public_key()
        ## Signing Data ##
        sig = privKey.sign(
            self.fileData,
            ec.ECDSA(hashes.SHA256())
        )
        return sig, pubKey
    def ELLIPTICCURVE_Verify(self, sig, publicKey):
        sigVerify = publicKey.verify(sig, self.fileData, ec.ECDSA(hashes.SHA256()))
        return sigVerify

    ### RSA ###
    def RSA_Encrypt(self):
        ## Init Cipher ##
        privKey = rsa.generate_private_key(
            public_exponent=65537,
            key_size=65536,
            backend=default_backend()
        )
        pubKey = privKey.public_key()
        # Serialize Public Key #
        secPubKey = pubKey.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )
        secPubKey.splitlines()[0]
        ## Encrypt Data ##
        encryptedData = pubKey.encrypt(
            self.fileData,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        return encryptedData, privKey
    def RSA_Decrypt(self, privateKey):
        ## Decrypt Data ##
        decryptedData = privKey.decrypt(
            self.fileData,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        return decryptedData
