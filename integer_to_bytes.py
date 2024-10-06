# Importing the required function from PyCryptodome
from Crypto.Util.number import long_to_bytes

# Given large integer
large_integer = 11515195063862318899931685488813747395775516287289682636499965282714637259206269

# Convert the large integer to bytes
message_bytes = long_to_bytes(large_integer)

# Convert bytes to string (UTF-8 encoding)
message = message_bytes.decode('utf-8')

# Print the message
print(message)

