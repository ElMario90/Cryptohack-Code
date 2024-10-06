from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto import Random
from Crypto.Util.Padding import pad

# Function to create a 256-bit key from the password using SHA-256
def get_key(password):
    hasher = SHA256.new(password.encode('utf-8'))
    return hasher.digest()

# Function to encrypt the message using AES-256 with the specified padding
def aes_encrypt(message, password, padding_scheme):
    # Get 256-bit AES key from the password
    key = get_key(password)
    
    # AES requires a block size of 16 bytes (128 bits)
    block_size = AES.block_size
    
    # Generate a random IV (Initialization Vector)
    iv = Random.new().read(block_size)
    
    # Create AES cipher object
    cipher = AES.new(key, AES.MODE_CBC, iv)
    
    # Apply padding to the message based on the scheme
    if padding_scheme == "PKCS7":
        padded_message = pad(message.encode('utf-8'), block_size, style='pkcs7')
    elif padding_scheme == "ISO7816":
        padded_message = pad(message.encode('utf-8'), block_size, style='iso7816')
    elif padding_scheme == "ANSI X.923":
        padded_message = pad(message.encode('utf-8'), block_size, style='x923')
    
    # Encrypt the message and return IV + ciphertext
    encrypted_message = iv + cipher.encrypt(padded_message)
    
    # Return the first 6 hex characters of the encrypted message
    return encrypted_message.hex()[:6]

# Test the encryption with different padding methods
message = "kettle"
password = "oxtail"

padding_methods = ["PKCS7", "ISO7816", "ANSI X.923"]

for padding in padding_methods:
    cipher_text = aes_encrypt(message, password, padding)
    print(f"Padding: {padding}, Cipher: {cipher_text}")
