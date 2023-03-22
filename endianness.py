#!/usr/bin/env python3

import argparse
from math import log2,floor

""" 
                        2023-03-22  vs 22-03-2023

endianness = byte order
             * big-endian = big end = network-endian or network byte order (tcp/ip)
             * Most CPUs, Intel/AMD/ARM, use little end


see: https://en.wikipedia.org/wiki/Endianness
     https://www.freecodecamp.org/news/what-is-endianness-big-endian-vs-little-endian/

           9499938 (in base 10)
              |
          0x90f522  (in base 16)
        /     |    \
   90        f5      22   <----- big-endian, big end 🥚 = network order
 10010000 11110101 00100010  (base 2)   

    addr   90
    addr+1 f5
    addr+2 22


    22       f5        90  <---- little-endian, little end 🥚
 00100010 11110101 10010000  (little-endian, little end)

    addr   22
    addr+1 f5
    addr+2 90
 

https://www.intel.com/content/dam/www/public/us/en/documents/application-notes/ixp4xx-ixc1100-big-endian-little-endian-modes-note.pdf
TCP/IP defines the network byte order as big-endian.
In other words, any 16- or 32-bit value within the various layer headers 
(e.g., an IP address, a packet length, or a checksum) must be sent and received with its MSB first.

Even if the computers at each end are little-endian, multi-byte integers passed between them must
be converted to network byte order (big-endian) prior to transmission across the network, and
converted back to little-endian at the receiving end. 

"""

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


if __name__ == '__main__':
    order, integer = prep()
    # using floor and log2 to calculate bytes needed to represent unsigned integer
    my_bytes = (integer).to_bytes( floor( log2( integer ) / 8) + 1, order)
    write_bytes_to_file(my_bytes, order)


