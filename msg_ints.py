from math import floor, log2

'''
  Demo Program:
       possible convertion of text message to integers using python
       also in the other direction
'''


# simple test message
message_string  = "This is a day for me to say hello world"

# 1. get blocks of fixed length, e.g. take slice in python
# 2. encode each block into bytes, e.g. str.encode('utf-8') in python
# 3. convert each byte into integers, e.g. int.from_bytes()

message_ints = []  # accumulator
for i in range(0,len(message_string),3):
    # print(i)
    # print(message_string[i:i+3])
    print(message_string[i:i+3].encode()) # utf-8 default 
    message_ints.append(int.from_bytes(message_string[i:i+3].encode()))

# print accumulator 
print( message_ints, type(message_ints) )


######################################################################
# now in the other direction 
message_bytes = bytes()  # accumulator
# convert int to bytes, e.g. use to_bytes in python
# note: you need to know how many bytes are needed:
#        needed_number_of_bytes = floor( log2( <my_int> ) / 8) + 1
#        you also want to specify network byte order (big)

for mi in message_ints:
    message_bytes += (mi).to_bytes( floor( log2( mi ) / 8) + 1, 'big') 

print( message_bytes, type(message_bytes) )

# you can convert back to 
print(message_bytes.decode(), type(message_bytes.decode() ))

