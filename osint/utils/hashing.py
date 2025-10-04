import hashlib

def quick_hash(data: str, algo="sha256"):
    h = hashlib.new(algo)
    h.update(data.encode())
    return h.hexdigest()