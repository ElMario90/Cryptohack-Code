# Given prime p = 17 for the first few calculations
p = 17

# 3^17 mod 17
result1 = pow(3, 17, p)
print("3^17 mod 17:", result1)

# 5^17 mod 17
result2 = pow(5, 17, p)
print("5^17 mod 17:", result2)

# 7^16 mod 17 (using Fermat's Little Theorem)
result3 = pow(7, 16, p)
print("7^16 mod 17:", result3)

# Now take the large prime p = 65537 and calculate the next one
p_large = 65537
base = 273246787654
exp = 65536

# Using pow for large calculations: 273246787654^65536 mod 65537
result4 = pow(base, exp, p_large)
print("273246787654^65536 mod 65537:", result4)
