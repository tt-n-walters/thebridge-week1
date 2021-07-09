import hashlib


file = open("C:/Users/Alumno.NOT06-02-I5S17G.000/Desktop/rockyou.txt", encoding="latin-1")

for i, line in enumerate(file):
    
    password = line.strip()
    encoded = password.encode()
    encrypted = hashlib.md5(encoded).hexdigest()

    if i % 5000 == 0:
        print(" ", i, "Encrypted password", repr(password), encrypted, " " * 10, end="\r")

    if encrypted == "89ae6fd2a5185085e35b6e755227f29b":
        print(" ", i, "Encrypted password", repr(password), encrypted, " " * 10, end="\r")
        print("\nFound match.")
        break