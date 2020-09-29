import os
import csv
from Model.Certificates import Certificate
from Model.Certificates import AllCertificates
import qrcode
import sys
from PIL import Image , ImageDraw ,ImageFont
import uuid


class AuthorCertificate:
    """All Certificates """
    
       

    # default constructor 
    def __init__(self):  
        self.x=0
        self.QRPosX =0
        self.QRPosY =0

        self.NamePosX =0
        self.NamePosY =0
        self.QRcodeSize=8
        self.QRCode_back_color='transparent'
        self.QRCode_front_color='black'
        self.NameFont = './res/Angelica Caroline.ttf'
        self.Fontsize = 100



    def setQRCodeColor(self , back_color, front_color):
        self.QRCode_back_color= back_color
        self.QRCode_front_color=front_color

    def setNameFont(self , font, size):
        self.NameFont= font
        self.Fontsize = size
    
    def setQrCodeSize(self,size):
        self.QRcodeSize =size

    def setQRCodeLocation(self,x,y):
        self.QRPosX =x
        self.QRPosY =y

    def setNameLocation(self,x,y):
        self.NamePosX =x
        self.NamePosY =y


    def getNameLocation(self):
        return self.NamePosX , self.NamePosY 

    def getQRCodeLocation(self):
        return self.QRPosX , self.QRPosY 
    


    def getQRCodeSize(self):
        return self.QRcodeSize
    
    def getQRCodeColor(self):
       return  self.QRCode_back_color , self.QRCode_front_color

    def getNameFont(self):
       return  self.NameFont ,  self.Fontsize 


    def Create(self,template,pathToSave,urlHead , certificate):
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
        first_image.paste(second_image, (self.QRPosX,self.QRPosY),second_image)


        image = Image.new("RGBA", (1200,200), (255,255,255,0))
        draw = ImageDraw.Draw(image)
        font = ImageFont.truetype(self.NameFont, 150)

        draw.text((10, 0), certificate.Name(), (0,0,0), font=font)
        #img_resized = image.resize((188,45), Image.ANTIALIAS)
        first_image.paste(image, (self.NamePosX,self.NamePosY),image)

        first_image.save(pathToSave +'/'+ unique_filename + '.png')
        return unique_filename + '.png'

    def BulkIssue(self,pathToSave,urlHead , certificates):

       
        for cert in certificates.getAllCertificates():
            self.Create(certificates.getTemplate(),pathToSave,urlHead , cert)
                