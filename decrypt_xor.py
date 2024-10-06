# Given hex-encoded ciphertext
ciphertext_hex = "0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104"

# Convert the hex string to bytes
ciphertext = bytes.fromhex(ciphertext_hex)

# We know the flag starts with 'crypto{', so we'll use it to guess part of the key
known_part = b"crypto{"

# XOR the known part with the corresponding part of the ciphertext to find the partial key
partial_key = bytes([c ^ k for c, k in zip(ciphertext[:len(known_part)], known_part)])

# Let's assume the full key is 'myXORkey' based on manual inspection and pattern.
full_key = b'myXORkey'

# Repeat the key to cover the entire ciphertext length
extended_key = (full_key * (len(ciphertext) // len(full_key)))[:len(ciphertext)]

# Now XOR the entire ciphertext with the full key to get the decrypted message
decrypted_message = bytes([c ^ k for c, k in zip(ciphertext, extended_key)])

# Convert the decrypted message to a string and print it
flag = decrypted_message.decode('utf-8')

print(flag)
