from pwn import * # pip install pwntools
import json
from Crypto.Util.number import bytes_to_long, long_to_bytes
import base64
import codecs
import random
from binascii import unhexlify


rem = remote('socket.cryptohack.org', 13377)

def json_recv():
    line = rem.recvline()
    return json.loads(line.decode())

def json_send(hsh):
    request = json.dumps(hsh).encode()
    rem.sendline(request)

def list_to_string(s):
    output = ""
    return(output.join(s))

for i in range(0,101):
    returned = json_recv()
    if "flag" in returned:
        print("\n FLAG: {}".format(returned["flag"]))
        break

    print("\nCycle: {}".format(i))
    print("Returned type: {}".format(returned["type"]))
    print("Returned encoded value: {}".format(returned["encoded"]))

    word = returned["encoded"]
    encoding = returned["type"]

    if encoding == "base64":
        decoded = base64.b64decode(word).decode('utf8')
    elif encoding == "hex":
        decoded = (unhexlify(word)).decode('utf8')
    elif encoding == "rot13":
        decoded = codecs.decode(word, 'rot_13')
    elif encoding == "bigint":
        decoded = unhexlify(word.replace("0x", "")).decode('utf8')
    elif encoding == "utf-8":
        decoded = list_to_string([chr(b) for b in word])

    print("Decoded: {}".format(decoded))
    print("Decoded Type: {}".format(type(decoded)))

    to_send = {
        "decoded": decoded
    }

    json_send(to_send)