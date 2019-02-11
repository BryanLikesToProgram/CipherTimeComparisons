from SymmetricAlgorithms import AES
from SymmetricAlgorithms import FERNET
from SymmetricAlgorithms import XOR
from ASymmetricAlgorithms import ELLIPTICCURVE
from ASymmetricAlgorithms import RSA

AES("test.mp4").counterMode(32, 16)
FERNET("test.mp4").singleFernet()
ELLIPTICCURVE("test.mp4").ThreeEightFourROne()
#RSA("test.mp4").PemSerialized() Not applicable for larger files
XOR("test.mp4").simpleXor()