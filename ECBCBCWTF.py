import requests
from Crypto.Util.strxor import strxor
import json
import base64

BASE_URL = "https://aes.cryptohack.org/ecbcbcwtf"

# Function to get ciphertext encrypted in CBC mode
def get_encrypted_flag():
    response = requests.get(f"{BASE_URL}/encrypt_flag/")
    data = response.json()
    return bytes.fromhex(data['ciphertext'])

# Function to decrypt in ECB mode
def ecb_decrypt(ciphertext):
    hex_cipher = ciphertext.hex()
    response = requests.get(f"{BASE_URL}/decrypt/{hex_cipher}/")
    data = response.json()
    return bytes.fromhex(data['plaintext'])

# Main function to get the flag
def get_flag():
    ciphertext = get_encrypted_flag()
    iv = ciphertext[:16]  # First block (IV) for CBC mode
    encrypted_flag = ciphertext[16:]  # Remaining part is the encrypted flag in CBC mode
    
    # ECB Decrypt each 16-byte block of the encrypted flag
    decrypted_blocks = []
    for i in range(0, len(encrypted_flag), 16):
        block = encrypted_flag[i:i+16]
        decrypted_block = ecb_decrypt(block)
        decrypted_blocks.append(decrypted_block)
    
    # XOR with the previous ciphertext block (starting with IV) to recover plaintext
    plaintext = b""
    previous_block = iv
    for decrypted_block in decrypted_blocks:
        plaintext_block = strxor(previous_block, decrypted_block)
        plaintext += plaintext_block
        previous_block = encrypted_flag[:16]
    
    return plaintext.decode()

# Fetch and print the flag
print(get_flag())
