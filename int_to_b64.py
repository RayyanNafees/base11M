import base64

filename = input('filepath (int-file): ')
filename = filename if filename.endswith('.int') else filename+'.int'

with open(filename) as intfile:
    number = int(intfile.read())
    #number_bytes = number.to_bytes((number.bit_length() + 7) // 8, byteorder="big")
    encoded = base64.b64encode(number.to_bytes(2, 'big')) # number_bytes
    open(filename.replace('.int','.b64'), 'wb').write(encoded)
