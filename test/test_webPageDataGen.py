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
from webPageDataGen import webPageDataGen



class test_webPageDataGen(unittest.TestCase):
   

    def setUp(self):
    
        self.mdGen = mdGen()
        self.webPageDataGen = webPageDataGen()


        self.allCertificates = AllCertificates()
        self.certificateDataLoder = CertificateDataLoder()
        self.event = AnEvent()
        self.allCertificates = AllCertificates()
        self.issue = AuthorCertificate()
        self.ad = Advertisement()
        self.configurationLoader = ConfigurationLoader(self.event,self.allCertificates,self.issue,self.ad)
        

        
        self.f = open('config.yaml', "w")
        self.f.write("Program : XP2020" +"\n")  
        self.f.write("IssuedBy : Anju M Dominic" +"\n") 
        self.f.write("Institution : Quadralogics" +"\n") 
        self.f.write("Date : 29 dec 1982" +"\n") 
        self.f.write("Text : A write-up about the event" +"\n") 
        self.f.write("Template : AgileNCR_Participation.png" +"\n") 
        self.f.write("Logo : ./logo.png" +"\n")
        self.f.write("Message : As your organizations progresses through its DevXOps journey, what are the best practices that successful teams use that you should follow? Discover what separates successful DevXOps teams from those that fail, and learn the next steps to take on your DevXOps journey" +"\n")
        self.f.write("Banner : ./banner.png" +"\n")
        self.f.write("CTAMessage : Download our E-Book to learn more" +"\n")
        self.f.write("CTALink : www.q.com" +"\n")
        self.f.write("CTALabel : Dload"+"\n")
        self.f.write("Phone : 898654423" +"\n")
        self.f.write("Email : a@p.com" +"\n")
        self.f.write("WebLink : www.qt.com" +"\n")
        self.f.write("Font : ./res/Font Pack/Ubuntu-B.ttf" +"\n")
        self.f.write("FontSize : 50"+"\n")
        self.f.write("NameX : 150"+"\n")
        self.f.write("NameY : 160"+"\n")
        self.f.write("QRCodeX : 1500"+"\n")
        self.f.write("QRCodeY : 1600"+"\n")
        self.f.write("QRCodeFrontColor : white"+"\n")
        self.f.write("QRCodeBackColor : black"+"\n")
        self.f.write("QRCodeSize : 10"+"\n")
        self.f.write("EventCode: AgileNCR" +"\n")
        self.f.close()  
        self.configurationLoader.loadConfig("config.yaml") 

        self.f = open('names.csv', "w")
        self.f.write("No,First Name ,Second Name" +"\n")
        self.f.write("1 ,ranjith, tharayil " +"\n")
        self.f.write("2 ,anju, M dominic " +"\n")
        self.f.write("3 ,Suraj, Meaheta " +"\n")
        self.f.close()
    
    
    def test_generate(self):          

        
              
        
        certificateFile = self.webPageDataGen.generate('names.csv','config.yaml' )

        file_count =0

        if os.path.isdir('./webPageDataGen'):
            path, dirs, files = next(os.walk('./webPageDataGen'))
            file_count = len(files)
        self.assertTrue(file_count>=2)


    


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(test_webPageDataGen)
    unittest.TextTestRunner(verbosity=2).run(suite)