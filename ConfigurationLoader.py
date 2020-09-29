import os
import csv
import yaml 
from Model.Certificates import Certificate
from Model.Certificates import AllCertificates

class ConfigurationLoader:
    """All Certificates """
   
    # default constructor 
    def __init__(self,event,certificates,issuer,ad):  
         self.event=event
         self.certificates =certificates
         self.issuer =issuer
         self.ad=ad
    


    def loadConfig(self,configFile):
        a_yaml_file = open(configFile)
        parsed_yaml_file = yaml.load(a_yaml_file)
        self.event.setProgram(parsed_yaml_file["Program"])
        self.event.setIssuer(parsed_yaml_file["IssuedBy"])
        self.event.setInstitution(parsed_yaml_file["Institution"])
        self.event.setDate(parsed_yaml_file["Date"])
        self.event.setText(parsed_yaml_file["Text"])

        self.certificates.setTemplate(parsed_yaml_file["Template"])

        self.ad.setLogo(parsed_yaml_file["Logo"])
        self.ad.setMessage(parsed_yaml_file["Message"])
        self.ad.setBanner(parsed_yaml_file["Banner"])
        self.ad.setCTAMessage(parsed_yaml_file["CTAMessage"])
        self.ad.setCTALink(parsed_yaml_file["CTALink"])
        self.ad.setPhone(parsed_yaml_file["Phone"])
        self.ad.setEmail(parsed_yaml_file["Email"])
        self.ad.setWebLink(parsed_yaml_file["WebLink"])

        self.issuer.setNameFont(parsed_yaml_file["Font"], parsed_yaml_file["FontSize"])
        self.issuer.setNameLocation(parsed_yaml_file["NameX"],parsed_yaml_file["NameY"])
        self.issuer.setQRCodeLocation(parsed_yaml_file["QRCodeX"],parsed_yaml_file["QRCodeY"])
        self.issuer.setQRCodeColor(parsed_yaml_file["QRCodeFrontColor"],parsed_yaml_file["QRCodeBackColor"])
        self.issuer.setQrCodeSize(parsed_yaml_file["QRCodeSize"])