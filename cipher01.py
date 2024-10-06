from Crypto.Cipher import AES
import hashlib
import sys
import binascii
import Padding

def encrypt(plaintext, key, mode):
    encobj = AES.new(key, mode)
    return encobj.encrypt(plaintext)

def decrypt(ciphertext, key, mode):
    encobj = AES.new(key, mode)
    return encobj.decrypt(ciphertext)

if len(sys.argv) != 3:
    print("Usage: python cipher01.py <plaintext> <password>")
    sys.exit()

# Read command-line arguments
plaintext_input = sys.argv[1]
password_input = sys.argv[2]

# Generate a key from the password using SHA-256
key = hashlib.sha256(password_input.encode('utf-8')).digest()

# Pad the plaintext
plaintext = Padding.appendPadding(plaintext_input, blocksize=Padding.AES_blocksize, mode='CMS')
print("After padding (CMS): " + binascii.hexlify(bytearray(plaintext)).decode('utf-8'))

# Encrypt the plaintext using AES in ECB mode
ciphertext = encrypt(plaintext, key, AES.MODE_ECB)
print("Cipher (ECB): " + binascii.hexlify(bytearray(ciphertext)).decode('utf-8'))

# Decrypt the ciphertext
decrypted_text = decrypt(ciphertext, key, AES.MODE_ECB)
decrypted_text = Padding.removePadding(decrypted_text, mode='CMS')
print("Decrypted text: " + decrypted_text.decode('utf-8'))
