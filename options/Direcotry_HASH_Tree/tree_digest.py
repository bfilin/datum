#!/usr/bin/env python3
from hashlib import sha1  
from binascii import hexlify 
from demo import header
import os


def file_digest(file_abs_path, file_relative_path):
    ''' this helper function returns the digest value for file 
          from Hash('file_relative_path' + file-contents)

    Note(s): 
        * For the purposes of computing the digest of the file use a
          sha1 object from hashlib, and return the value from .digest() method.
        * You can use file_abs_path for reading file-content
    '''
    print('Todo: implement file_digest')


def get_tree_digest(prefix, path_in_tree, debug=False):
    '''
    Compute and return the digest value of a filesystem directory tree. 
    If debug=True, also print the intermediary calculated hashes of the tree
    objects that are nested inside.

    For the purposes of computing the digest of a filesystem directory structure
    use sha1 object from hashlib, and return the value from .digest() method.

    [Example]
    Suppose that in our ~/Documents/dir_hash_option folder we have a
    folder called 'dir_a' with the directory tree structure given below:

    dir_a
        ├── dir_b1
        ├── dir_b2
        │        └── file_b2.txt
        ├── file_a.txt
        └── song_a.m4a

    Note(s):
     * folder 'dir_a' is the parent directory, root of this structure
     * all other nested objects can be found either:
       i) via the Relative Path, starting from the root of the structure:
          e.g. Relative Path of file_b2.txt is:
           dir_a/dir_b2/file_b2.txt
       ii) via the Absolute Path, starting from the root of the filesystem:
          e.g. Absolute Path of file_b2.txt is:
           /home/<username>/Documents/dir_hash_option/dir_a/dir_b2/file_b2.txt
 

    Computing the hash:

    Hash('dir_a' +
      Hash('dir_a/dir_b1') +
      Hash('dir_a/dir_b2' +
        Hash('dir_a/dir_b2/file_b2.txt' + file_b2.txt-contents)) +
      Hash('dir_a/file_a.txt' + file_a.txt-contents) +
      Hash('dir_a/song_a.m4a' + song_a.m4a-contents))
    

    Note(s):
    * the + symbol means concatenation
    * when hasing an object:
        - The relative path to the object is hashed first
        - Followed by the contents of the hashed object.
          e.g. suppose h is the sha1 object from hashlib library,
            then to calculate digest for a file: 
                h.update(relative_path_to_file.encode() + file_contnet)      
    * The objects in a given directory are processed in the a lexicographical order.
    '''
    header('Todo: implement get_tree_digest() and helper function')
    return "".encode()


