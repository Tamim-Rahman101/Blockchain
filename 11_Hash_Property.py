# 11. Write a Program in Python to Verify Hash Properties 

import hashlib

input1 = "Hello world!"
input2 = "Hello world."

def hash_string(input_string):
    md5_hash = hashlib.md5(input_string.encode()).hexdigest()
    sha1_hash = hashlib.sha1(input_string.encode()).hexdigest()
    sha256_hash = hashlib.sha256(input_string.encode()).hexdigest()
    return md5_hash, sha1_hash, sha256_hash

def print_hash(md5, sha1, sha256):
     print(f"MD5 hash value: {md5}")
     print(f"SHA1 hash value: {sha1}")
     print(f"SHA256 hash value: {sha256}")


# Deterministic (always gives same hash value for same input)
def verify_determinism():
    md5_1, sha1_1, sha256_1 = hash_string(input1)
    md5_2, sha1_2, sha256_2 = hash_string(input1)
    print_hash(md5_1, sha1_1, sha256_1)
    print_hash(md5_2, sha1_2, sha256_2)
    print(f"MD5 is deterministic : {md5_1 == md5_2}")
    print(f"SHA1 is deterministic : {sha1_1 == sha1_2}")
    print(f"SHA256 is deterministic : {sha256_1 == sha256_2}")


# Avalanche Effect (small change in input will change hash value significantly)
def verify_avalanche_effect():
    md5_1, sha1_1, sha256_1 = hash_string(input1)
    md5_2, sha1_2, sha256_2 = hash_string(input2)
    print_hash(md5_1, sha1_1, sha256_1)
    print_hash(md5_2, sha1_2, sha256_2)
    print(f"MD5 follows avalanche effect : {md5_1 != md5_2}")
    print(f"SHA1 follows avalanche effect : {sha1_1 != sha1_2}")
    print(f"SHA256 follows avalanche effect : {sha256_1 != sha256_2}")


# Fixed Length (specific hash function always gives a hash of specific length)
# MD5 length 32
# SHA1 length 40
# SHA256 length 64
def verify_length():
    md5_1, sha1_1, sha256_1 = hash_string(input1)
    print_hash(md5_1, sha1_1, sha256_1)
    print(f"MD5 hash length: {len(md5_1)}")
    print(f"SHA1 hash length: {len(sha1_1)}")
    print(f"SHA256 hash length: {len(sha256_1)}")

if __name__ == "__main__":
    verify_determinism()
    print("")
    verify_avalanche_effect()
    print("")
    verify_length()
