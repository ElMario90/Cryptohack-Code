# Given integer array
ascii_values = [99, 114, 121, 112, 116, 111, 123, 65, 83, 67, 73, 73, 95, 112, 114, 49, 110, 116, 52, 98, 108, 51, 125]

# Convert ASCII values to characters
flag = ''.join([chr(i) for i in ascii_values])

# Print the flag
print(flag)
