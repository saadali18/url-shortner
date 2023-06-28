import hashlib
import time

def generate_short_url(long_url):
    return hashlib.md5(long_url.encode()).hexdigest()

def generate_id():
    return int(time.time()) * 1000

def decimal_to_base62():
    decimal_num = generate_id()
    characters = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    base = len(characters)
    result = []

    while decimal_num > 0:
        remainder = decimal_num % base
        result.append(characters[remainder])
        decimal_num //= base

    # Reverse the result and convert it to a string
    result.reverse()
    base62_str = ''.join(result)

    return base62_str
