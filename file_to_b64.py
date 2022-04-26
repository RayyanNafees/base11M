import base64

filename = input('filepath: ')

with open(filename, "rb") as image_file:
    encoded_string = base64.b64encode(image_file.read())
    open(filename+'.b64','wb').write(encoded_string)
