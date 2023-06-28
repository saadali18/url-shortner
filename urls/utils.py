import hashlib
import time

def generate_short_url(long_url):
    return hashlib.md5(long_url.encode()).hexdigest()
