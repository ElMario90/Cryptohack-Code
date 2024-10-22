from Crypto.Util.number import inverse

# Given values for p, q, and e
p = 857504083339712752489993810777
q = 1029224947942998075080348647219
e = 65537

# Calculate Euler's totient φ(N) = (p - 1) * (q - 1)
phi_N = (p - 1) * (q - 1)

# Calculate the private key d, which is the modular inverse of e modulo φ(N)
d = inverse(e, phi_N)

# Output the private key d
print(d)
