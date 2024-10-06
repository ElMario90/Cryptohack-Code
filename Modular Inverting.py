# Function to find the modular inverse using Fermat's Little Theorem
def mod_inverse(g, p):
    # Fermat's Little Theorem: g^(p-2) mod p gives the inverse
    return pow(g, p - 2, p)

# Given values
g = 3
p = 13

# Calculate the inverse
inverse = mod_inverse(g, p)

# Output the result
print(f"The inverse of {g} modulo {p} is: {inverse}")
