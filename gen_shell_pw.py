#!/usr/bin/env python3
from typing import Tuple
import os
import hashlib
import hmac


def hash_new_password(password: str) -> Tuple[bytes, bytes]:
    """
    Hash the provided password with a randomly-generated salt and return the
    salt and hash to store in the database.
    """
    salt = os.urandom(16)
    pw_hash = hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100000)
    return salt, pw_hash


def is_correct_password(salt: bytes, pw_hash: bytes, password: str) -> bool:
    """
    Given a previously-stored salt and hash, and a password provided by a user
    trying to log in, check whether the password is correct.
    """
    return hmac.compare_digest(
        pw_hash,
        hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100000)
    )

# hash a password
pw = input('Enter a password: ')
pw2 = input('Confirm Password: ')
if pw != pw2:
    print('Passwords do not match!. Quitting.')
    exit(1)

salt, pw_hash = hash_new_password(pw)
salt = salt.hex()
pw_hash = pw_hash.hex()

if is_correct_password(bytes.fromhex(salt), bytes.fromhex(pw_hash), pw):
    print('Test Succeeded!')
    print("Salt: %s" % salt)
    print("Hash: %s" % pw_hash)
