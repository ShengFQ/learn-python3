import hashlib


def sha256_hash(file_path):
    with open(file_path, 'rb') as file:
        data = file.read()
        return hashlib.sha256(data).hexdigest()


print(sha256_hash('example.txt'));