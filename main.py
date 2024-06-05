import algo
import file

data_path = "./Data/data.txt"
encrypted_path = "./Encrypted/encrypted.txt"
decrypted_path = "./Decrypted/decrypted.txt"

# Generate RSA Keys
private_key = algo.private_key_gen()
public_key = algo.public_key_gen(private_key)

# Encrypt Data and Decrypt Data
for message in file.read_large_file(data_path):
    message_bytes = message.encode('utf-8')
    encrypted,hex_encrypted = algo.encrpyt(message_bytes, public_key)
    file.store_encrypted_file(encrypted_path, hex_encrypted)
    decrypted = algo.decrypt(encrypted, private_key)
    decrypted_bytes = decrypted.encode('utf-8')
    file.store_decrypted_file(decrypted_path, decrypted_bytes)




