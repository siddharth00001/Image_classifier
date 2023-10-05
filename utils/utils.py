import base64


def decode_image(imgstring,filename):
    img_data = base64.b64decode(imgstring)
    with open(filename,'wb') as f:
        f.write(img_data)
        f.close()

def encodeImageIntoBase64(croppedImagePath):
    with open(croppedImagePath,'rb') as file:
        return base64.b64encode(file.read())
