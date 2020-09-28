import os
import csv
from Model.Certificates import Certificate
from Model.Certificates import AllCertificates
import qrcode
import sys
from PIL import Image , ImageDraw ,ImageFont
import uuid


class IssueCertificate:
    """All Certificates """
    
   
    # default constructor 
    def __init__(self):  
         self.x=0

    def Create(self,qx,qy,nx,ny,template,font,pathToSave,urlHead , certificate):
        qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=7,
        border=4,
        )
        unique_filename = str(uuid.uuid4().hex)

        qr.add_data(urlHead + unique_filename)

        qr.make(fit=True)

        img = qr.make_image(fill_color="transparent", back_color="black")
        img.save('./qrcode_test.png')

        first_image = Image.open(template)
        second_image = Image.open("./qrcode_test.png")
        first_image.paste(second_image, (qx,qy),second_image)


        image = Image.new("RGBA", (1200,200), (255,255,255,0))
        draw = ImageDraw.Draw(image)
        font = ImageFont.truetype(font, 150)

        draw.text((10, 0), certificate.Name(), (0,0,0), font=font)
        #img_resized = image.resize((188,45), Image.ANTIALIAS)
        first_image.paste(image, (nx,ny),image)

        first_image.save(pathToSave +'/'+ unique_filename + '.png')
        return unique_filename + '.png'

    def BulkIssue(self,template,font,pathToSave,urlHead , certificates):

        qx,qy = certificates.getQRCodeLocation()
        nx,ny = certificates.getNameLocation()
        for cert in certificates.getAllCertificates():
            self.Create(qx,qy,nx,ny,template,font,pathToSave,urlHead , cert)
                