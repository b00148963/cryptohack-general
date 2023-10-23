from binascii import unhexlify

keyEnc = bytes.fromhex('0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104')

# to find the start of the key
startKey = bytes(a ^ b for a, b in zip(keyEnc, b"crypto{"))

print("\n Key: ", startKey)

# to match the length of the ciphertext
key = (startKey.decode() + 'y').encode() * (len(keyEnc) // len(startKey) + 1)

# decrypt message
decrypted = bytes(a ^ b for a, b in zip(keyEnc, key))

print("\n Flag: ", decrypted.decode())