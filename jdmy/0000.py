import os
from PIL import Image, ImageFont, ImageDraw


def add_num(ImageFile):
    im = Image.open(ImageFile)
    font = ImageFont.truetype('msyh.ttc', 66)
    Path, Ext = os.path.splitext(ImageFile)
    d = ImageDraw.Draw(im)
    width, height = im.size
    d.text((width - 80, 0), '99', font=font, fill=(255, 255, 255))
    im.save('{0}addnum{1}'.format(Path, Ext))
    im.show()


ImageFile = 'C:/Users/asus/Desktop/profile.jpg'
add_num(ImageFile)
