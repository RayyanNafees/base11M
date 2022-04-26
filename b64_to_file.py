import base64

filename = input('filepath (b64): ')
filename = filename if filename.endswith('.b64') else filename+'.b64'

with open(filename, 'rb') as image:
    image_read = image.read()
    image_64_decode = base64.decodebytes(image_read) 
    with open(filename[:-4], 'wb') as file:
        file.write(image_64_decode)
