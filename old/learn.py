
import base64
import hashlib
from Crypto import Random
from Crypto.Cipher import AES

obj = AES.new('This is a key123', AES.MODE_CBC, 'This is an IV456')
message = "The answer is no"
ciphertext = obj.encrypt(message)
print(ciphertext)


encode= '�S��^)��11Y<��&GZ���ؓ�dT�%ZN�'
obj2 = AES.new('This is a key123', AES.MODE_ECB)
print(obj2.decrypt(encode))
