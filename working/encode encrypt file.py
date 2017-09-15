import binascii
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
bin_key=bin(int(binascii.hexlify(key),16))[2:] + str((32 - len('heeelooow'))*'00000000')
key_con = int(bin_key, 2)
key32 = binascii.unhexlify('%x' % key_con)

#key32 = "{: <32}".format(key).encode("utf-8")
#format32 = "{: <32}".format(key)
encoded_file = encoded_file.read()
#print (format32)
print("key: ", key32)
print (encoded_file)

enc_algo = AES.new(key32, AES.MODE_ECB)
print(enc_algo.decrypt(encoded_file))

decoded_file.write(enc_algo.decrypt(encoded_file))
decoded_file.close()
