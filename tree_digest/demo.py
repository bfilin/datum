#!/usr/bin/env python3
from hashlib import sha1 
from binascii import hexlify   

def header(s): 
    print("\033[91m{}\033[00m" .format(s))

def basic_demo():
    h = sha1()
    i = sha1()
    j = sha1()

    header('\nThe examples below use:')
    print(' 1) sha1 hash object from hashlib module')
    print('         such that .update() method updates the current digest with an additional string')
    print('         such that .digest() -- return the current digest value')
    print(' 2) hexlify from binascii module to generate hexadecimal representation of digest encoded as bytes')
    print()

    my_string = 'hello world'
    my_file_path_and_name = 'dir_a/dir_b2/file_b2.txt'

    # example 1
    header('[ example 1: get hash of a string: ' + my_string + ' ]')
    h.update( my_string.encode() )     
    print('Input: \'' + my_string + '\' encoded as bytes')
    print('Digest Output: ',h.digest())
    print('Digest as hex Output: ', hexlify( h.digest()) ) 
    # Note: equivalent Linux terminal command: echo -n 'hello world' | sha1sum')
    print(end='\n\n')
    # end of example 1



    # example 2 
    header('[ example 2: get hash of content of ' + my_file_path_and_name + ' file ]')
    # read file in binary mode
    with open(my_file_path_and_name, 'rb') as in_file:
        text = in_file.read()

    i.update(text)
    print('Input: content of ' + my_file_path_and_name + ' file that was read as bytes')
    print("Digest Output: ",i.digest())
    print("Digest as hex Output: ", hexlify( i.digest()) ) 
    print(end='\n\n')
    # equivalent Linux terminal command: sha1sum dir_a/dir_b2/file_b2.txt
    # end of example 2 - do not use for get_tree_digest



    # example 3 
    header('[ example 3: get hash of content of ' + my_file_path_and_name + ', useful for generating digest of file a  project]')
    print('We want the file path/name and file content to be part of the digest')
    j.update(my_file_path_and_name.encode())
    j.update(text)
    print('Input: we call .update() twice: on path/filename and then on file content')
    print(' 1. .update(b\'' + my_file_path_and_name + '\')')
    print(' 2. .update(text) where text is the content of ' + my_file_path_and_name + ' that was read as bytes')
    print("Digest Output: ",j.digest())
    print("Digest as hex Output: ", hexlify( j.digest())) 
    print(end='\n\n')

    # end of example 3

if __name__ == '__main__':
    basic_demo()




