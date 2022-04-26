'''byte_val = b'\x00\x01'
  
# converting to int
# byteorder is big where MSB is at start
int_val = int.from_bytes(byte_val, "big")
'''
import base64

filename = input('filepath (b64): ')
filename = filename if filename.endswith('.b64') else filename+'.b64'

with open(filename, 'rb') as image:
    bindata = image.read()
    base10 = int.from_bytes(bindata, "big")
    print(base10, file=open(filename.replace('.b64','.int'), 'w'))
    
