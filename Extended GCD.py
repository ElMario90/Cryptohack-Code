def extended_gcd(a, b):
    # Base case: when b is 0, we know gcd(a, 0) = a, and coefficients are u=1, v=0
    if b == 0:
        return a, 1, 0
    # Recursive case: apply Euclid's algorithm
    gcd, u1, v1 = extended_gcd(b, a % b)
    # Update coefficients u and v
    u = v1
    v = u1 - (a // b) * v1
    return gcd, u, v

# Given primes p and q
p = 26513
q = 32321

# Compute gcd and coefficients u, v
gcd_value, u, v = extended_gcd(p, q)

# Print results
print("GCD:", gcd_value)
print("u:", u)
print("v:", v)

# Since we need the lower of u and v as the flag
print("Flag (lower of u and v):", min(u, v))
