from functools import reduce

# Extended Euclidean Algorithm to find the modular inverse
def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

def mod_inverse(a, m):
    gcd, x, y = extended_gcd(a, m)
    if gcd != 1:
        raise Exception('Modular inverse does not exist')
    else:
        return x % m

def chinese_remainder_theorem(a, n):
    # Step 1: Calculate the product N of all n_i
    N = reduce(lambda x, y: x * y, n)
    
    # Step 2: Calculate the result x using the formula
    x = 0
    for a_i, n_i in zip(a, n):
        N_i = N // n_i
        inv_N_i = mod_inverse(N_i, n_i)
        x += a_i * N_i * inv_N_i
    
    return x % N

# Given system of congruences
a = [2, 3, 5]  # The a_i values
n = [5, 11, 17]  # The n_i values (moduli)

# Solve using Chinese Remainder Theorem
result = chinese_remainder_theorem(a, n)
print(f"The solution x ≡ {result} mod 935")
