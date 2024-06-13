from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes, serialization

# Private Key Generation
def private_key_gen(key_size1):
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=key_size1)
    return private_key

def public_key_gen(private_key):
    public_key = private_key.public_key()
    return public_key

    
# hex_ciphertext
def hex_ciphertext(ciphertext):
    hex_ciphertext = ciphertext.hex()
    return hex_ciphertext

# encryption
def encrpyt(message,public_key):
    ciphertext = public_key.encrypt(
        message,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )   
    )
    hex = hex_ciphertext(ciphertext)
    return ciphertext,hex

# decryption
def decrypt(ciphertext, private_key):
    plaintext = private_key.decrypt(
        ciphertext,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    plaintext = plaintext.decode("utf-8")
    return plaintext



