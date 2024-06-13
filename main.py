import algo
import file
import time

data_path = "./Data/data.txt"
encrypted_path = "./Encrypted/"
decrypted_path = "./Decrypted/"

encryption_times = []
decryption_times = []
key_sizes = [1024,2048,3072,4096]

for key_size in key_sizes:
    private_key = algo.private_key_gen(key_size)
    public_key = algo.public_key_gen(private_key)

    start_time = time.perf_counter()
    for message in file.read_large_file(data_path):
        message_bytes = message.encode('utf-8')
        encrypted_bytes, hex_encrypted = algo.encrpyt(message_bytes, public_key)
        file.store_encrypted_file(f"{encrypted_path}{key_size}_enc_hex.txt", hex_encrypted,type="hex")
        #file.store_encrypted_file(f"{encrypted_path}{key_size}enc.bin", encrypted_bytes,type="bin")
    encryption_times.append(time.perf_counter() - start_time)

    start_time = time.perf_counter()
    for hex_encrypted in file.read_large_file(f"{encrypted_path}{key_size}_enc_hex.txt"):
        encrypted_bytes = bytes.fromhex(hex_encrypted)
        decrypted_bytes = algo.decrypt(encrypted_bytes, private_key)
        decrypted_bytes = decrypted_bytes.encode('utf-8')
        file.store_decrypted_file(f"{decrypted_path}{key_size}dec.txt", decrypted_bytes)
    decryption_times.append(time.perf_counter() - start_time)


for key_size, encryption_time, decryption_time in zip(key_sizes, encryption_times, decryption_times):
    print(f"Key Size: {key_size} bits")
    print(f"  Encryption Time: {encryption_time:.6f} seconds")
    print(f"  Decryption Time: {decryption_time:.6f} seconds")
    print("-" * 30)

