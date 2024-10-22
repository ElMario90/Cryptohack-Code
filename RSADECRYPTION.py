# Given values from the problem
N = 882564595536224140639625987659416029426239230804614613279163
e = 65537
c = 77578995801157823671636298847186723593814843845525223303932

# The private key (calculated from the previous problem)
d = 121832886702415731577073962957377780195510499965398469843281

# Decrypt the ciphertext using modular exponentiation
message = pow(c, d, N)

# Output the decrypted message
print(message)
