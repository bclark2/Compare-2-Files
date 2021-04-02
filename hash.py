import hashlib


def read_file(file_path):
    with open(file_path, 'rb') as file:
        file = file.read()
    return file


file1 = read_file('path_to_your_first_file')
file1_hash = hashlib.sha256(file1)

file2 = read_file('path_to_your_second_file')
file2_hash = hashlib.sha256(file2)

print(file1_hash.hexdigest())
print(file2_hash.hexdigest())

if file1_hash.hexdigest() != file2_hash.hexdigest():
    print('Houston we have a problem: The files are different!')
