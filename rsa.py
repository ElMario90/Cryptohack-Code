from sympy import factorint

# Given 150-bit number
number = 510143758735509025530880200653196460532653147

# Factorize the number using sympy's factorint function
factors = factorint(number)

# Extract the prime factors and find the smaller one
prime_factors = list(factors.keys())
smaller_prime = min(prime_factors)

# Print the smaller prime factor
print(smaller_prime)
