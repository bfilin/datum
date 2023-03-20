#!/usr/bin/env python3

import argparse

# see
# https://www.freecodecamp.org/news/what-is-endianness-big-endian-vs-little-endian/

help_screen = '''
   pass an integer and and an endianness, 'big' (default) or 'little'.
'''

parser = argparse.ArgumentParser(description=help_screen)
parser.add_argument('-i','--integer', type = int, help = "specify the integer value",required = True)
parser.add_argument('-o','--order', default = 'big', choices = ['big', 'little'],type = str, help = 'specify byte order, endianness big/little')
args = parser.parse_args()


def write_bytes_to_file(my_bytes, order):
    with open("file_" + order, "wb") as binary_file:
        binary_file.write(my_bytes)



def prep():
    ''' this funciton prepares for execution  '''
    return args.order, args.integer


def exec_with_timer(func, *pargs, **kargs):
    ''' this function returns the runtime and calculated digest value '''
    start = time()
    val = func(*pargs, **kargs)
    runtime = time() - start
    return runtime, val


if __name__ == '__main__':
    order, integer = prep()
    # using the default of two bytes
    my_bytes = (integer).to_bytes(2, order)
    write_bytes_to_file(my_bytes, order)


