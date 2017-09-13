from Crypto.Cipher import AES
import base64


cipher = AES.new('secret_key',AES.MODE_ECB) # never use ECB in strong systems obviously
encoded = base64.b64encode(cipher.encrypt(msg_text))
# ...
decoded = cipher.decrypt(baes64.b64decode(msg_text))