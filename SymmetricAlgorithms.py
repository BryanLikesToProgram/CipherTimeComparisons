import os
import cryptography
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.fernet import Fernet

### Error Handling ###
class SymmEncryptionError(Exception):
    ## Errors/Exceptions in cipher encryption ##
    pass
class SymmDecryptionError(Exception):
    ## Errors/Exceptions in cipher encryption ##
    pass

class SymmetricAlgorithms:
    def __init__(self, fileData) :
        self.fileData = fileData

    ### AES Cipher ###
    def AES_Encrypt(self, keySize, nonceSize):
        ## Init Cipher ##
        key = os.urandom(keySize) # average key length = 128 Bits
        init_val = os.urandom(nonceSize)
        cipher = Cipher(algorithms.AES(key), modes.CTR(init_val), backend=default_backend())  # Counter mode converts blocks to streams, no padding
        encryptor = cipher.encryptor()
        ## Encrypting Data ##
        encryptedData = encryptor.update(self.fileData) + encryptor.finalize()
        return encryptedData, cipher
    def AES_Decrypt(self, cipherObj) :
        decryptor = cipherObj.decryptor()
        ## Decrypting Data ##
        decryptedData = decryptor.update(self.fileData) + decryptor.finalize()
        return decryptedData

    ### FERNET CIPHER ###
    def FERNET_Encrypt(self):
        ## Init Cipher ##
        key = Fernet.generate_key()
        cipher = Fernet(key)
        ## Encrypting Data ##
        encryptedData = cipher.encrypt(self.fileData)
        return encryptedData, cipher
    def FERNET_Decrypt(self, cipherObj):
        ## Decrypting Data ##
        encryptedData = cipherObj.decrypt(self.fileData)
        return encryptedData
    
    ### XOR CIPHER ###
    def XOR_Encrypt(self):
        dataLength = len(self.fileData)
        ## Gen nonrepeating OTP the same size as data ##
        keySize = dataLength + 4 #Easy padding for bit length !/4 
        key = os.urandom(int(keySize))
        encryptedData = bytearray()
        ## Encrypting Data ##
        for i in range(0, (dataLength-1)):
            encryptedData.append( self.fileData[i] ^ key[i] )
        return encryptedData, key
    def XOR_Decrypt(self, cipherKey):
        decryptedData = bytearray()
        ## Decrypting Data ##
        for i in range(0, (len(self.fileData)-1)):
            decryptedData.append( self.fileData[i] ^ cipherKey[i] )
        return decryptedData
