from sympy import isprime

# Given sequence of integers
sequence = [588, 665, 216, 113, 642, 4, 836, 114, 851, 492, 819, 237]

def find_p_and_x(sequence):
    # Loop over all three-digit primes for p
    for p in range(100, 1000):
        if not isprime(p):
            continue
        
        # Try every x from 2 to p-1
        for x in range(2, p):
            valid = True
            # Start with the first element and apply powers of x to match the sequence
            current = sequence[0]
            
            for i in range(1, len(sequence)):
                # Calculate the next power of x modulo p
                current = (current * x) % p
                # Check if it matches the sequence
                if current != sequence[i]:
                    valid = False
                    break
            
            # If we found a valid p and x, return them
            if valid:
                return p, x
    
    return None, None

# Run the function to find p and x
p, x = find_p_and_x(sequence)

# Generate the flag format if p and x are found
if p and x:
    flag = f"crypto{{p={p},x={x}}}"
    print("Flag:", flag)
else:
    print("No solution found.")
