import requests
import json
from pwn import xor

BASE_URL = 'https://aes.cryptohack.org/lazy_cbc/'

def encrypt(plaintext_hex):
    response = requests.get(f'{BASE_URL}encrypt/{plaintext_hex}/')
    return response.json()['ciphertext']

def decrypt(ciphertext_hex):
    response = requests.get(f'{BASE_URL}receive/{ciphertext_hex}/')
    return response.json()['error'].split(': ')[1]

def get_flag(key_hex):
    response = requests.get(f'{BASE_URL}get_flag/{key_hex}/')
    return bytes.fromhex(response.json()['plaintext']).decode()

# Step 1: Encrypt a known plaintext
plaintext = b'a' * 48  # 3 blocks of 'a'
plaintext_hex = plaintext.hex()
ciphertext = encrypt(plaintext_hex)

# Step 2: Craft a malicious ciphertext
C0 = ciphertext[:32]
C1 = '0' * 32
C2 = C0
malicious_ciphertext = C0 + C1 + C2

# Step 3: Decrypt the malicious ciphertext
decrypted_plaintext_hex = decrypt(malicious_ciphertext)
decrypted_plaintext = bytes.fromhex(decrypted_plaintext_hex)

# Step 4: Recover the key
P0 = decrypted_plaintext[:16]
P2 = decrypted_plaintext[32:48]
key = xor(P0, P2).hex()

# Step 5: Retrieve the flag
flag = get_flag(key)
print(f'Flag: {flag}')
