import hashlib


password = "password1"
encoded_password = password.encode()
encrypted = hashlib.sha256(encoded_password).hexdigest()

# https://resources.nicowalters.repl.co/hash
