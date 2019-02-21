import sys
import time
from SymmetricAlgorithms import SymmetricAlgorithms
from ASymmetricAlgorithms import ASymmetricAlgorithms
### Error Handling ###
class ArgsError(Exception):
    ## Errors/Exceptions in script calls ##
    pass
class FileError(Exception):
    ## Errors/Exceptions in file IO ##
    pass
class CipherError(Exception):
    ## Errors/Exceptions from Cipher-Test implimentation ##
    pass

### File Handling ###
def fileStream_In(fileName): 
    try:
        inFile = open(fileName, 'rb')
        fileData = inFile.read()
        inFile.close()
        return fileData
    except FileError:
        print('Error handling input file')
        raise
def fileStream_Out(fileData, fileName):
    try:
        outFile = open(fileName, "wb")
        outFile.write(fileData)
        outFile.close()
    except FileError:
        print('Error handling input file')
        raise

### Cipher Time Evaulation ###
def cipherEncrypt( filename, data, cipherFunct, * args):
    try:
        arguments = []
        for x in args:
            arguments.append(x) ## Setup variable args values foreach funct call
        ## Start Timer ##
        startTime = time.time()
        ## Encrypt Data ##
        returnedData = cipherFunct(*arguments)
        encryptedData = returnedData[0]
        cipherKey = returnedData[1]
        elapsedTime = (time.time() - startTime)
        print("Encrypt Time Elapsed: "+str(elapsedTime))
        ## Write To File ##
        fileStream_Out(encryptedData, filename)
        return encryptedData, cipherKey
    except CipherError: 
        print('Error handling cipher timing')
        raise 
def cipherDecrypt(infilename, cipherFunct, * args):
    try:
        arguments = []
        for x in args:
            arguments.append(x) ## Setup variable args values foreach funct call
        ## Start Timer ##
        startTime = time.time()
        ## Decrypt Data ##
        decryptedData = cipherFunct(*arguments)
        elapsedTime = (time.time() - startTime)
        print("Decrypt Time Elapsed: "+str(elapsedTime))
        ## Write To File ##
        fileStream_Out(decryptedData, "Decrypted.mp4")
    except CipherError: 
        print('Error handling cipher timing')
        raise 
