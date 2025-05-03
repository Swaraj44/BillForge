import hashlib

# Input string
input_string = "Hello, World!"

# Create a hash object
hash_object = hashlib.sha256(input_string.encode())

# Get the hexadecimal representation of the hash
hash_value = hash_object.hexdigest()

print("Hash value:", hash_value)
