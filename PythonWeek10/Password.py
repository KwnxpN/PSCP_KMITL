"""KKK"""
import hashlib
def password(user_pass):
    """using SHA512"""
    print(hashlib.sha512(user_pass.encode('UTF-8')).hexdigest().upper())
password(str(input()))
