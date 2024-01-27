import os
import hashlib

def find_duplicate_files(directory):
    duplicates = {}
    for root, dirs, files in os.walk(directory):
        for filename in files:
            file_path = os.path.join(root, filename)
            file_hash = hashfile(file_path)
            if file_hash in duplicates:
                duplicates[file_hash].append(file_path)
            else:
                duplicates[file_hash] = [file_path]
    return duplicates

def hashfile(path, blocksize=65536):
    hasher = hashlib.md5()
    with open(path, 'rb') as file:
        buf = file.read(blocksize)
        while len(buf) > 0:
            hasher.update(buf)
            buf = file.read(blocksize)
    return hasher.hexdigest()

def remove_duplicate_files(duplicate_dict):
    for key in duplicate_dict:
        if len(duplicate_dict[key]) > 1:
            # Keep the first file and remove the rest
            for file_to_remove in duplicate_dict[key][1:]:
                os.remove(file_to_remove)

#As mentioned in ReadMe file: hard-code the directory path to variable named:directory_path over which you likely to remove duplicate entries of file
directory_path = "/home/box/ipython"
duplicates = find_duplicate_files(directory_path)
remove_duplicate_files(duplicates)


