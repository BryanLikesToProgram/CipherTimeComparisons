from SymmetricAlgorithms import AES
from SymmetricAlgorithms import FERNET

AES("test.mp4").counterMode(32, 16)
FERNET("test.mp4").singleFernet()
