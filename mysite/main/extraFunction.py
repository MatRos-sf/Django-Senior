import qrcode
import os
def generationQrCode(name, content ):
    #if find(f'{name}.png','E:\\code\\Django\\Senior\\mysite\\main\\bonus\\code'):
    #    return True
    #else:
    img = qrcode.make(content)
    #tutaj zmienić adres jak na inny dysku ...
    img.save(f'E:\\code\\Django\\Senior\\mysite\\main\\static\\main\\code\\{name}.jpg')



def find(name,path):
    for root, dirs, files in os.walk(path):
        if name in files:
            return True
    return False


