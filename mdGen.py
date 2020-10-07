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
        
        filePath = './' + dirToSave +'/' + certificate.Name().strip() + '.md'

        f = open(filePath, "w")

        f.write("--- \n")
        f.write("layout : newCert \n")
        f.write("issuedTo: " + certificate.Name()  +"\n")
        f.write("certificatePath: " + certPath  +"\n")
        f.write("--- \n")
        f.close()
        return filePath

 

    def genMDBulkIssue(self,pathToSave,cert_url , certificates):

        if os.path.isdir(pathToSave):
            shutil.rmtree(pathToSave)
        os.mkdir(pathToSave)

       
        for cert in certificates.getAllCertificates():
            self.Create(pathToSave,cert_url , cert)

        
