import requests
from Crypto.Util.strxor import strxor

BASE_URL = "https://aes.cryptohack.org/flipping_cookie"

# Retrieve the encrypted cookie (contains both IV and encrypted data)
def get_cookie():
    response = requests.get(f"{BASE_URL}/get_cookie/")
    data = response.json()["cookie"]
    # Split IV and ciphertext
    iv = bytes.fromhex(data[:32])         # IV is the first 16 bytes (32 hex characters)
    cookie = bytes.fromhex(data[32:])     # The rest is the encrypted cookie
    return iv, cookie

# Send the modified cookie and IV to check if we're admin
def check_admin(modified_cookie, modified_iv):
    response = requests.get(f"{BASE_URL}/check_admin/{modified_cookie.hex()}/{modified_iv.hex()}/")
    try:
        data = response.json()
        if "flag" in data:
            return data["flag"]
        else:
            return data["error"]
    except ValueError:
        print("Failed to parse response.")
    return None

# Perform bit-flipping to turn "admin=False" to "admin=True" in the decrypted cookie
def flip_cookie_for_admin():
    iv, cookie = get_cookie()
    print("Original IV:", iv.hex())
    print("Original Cookie (Ciphertext):", cookie.hex())

    # Original and target plaintexts
    original_plaintext = b"admin=False;"
    target_plaintext = b"admin=True; "

    # Calculate XOR difference to change "False" to "True"
    xor_diff = strxor(original_plaintext, target_plaintext)

    # Modify the IV to introduce the required change in the first block of plaintext
    modified_iv = strxor(iv[:len(xor_diff)], xor_diff) + iv[len(xor_diff):]

    # Send modified IV with original ciphertext to attempt admin access
    result = check_admin(cookie, modified_iv)
    return result

# Run the attack
flag = flip_cookie_for_admin()
if "flag" in flag:
    print("Flag:", flag)
else:
    print("Error or not admin:", flag)
