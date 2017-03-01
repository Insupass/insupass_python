# Hash ascii string with SHA-512
# Return: hex string of hash result
# @tested python3.5

import hashlib


def hash_sha512(str_byte_message):
    return hashlib.sha512(str_byte_message).hexdigest().lower()