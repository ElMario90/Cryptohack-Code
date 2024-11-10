import requests
import hashlib
from Crypto.Cipher import AES

# Function to decrypt encrypted_data using a specified decryption_key
def decrypt(encrypted_data, decryption_key):
    cipher = AES.new(decryption_key, AES.MODE_ECB)
    decrypted_text = cipher.decrypt(bytes.fromhex(encrypted_data))
    return decrypted_text

# URL to get the encrypted flag data
endpoint_url = "https://aes.cryptohack.org/passwords_as_keys/encrypt_flag/"
response = requests.get(endpoint_url)
cipher_data = response.json()["ciphertext"]

# Load possible passwords from wordlist file
with open("words.txt", "r") as word_file:
    candidate_passwords = word_file.read().splitlines()

# Iterate over each potential password in the list
for password_guess in candidate_passwords:
    # Derive the AES key by hashing the password_guess using MD5
    derived_key = hashlib.md5(password_guess.encode()).digest()
    # Decrypt the cipher_data with the derived_key
    plaintext = decrypt(cipher_data, derived_key)
    # Check if the decrypted text contains the expected flag format
    if b"crypto{" in plaintext:
        print(f"Password Found: {password_guess}")
        print(f"Decrypted Flag: {plaintext.decode().strip()}")
        break
