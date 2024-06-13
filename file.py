# Read large files line by line 
def read_large_file(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            yield line

# Store Encrypted File
def store_encrypted_file(file_path, encrypted_data,type):
    if type=="hex":
        with open(file_path, 'a') as file:
            file.write(encrypted_data)
            file.write("\n")
    else:
        with open(file_path, 'ab') as file:
            file.write(encrypted_data)
            file.write(b"\n")

# Read Encrypted File
def read_encrypted_file(file_path):
     with open(file_path, 'r') as file:
         for line in file:
             yield line

# Store Decrypted File
def store_decrypted_file(file_path, decrypted_data):
    with open(file_path, 'ab') as file:
        file.write(decrypted_data)

# Read Decrypted File
def read_decrypted_file(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            yield line

 