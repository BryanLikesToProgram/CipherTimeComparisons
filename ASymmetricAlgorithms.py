import time
import os
import io
import cryptography
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import utils
from cryptography.hazmat.primitives.asymmetric import padding
class ELLIPTICCURVE:
    def __init__(self, filename) :
        self.fileName = filename
        print("Cipher: Elliptic Curve")

    def ThreeEightFourROne(self) :
        print("Mode: ECDSA SECP394R1 w/ SHA 256 Hash")
        inFile = open(self.fileName, 'rb')
        fileData = inFile.read()
        inFile.close()

        privKey = ec.generate_private_key(
            ec.SECP384R1(), default_backend()
        )
        pubKey = privKey.public_key()
        startEncTime = time.time()
        #----------- Start
        sig = privKey.sign(
            fileData,
            ec.ECDSA(hashes.SHA256())
        )
        #----------- End
        endEncTime = time.time() - startEncTime
        print("Signing Time: " + str(endEncTime))
        startDecTime = time.time()
        #----------- Start
        sigVerify = pubKey.verify(sig, fileData, ec.ECDSA(hashes.SHA256()))
        #----------- End
        endDecTime = time.time() - startDecTime
        print("Verify Time: " + str(endDecTime))
        print("Signature Anomalies: "+str(sigVerify))
        print("")
        
class RSA:
    def __init__(self, filename) :
        self.fileName = filename
        print("Cipher: RSA")
    def PemSerialized(self) :
        print("Mode: 65537 Pem Serialized Key ")
        inFile = open(self.fileName, 'rb')
        fileData = inFile.read()
        inFile.close()

        privKey = rsa.generate_private_key(
            public_exponent=65537,
            key_size=8192,
            backend=default_backend()
        )
        pubKey = privKey.public_key()

        ### Serialize Public Key ###
        secPubKey = pubKey.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )
        secPubKey.splitlines()[0]

        startEncTime = time.time()
        #----------- Start
        encryptedData = pubKey.encrypt(
            fileData,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        #----------- End
        endEncTime = time.time() - startEncTime
        print("Encrypt Time: " + str(endEncTime))
        outFile = open("encrypted.mp4", "wb")
        outFile.write(encryptedData)
        outFile.close()

        startDecTime = time.time()
        #----------- Start 
        encryptedData = privKey.decrypt(
            encryptedData,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        #----------- End
        endDecTime = time.time() - startDecTime
        print("Decrypt Time: " + str(endDecTime))
        outFile = open("decrypted.mp4", "wb")
        outFile.write(encryptedData)
        outFile.close()
        print("")