from Crypto.PublicKey import RSA
from Crypto.IO import PKCS8
from cryptography import x509
from cryptography.hazmat.backends import default_backend

# Load the DER-encoded certificate
with open('/Users/georgemariusstanciu/Desktop/2048b-rsa-example-cert_3220bd92e30015fe4fbeb84a755e7ca5.der', 'rb') as der_file:
    der_data = der_file.read()

# Parse the DER certificate
cert = x509.load_der_x509_certificate(der_data, default_backend())

# Extract the public key (which is RSA in this case)
public_key = cert.public_key()

# Extract the modulus from the RSA public key
if isinstance(public_key, RSA.RsaKey):
    modulus = public_key.public_numbers().n
    print("Modulus:", modulus)
els