import time
import os
import io
import cryptography
import sys
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.fernet import Fernet

class AES:
    def __init__(self, filename) :
        self.fileName = filename
        print("Cipher: AES")

    def counterMode(self, keySize, nonceSize) :
        print("Mode: Counter")
        inFile = open(self.fileName, 'rb')
        fileData = inFile.read()
        inFile.close()

        key = os.urandom(keySize) # average key length = 128 Bits
        init_val = os.urandom(nonceSize)

        cipher = Cipher(algorithms.AES(key), modes.CTR(init_val), backend=default_backend())  # Counter mode converts blocks to streams, no padding 
        encryptor = cipher.encryptor()
        startEncTime = time.time()
        #----------- Start
        encryptedData = encryptor.update(fileData) + encryptor.finalize()
        #----------- End
        endEncTime = time.time() - startEncTime
        print("Encrypt Time: " + str(endEncTime))
        outFile = open("encrypted.mp4", "wb")
        outFile.write(encryptedData)
        outFile.close()

        decryptor = cipher.decryptor()
        startDecTime = time.time()
        #----------- Start 
        encryptedData = decryptor.update(encryptedData) + decryptor.finalize()
        #----------- End
        endDecTime = time.time() - startDecTime
        print("Decrypt Time: " + str(endDecTime))
        outFile = open("decrypted.mp4", "wb")
        outFile.write(encryptedData)
        outFile.close()
        print("")

class FERNET:

    def __init__(self, filename) :
        self.fileName = filename
        print("Cipher: Fernet")

    def singleFernet(self) :
        print("Mode: Single")
        inFile = open(self.fileName, 'rb')
        fileData = inFile.read()
        inFile.close()

        key = Fernet.generate_key()
        cipher = Fernet(key)
        startEncTime = time.time()
        #----------- Start
        encryptedData = cipher.encrypt(fileData)
        #----------- End
        endEncTime = time.time() - startEncTime
        print("Encrypt Time: " + str(endEncTime))
        outFile = open("encrypted.mp4", "wb")
        outFile.write(encryptedData)
        outFile.close()
        
        startDecTime = time.time()
        #----------- Start 
        encryptedData = cipher.decrypt(encryptedData)
        #----------- End
        endDecTime = time.time() - startDecTime
        print("Decrypt Time: " + str(endDecTime))
        outFile = open("decrypted.mp4", "wb")
        outFile.write(encryptedData)
        outFile.close()
        print("")

    def multiFernet(self) :
        print( "Not yet implimented" )

class XOR:
        def __init__(self, filename) : 
            self.filename = filename
            print("Cipher: XOR")
                                                                                         
        def simpleXor(self): 
            print("Mode: No OTP")
            inFile = open(self.filename, 'rb')
            fileData = inFile.read()
            inFile.close()
        
            dataLength = len(fileData)
            keySize = dataLength + 4 #Easy padding for bit length !/4 
            key = os.urandom(int(keySize))

            encryptedData = bytearray()
            ## Encrypt using XOR ##
            startEncTime = time.time()
            #----------- Start
            for i in range(0, (dataLength-1)):
                encryptedData.append( fileData[i] ^ key[i] )
            #----------- End
            endEncTime = time.time() - startEncTime
            print("Encrypt Time: " + str(endEncTime))
            outFile = open("encrypted.mp4", "wb")
            outFile.write(encryptedData)
            outFile.close()

            decryptedData = bytearray()
            ## Decrypt using XOR ##
            startDecTime = time.time()
            #----------- Start
            for i in range(0, (dataLength-1)):
                decryptedData.append( encryptedData[i] ^ key[i] )
            #----------- End
            endDecTime = time.time() - startDecTime
            print("Decrypt Time: " + str(endDecTime))
            outFile = open("decrypted.mp4", "wb")
            outFile.write(decryptedData)
            outFile.close()
            
