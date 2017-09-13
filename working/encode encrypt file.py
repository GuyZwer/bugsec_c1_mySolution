
import base64
import hashlib
from Crypto import Random
from Crypto.Cipher import AES
'''
cipher = AES.new(self.key, AES.MODE_EBC)
return self._unpad(cipher.decrypt(enc[AES.block_size:])).decode('utf-8')
'''

encoded_file = open(raw_input('Please type the encryptrd file name: '), 'r')
decoded_file = open(raw_input('Please type the name for output file: '), 'w')
key = raw_input('Please type the key: ')
key32 = "{: <32}".format(key).encode("utf-8")
encoded_file = encoded_file.read()
print("key: ", key32)
print (encoded_file)

enc_algo = AES.new(key32, AES.MODE_ECB)
print(enc_algo.decrypt(encoded_file))

decoded_file.write(enc_algo.decrypt(encoded_file))
decoded_file.close()
