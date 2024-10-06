# Given hex values
key1_hex = "a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313"
key2_key1_hex = "37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e"
key2_key3_hex = "c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1"
flag_xor_key1_key2_key3_hex = "04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf"

# Convert hex strings to bytes
key1 = bytes.fromhex(key1_hex)
key2_key1 = bytes.fromhex(key2_key1_hex)
key2_key3 = bytes.fromhex(key2_key3_hex)
flag_xor_key1_key2_key3 = bytes.fromhex(flag_xor_key1_key2_key3_hex)

# Use XOR to retrieve the values of KEY2 and KEY3
key2 = bytes([a ^ b for a, b in zip(key1, key2_key1)])
key3 = bytes([a ^ b for a, b in zip(key2, key2_key3)])

# Now XOR FLAG ^ KEY1 ^ KEY2 ^ KEY3 with KEY1, KEY2, and KEY3 to retrieve the flag
flag = bytes([a ^ b ^ c ^ d for a, b, c, d in zip(flag_xor_key1_key2_key3, key1, key2, key3)])

# Convert the flag from bytes to string and display it
print(flag.decode())
