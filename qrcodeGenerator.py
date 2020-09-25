import qrcode
import os, sys
from PIL import Image , ImageDraw ,ImageFont
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data('Some data')
qr.make(fit=True)

img = qr.make_image(fill_color="transparent", back_color="black")
img.save('./qrcode_test.png')

first_image = Image.open("./AnuMDominic.png")
second_image = Image.open("./qrcode_test.png")
first_image.paste(second_image, (0,0),second_image)


image = Image.new("RGBA", (600,150), (255,255,255,0))
draw = ImageDraw.Draw(image)
font = ImageFont.truetype("./res/Angelica Caroline.ttf", 50)

draw.text((10, 0), "Ranjith", (0,0,0), font=font)
#img_resized = image.resize((188,45), Image.ANTIALIAS)
first_image.paste(image, (1250,50),image)

first_image.save("./AnuMDominicnew.png")