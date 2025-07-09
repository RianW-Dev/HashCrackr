import hashlib
salt = "1234"
senha = "banana"
print(hashlib.sha256((salt + senha).encode()).hexdigest())
