from Crypto.Util.number import long_to_bytes, inverse

# RSA parameters from output.txt
n = 984994081290620368062168960884976209711107645166770780785733
e = 65537
ct = 948553474947320504624302879933619818331484350431616834086273

# Step 1: Use the factors of n from FactorDB
p = 848445505077945374527983649411
q = 1160939713152385063689030212503

# Step 2: Calculate the private exponent d
phi_n = (p - 1) * (q - 1)
d = inverse(e, phi_n)

# Step 3: Decrypt the ciphertext
m = pow(ct, d, n)
plaintext = long_to_bytes(m)

# Print the plaintext (the cryptoflag)
print("Cryptoflag:", plaintext.decode())
