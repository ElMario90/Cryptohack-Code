# Given string
label = "label"

# XOR each character with the integer 13
xor_result = ''.join([chr(ord(char) ^ 13) for char in label])

# Format the flag
flag = f"crypto{{{xor_result}}}"

# Print the result
print(flag)
