from sys import argv
from hashlib import blake2b
from hmac import compare_digest

SECRET_KEY = b'pseudorandomly generated server secret key'
AUTH_SIZE = 16


def sign(cookie):
    h = blake2b(digest_size=AUTH_SIZE, key=SECRET_KEY)
    h.update(cookie)
    return h.hexdigest().encode('utf-8')


def verify(cookie, sig):
    good_sig = sign(cookie)
    return compare_digest(good_sig, sig)


cookie = str.encode(argv[1])
sig = sign(cookie)
print("{0},{1}".format(cookie.decode('utf-8'), sig))
if verify(cookie, sig):
    print('OK')

