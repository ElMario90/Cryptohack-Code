def gcd(a, b):
    # Implementing Euclid's algorithm
    while b != 0:
        a, b = b, a % b
    return a

# Test the algorithm with a=12 and b=8 as an example
print("GCD of 12 and 8:", gcd(12, 8))

# Now calculate GCD for a=66528 and b=52920
a = 66528
b = 52920
print("GCD of 66528 and 52920:", gcd(a, b))
