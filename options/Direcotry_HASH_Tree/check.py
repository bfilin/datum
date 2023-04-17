#!/usr/bin/env python3

import os
import sys
import argparse

from time import time
from binascii import hexlify
from tree_digest import get_tree_digest

help_screen = '''
This program tests your 'get_tree_digest' function defined dtree_digest.py module.
'''

parser = argparse.ArgumentParser(description=help_screen)
parser.add_argument("directory", help="specify directory structure to hash")
parser.add_argument('--debug', help="increase output verbosity", action="store_true")
args = parser.parse_args()


def prep():
    ''' this funciton prepares for execution  '''
    if os.path.isdir(args.directory):
        abs_path = os.path.abspath(args.directory)
        return get_tree_digest, os.path.dirname(abs_path), os.path.basename(abs_path), args.debug
    else:
        print('\nno such directory', args.directory)
        sys.exit(0)


def exec_with_timer(func, *pargs, **kargs):
    ''' this function returns the runtime and calculated digest value '''
    start = time()
    val = func(*pargs, **kargs)
    runtime = time() - start
    return runtime, val


if __name__ == '__main__':
    func, *args = prep()
    runtime, val = exec_with_timer(func, *args)
    fmt = "{0:>15}: {1}"
    print()
    print(fmt.format('Function', func.__name__))
    print(fmt.format('Runtime', runtime))
    print(fmt.format('Prefix', args[0]))
    print(fmt.format('Directory', args[1]))
    print(fmt.format('Digest Hash', hexlify(val)))
    print()



