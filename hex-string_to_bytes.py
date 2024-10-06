# Given hex-encoded ciphertext
ciphertext_hex = "73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"

# Convert the hex string to bytes
ciphertext = bytes.fromhex(ciphertext_hex)

# Try XOR with each possible byte (0-255) to find the key
for key in range(256):
    # XOR the ciphertext with the potential key
    decoded_message = ''.join([chr(b ^ key) for b in ciphertext])
    
    # Print the decoded message if it looks readable
    if decoded_message.isprintable() and "crypto" in decoded_message:
        flag = decoded_message
        break

print(flag)
