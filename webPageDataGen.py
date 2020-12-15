import os
import unittest
from Model.Certificates import Certificate
from Model.Certificates import AllCertificates
from CertificateDataLoder import CertificateDataLoder
from mdGen import mdGen
from ConfigurationLoader import ConfigurationLoader
import shutil  
from AuthorCertificate import AuthorCertificate

from Model.Event import AnEvent

from Model.Ad import Advertisement

class webPageDataGen:
    """All Certificates """
   
    # default constructor 
    def __init__(self):  
        X=0
         

    def generate(self,csvCertFile,config):

        pathToSave ='./webPageDataGen'

        self.mdGen = mdGen()
        


        self.allCertificates = AllCertificates()
        self.certificateDataLoder = CertificateDataLoder()
        self.event = AnEvent()
        self.allCertificates = AllCertificates()
        self.issue = AuthorCertificate()
        self.ad = Advertisement()
        self.configurationLoader = ConfigurationLoader(self.event,self.allCertificates,self.issue,self.ad)
        
        self.configurationLoader.loadConfig("./test/data//SYNAPSE//config1.yaml") 
        certificates= self.allCertificates.getAllCertificates()
        self.certificateDataLoder= self.certificateDataLoder.load(certificates ,'./test/data//SYNAPSE//names.csv',False)   

              

        URL = "https://certifyme.online/CSIT/SYNAPSE/SYNAPSEQA2020/" 
        certificateFile = self.issue.BulkIssue(pathToSave+ "/"+self.event.getEventCode() ,URL ,  self.allCertificates ,eventCode=self.event.getEventCode())

        URL = URL + self.event.getEventCode() + "/"

        self.mdGen.genMDBulkIssue(pathToSave + "/"+ "_"+ self.event.getEventCode() ,URL ,  self.allCertificates )

        defaultFile = self.mdGen.genDefaults(pathToSave,self.issue , self.event ,self.ad)
        self.genLinkCSVFile(self.allCertificates)

    def generateBadge(self,csvCertFile,config):

        pathToSave ='./webPageDataGen'

        self.mdGen = mdGen()
        


        self.allCertificates = AllCertificates()
        self.certificateDataLoder = CertificateDataLoder()
        self.event = AnEvent()
        self.allCertificates = AllCertificates()
        self.issue = AuthorCertificate()
        self.ad = Advertisement()
        self.configurationLoader = ConfigurationLoader(self.event,self.allCertificates,self.issue,self.ad)
        
        self.configurationLoader.loadConfig(config) 
        certificates= self.allCertificates.getAllCertificates()
        self.certificateDataLoder= self.certificateDataLoder.load(certificates ,csvCertFile,False)   

              

       
        

        URL = "https://certifyme.online/" 

        self.mdGen.genMDBulkIssueBadge(pathToSave + "/"+ "_"+ self.event.getEventCode() ,self.event.getEventCode(),URL ,  self.allCertificates )

        defaultFile = self.mdGen.genDefaults(pathToSave,self.issue , self.event ,self.ad)
        self.genLinkCSVFile(self.allCertificates)

    def genLinkCSVFile(self,allCertificates):
        self.f = open('./webPageDataGen/namesWithLink.csv', "w")
        self.f.write("No,First Name ,Second Name , email ,Link" +"\n")
        i =0

        for cert in allCertificates.getAllCertificates():
            i =i +1
            firstName , secondName = cert.getName()
            

            line = str(i)+ "," + firstName + "," + secondName +"," + cert.Email() + "," + cert.getWebURL() +"\n"
            
            self.f.write(line)
            
        self.f.close() 