### When running as script ###
if __name__ == "__main__":
    cipherArray = ["AES", "FERNET", "XOR", "PRESENT80"]
    try : 
        fileName = "test.mp4" # default file
        numArgs = len(sys.argv)
        if numArgs == 1 :
            ## Demo ##
            print ("Running Demo...")
            fileData = fileStream_In(fileName)
            encryptedFileName = "Encrypted.mp4"
            decryptedFileName = "Decrypted.mp4"
            print("------Symmetric Cryptographic Algorithms------")
            ## AES ##
            print("AES")
            returnData = cipherEncrypt(
                encryptedFileName, 
                fileData, 
                SymmetricAlgorithms.AES_Encrypt, 
                SymmetricAlgorithms(fileData), 32, 16
            ) 
            encryptedData = returnData[0]
            cipherKey = returnData[1]
            cipherDecrypt(
                decryptedFileName, 
                SymmetricAlgorithms.AES_Decrypt, 
                SymmetricAlgorithms(encryptedData), cipherKey
            )
            ## FERNET ##
            print("FERNET")
            returnData = cipherEncrypt(
                encryptedFileName, 
                fileData, 
                SymmetricAlgorithms.FERNET_Encrypt, 
                SymmetricAlgorithms(fileData)
            ) 
            encryptedData = returnData[0]
            cipherKey = returnData[1]
            cipherDecrypt(
                decryptedFileName, 
                SymmetricAlgorithms.FERNET_Decrypt, 
                SymmetricAlgorithms(encryptedData), cipherKey
            )
            ## XOR ##
            print("XOR")
            returnData = cipherEncrypt(
                encryptedFileName, 
                fileData, 
                SymmetricAlgorithms.XOR_Encrypt, SymmetricAlgorithms(fileData)
            ) 
            encryptedData = returnData[0]
            cipherKey = returnData[1]
            cipherDecrypt(
                decryptedFileName, 
                SymmetricAlgorithms.XOR_Decrypt, 
                SymmetricAlgorithms(encryptedData), cipherKey
            )
            ## PRESENT80 ##
            print("PRESENT-80")
            print("TODO")
            print("------Asymmetric Cryptographic Algorithms------")
            ## Elliptic Curve ##
            print("ELLIPTIC CURVE")
            returnData = cipherEncrypt(
                encryptedFileName, # /signedFileName
                fileData, 
                ASymmetricAlgorithms.ELLIPTICCURVE_Sign, 
                ASymmetricAlgorithms(fileData)
            ) 
            signature = returnData[0]
            publicKey = returnData[1]
            verification = ASymmetricAlgorithms.ELLIPTICCURVE_Verify(
                ASymmetricAlgorithms(fileData), signature, publicKey
            )
            print("Signature Anomalies: "+str(verification))
            ## RSA ##
            print("RSA")
            returnData = cipherEncrypt(
                encryptedFileName, 
                fileData, 
                ASymmetricAlgorithms.RSA_Encrypt, ASymmetricAlgorithms(fileData)
            ) 
            encryptedData = returnData[0]
            privateKey = returnData[1]
            cipherDecrypt(
                decryptedFileName, 
                ASymmetricAlgorithms.RSA_Decrypt, 
                ASymmetricAlgorithms(encryptedData), privateKey
            )
            
        elif numArgs == 2 :
            ## Request Cipher ##
            fileName = sys.argv[1]
            print(fileName)
            print(" Which Cipher?", '\n',
            "(1) AES", '\n',
            "(2) FERNET", '\n',
            "(3) XOR", '\n',
            "(4) PRESENT-80", '\n',
            "(5) Elliptic Curve", '\n',
            "(6) RSA")
            cipherChoice = input()
            fileData = fileStream_In(fileName)
            # Authors note: RIP switch statements.... #
            if cipherChoice == 1:
                ## AES ##
                print("AES")
                returnData = cipherEncrypt(
                    encryptedFileName, 
                    fileData, 
                    SymmetricAlgorithms.AES_Encrypt, 
                    SymmetricAlgorithms(fileData), 32, 16
                ) 
                encryptedData = returnData[0]
                cipherKey = returnData[1]
                cipherDecrypt(
                    decryptedFileName, 
                    SymmetricAlgorithms.AES_Decrypt, 
                    SymmetricAlgorithms(encryptedData), cipherKey
                )
            elif cipherChoice == 2:
                ## FERNET ##
                print("FERNET")
                returnData = cipherEncrypt(
                    encryptedFileName, 
                    fileData, 
                    SymmetricAlgorithms.FERNET_Encrypt, 
                    SymmetricAlgorithms(fileData)
                ) 
                encryptedData = returnData[0]
                cipherKey = returnData[1]
                cipherDecrypt(
                    decryptedFileName, 
                    SymmetricAlgorithms.FERNET_Decrypt, 
                    SymmetricAlgorithms(encryptedData), cipherKey
                )
            elif cipherChoice == 3:
                ## XOR ##
                print("XOR")
                returnData = cipherEncrypt(
                    encryptedFileName, 
                    fileData, 
                    SymmetricAlgorithms.XOR_Encrypt, SymmetricAlgorithms(fileData)
                ) 
                encryptedData = returnData[0]
                cipherKey = returnData[1]
                cipherDecrypt(
                    decryptedFileName, 
                    SymmetricAlgorithms.XOR_Decrypt, 
                    SymmetricAlgorithms(encryptedData), cipherKey
                )
            elif cipherChoice == 4:
                ## PRESENT80 ##
                print("PRESENT-80")
                print("TODO")
            elif cipherChoice == 5:
                ## Elliptic Curve ##
                print("ELLIPTIC CURVE")
                returnData = cipherEncrypt(
                    encryptedFileName, # /signedFileName
                    fileData, 
                    ASymmetricAlgorithms.ELLIPTICCURVE_Sign, 
                    ASymmetricAlgorithms(fileData)
                ) 
                signature = returnData[0]
                publicKey = returnData[1]
                verification = ASymmetricAlgorithms.ELLIPTICCURVE_Verify(
                    ASymmetricAlgorithms(fileData), signature, publicKey
                )
                print("Signature Anomalies: "+str(verification))
            elif cipherChoice == 6:
                print("RSA")
                returnData = cipherEncrypt(
                    encryptedFileName, 
                    fileData, 
                    ASymmetricAlgorithms.RSA_Encrypt, ASymmetricAlgorithms(fileData)
                ) 
                encryptedData = returnData[0]
                privateKey = returnData[1]
                cipherDecrypt(
                    decryptedFileName, 
                    ASymmetricAlgorithms.RSA_Decrypt, 
                    ASymmetricAlgorithms(encryptedData), privateKey
                )
        elif numArgs == 3 :
            ## Run Cipher on Filename ##
            print("Cipher")
            fileName = sys.argv[1]
            fileData = fileStream_In(fileName)
            print("TODO")
        else:
            raise ArgsError('More than 3 call arguments')
    except ArgsError:
        print('Unexpected ArgumentError: ')
        raise
