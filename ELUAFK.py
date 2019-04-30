'''
Encryption center do NOT touch!
'''

import base64
import os
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

#can change the password to your liking
password_provided = 'default'
kpassword = password_provided.encode()

#can change the salt to your liking
salt = b'H&\xb6\n\xe6@\xdf\x13\x88\x98 Z\xf0\xea,\xca\x05\xd7\x99\x105\xa8\xa2{\xa9F\xe0\x91\x89c)\xf8%@]"u<\xe03|\xe2\re]\'\xb7\x89O2\xf9\x0bY\xf5\xb6<\x80z\\bM\x8dDx'
kdf = PBKDF2HMAC(
    algorithm = hashes.SHA256,
    length = 32,
    salt = salt,
    iterations = 100000,
    backend = default_backend()
)
key = base64.urlsafe_b64encode(kdf.derive(kpassword))
