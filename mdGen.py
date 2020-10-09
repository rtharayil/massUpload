import os
import csv
from Model.Certificates import Certificate
from Model.Certificates import AllCertificates
import qrcode
import sys

import uuid
import shutil 


class mdGen:
    """All Certificates """
    
       

    # default constructor 
    def __init__(self):  
        self.x=0

    def Create(self,dirToSave,certPath , certificate):
        
        filePath = './' + dirToSave +'/' + certificate.get_FileName() + '.md'

        f = open(filePath, "w")

        f.write("--- \n")
        f.write("layout : newCert \n")
        f.write("issuedTo: " + certificate.Name()  +"\n")
        f.write("certificatePath: " + certificate.uri()  +"\n")
        f.write("--- \n")
        f.close()
        return filePath

 

    def genMDBulkIssue(self,pathToSave,cert_url , certificates):

        if os.path.isdir(pathToSave):
            shutil.rmtree(pathToSave)
        os.mkdir(pathToSave)

       
        for cert in certificates.getAllCertificates():
            self.Create(pathToSave,cert_url , cert)


    def genDefaults (self,dirToSave,issue , event, ad):

       

        filePath = './' + dirToSave +'/' + 'defaults' + '.yml'
        f = open(filePath, "w")

        f.write("defaults:\n")
        f.write("  - \n")
        f.write("    scope: \n")
        f.write("      path:"" \n")
        f.write("      type: "+ event.getEventCode() +  "\n")
        f.write("    value: \n")
        f.write("      issuedBy: " + event.getIssuer() + "\n")
        f.write("      issuedInstitute: " + event.getInstitution() + "\n")
        f.write("      dateOfIssue: " + event.getDate() + "\n")
        f.write("      program: " + event.getProgram() + "\n")
        f.write("      advCTAName: " + ad.getButtonLabel() + "\n")
        f.write("      advCTALink: " + ad.getCTALink() + "\n")
        f.write("      CTAText: " + ad.getCTAMessage() + "\n")
        f.write("      advBGImagelink: " + ad.getBanner() + "\n")
        f.write("      brandLogo: " + ad.getLogo() + "\n")
        f.write("      brandMessage: " + ad.getMessage() + "\n")
        f.write("      contactPh_number: " + str(ad.getPhone()) + "\n")
        f.write("      contactEmail: " + ad.getEmail() + "\n")
        f.write("      contactCompanyWebSiteLink: " + ad.getWebLink() + "\n")
        f.write("      text: " + event.getText() + "\n")

        f.close() 
        return filePath
        
