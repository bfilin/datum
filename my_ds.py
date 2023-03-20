import struct
import base64
import hashlib
#
# rfc4509
#
# digest = SHA_256(DNSKEY owner name | DNSKEY RDATA)
#
# where DNSKEY RDATA is defined by [RFC4034] as:
#
#      DNSKEY RDATA = Flags | Protocol | Algorithm | Public Key
#

# From: dig DNSKEY torquegear.me @1.1.1.1
key = "mdsswUyr3DPW132mOi8V9xESWE8jTo0dxCjjnopKl+GqJxpVXckHAeF+ KkxLbxILfDLUT0rAK9iUzy1L53eKGQ=="
key_ = base64.b64decode(key)


domain = 'torquegear.me.'

owner = bytes()
for i in domain.split('.'):
     owner += struct.pack('B', len(i)) + i.encode()

params = struct.pack('!HBB',257,3,13)
# params = bytes()
# params += (257).to_bytes(2,'big')
# params += (3).to_bytes(1,'big') 
# params += (13).to_bytes(1,'big')
# https://docs.python.org/3/library/struct.html
# module converts between Python values and C structs represented as Python bytes objects. 
# '!HBB'
#  first character of the format string can be used to indicate byte order, size and alignment of the packed data
#   ! network ( network byte order which is always big-endian, https://tools.ietf.org/html/rfc1700)
#
# Format Characters
#   H 'unsigned short' integer
#   B 'unsigned char' integer
#
# From: dig DNSKEY torquegear.me @1.1.1.1
#  flags       should be 257 KSK
#  protocol    Should be 3, backward compatibility 
#  algorithm   should 13, signing algorithm ECDSAP256SHA256

formatted  = owner + params + key_

print( hashlib.sha256(formatted).hexdigest().upper() )
