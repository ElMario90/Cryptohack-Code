import requests

# Base URL for the challenge API
BASE_URL = "https://aes.cryptohack.org/block_cipher_starter"

# Function to interact with the encrypt_flag endpoint
def encrypt_flag():
    url = f"{BASE_URL}/encrypt_flag/"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()["ciphertext"]
    else:
        raise Exception("Failed to encrypt flag.")

# Function to interact with the decrypt endpoint
def decrypt(ciphertext):
    url = f"{BASE_URL}/decrypt/{ciphertext}/"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()["plaintext"]
    else:
        raise Exception("Failed to decrypt ciphertext.")

# Main function to solve the challenge
def solve_challenge():
    # Step 1: Encrypt the flag and get the ciphertext
    print("Encrypting the flag...")
    ciphertext = encrypt_flag()
    print(f"Ciphertext: {ciphertext}")

    # Step 2: Decrypt the ciphertext to retrieve the flag
    print("Decrypting the ciphertext...")
    plaintext = decrypt(ciphertext)
    print(f"Decrypted plaintext (hex): {plaintext}")

# Run the challenge solver
if __name__ == "__main__":
    solve_challenge()
