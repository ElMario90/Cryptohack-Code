from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography import x509

# Load the DER file
with open("2048b-rsa-example-cert.der", "rb") as f:
    der_data = f.read()

# Parse the DER-encoded certificate
certificate = x509.load_der_x509_certificate(der_data, default_backend())

# Extract the public key from the certificate
public_key = certificate.public_key()

# Ensure it is an RSA key and extract the modulus
if isinstance(public_key, rsa.RSAPublicKey):
    modulus = public_key.public_numbers().n
    print("Modulus (decimal):", modulus)
else:
    print("The public key is not RSA.")
