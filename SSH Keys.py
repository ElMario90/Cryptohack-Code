import base64
import struct

def extract_modulus_from_ssh_pubkey(ssh_pubkey):
    # Split the key into parts (we're interested in the second part, which is base64-encoded)
    key_parts = ssh_pubkey.split()
    key_type = key_parts[0]  # This should be 'ssh-rsa'
    key_data_base64 = key_parts[1]  # The actual base64-encoded data

    # Decode the base64 part
    key_data = base64.b64decode(key_data_base64)

    # Now we need to parse the structure of the decoded data
    # The structure starts with a 4-byte length field for the 'ssh-rsa' type
    # followed by the 'ssh-rsa' string, then exponent, and modulus.
    
    # Helper function to read the next length-prefixed field
    def read_next_field(data):
        field_len = struct.unpack(">I", data[:4])[0]  # ">I" reads a big-endian unsigned int (4 bytes)
        return data[4:4+field_len], data[4+field_len:]

    # Read the first field (the 'ssh-rsa' type)
    ssh_rsa_type, key_data = read_next_field(key_data)

    # Read the exponent (e)
    exponent, key_data = read_next_field(key_data)

    # Read the modulus (n)
    modulus, _ = read_next_field(key_data)

    # Convert the modulus to an integer
    modulus_int = int.from_bytes(modulus, byteorder='big')

    return modulus_int

# Load the SSH public key from a file
with open("bruce_rsa_6e7ecd53b443a97013397b1a1ea30e14.pub", "r") as f:
    ssh_public_key = f.read().strip()

# Extract modulus
modulus = extract_modulus_from_ssh_pubkey(ssh_public_key)

# Output the modulus in decimal
print("Modulus (n) as a decimal integer:", modulus)
