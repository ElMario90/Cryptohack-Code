# Given values from the problem:
e = 65537
p = 17
q = 23
message = 12

# Calculate the modulus N = p * q
N = p * q

# Encrypt the message using modular exponentiation
ciphertext = pow(message, e, N)

# Output the result
print(ciphertext)
