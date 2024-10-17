def is_quadratic_residue(x, p):
    """ Check if x is a quadratic residue modulo p. """
    for a in range(1, p):
        if (a * a) % p == x:
            return a
    return None

# Given integers and prime p
p = 29
ints = [14, 6, 11]

# Check each number in the list for quadratic residue
for x in ints:
    sqrt_res = is_quadratic_residue(x, p)
    if sqrt_res is not None:
        # If x is a quadratic residue, calculate the two square roots
        root1 = sqrt_res
        root2 = p - sqrt_res  # Because (-a)^2 = a^2 mod p
        print(f"Quadratic residue: {x}, Roots: {root1} and {root2}")
        print(f"Smaller root: {min(root1, root2)}")
