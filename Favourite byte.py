from binascii import unhexlify
import string

decoded = bytes.fromhex("73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d")

def decode(s):
    return ''.join([chr(s ^ a) for a in decoded])

for i in range(0, 127):
    if "crypto" in decode(i):
        print("\n Byte: ", decoded)
        print("\n Flag: ", decode(i))