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



class test_mdGen(unittest.TestCase):
   

    def setUp(self):
    
        self.mdGen = mdGen()
        


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
        self.f.write("Template : ./AnuMDominicnew.png" +"\n") 
        self.f.write("Logo : ./logo.png" +"\n")
        self.f.write("Message : As your organizations progresses through its DevXOps journey, what are the best practices that successful teams use that you should follow? Discover what separates successful DevXOps teams from those that fail, and learn the next steps to take on your DevXOps journey" +"\n")
        self.f.write("Banner : ./banner.png" +"\n")
        self.f.write("CTAMessage : Download our E-Book to learn more" +"\n")
        self.f.write("CTALink : www.q.com" +"\n")
        self.f.write("CTALabel : Dload"+"\n")
        self.f.write("Phone : 898654423" +"\n")
        self.f.write("Email : a@p.com" +"\n")
        self.f.write("WebLink : www.qt.com" +"\n")
        self.f.write("Font : ./res/AngelicaCaroline.ttf" +"\n")
        self.f.write("FontSize : 100"+"\n")
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


    def test_genMDFile(self):
        pathToSave = './md'
        
        if os.path.isdir(pathToSave):
            shutil.rmtree(pathToSave)
        os.mkdir(pathToSave) 
        certificate =Certificate('Rahul' , 'Panday','rahul@panday.com')
        
        mdFile = self.mdGen.Create( pathToSave ,'https://certifyme.online/devopsma/' ,  certificate )
        
        self.assertTrue(os.path.exists(mdFile))
    
    def test_genMDBulkIssue(self):
        pathToSave = './md'        

        self.f = open('names.csv', "w")
        self.f.write("No,First Name ,Second Name" +"\n")
        self.f.write("1 ,ranjith, tharayil " +"\n")
        self.f.write("2 ,anju, M dominic " +"\n")
        self.f.write("3 ,Suraj, Meaheta " +"\n")
        self.f.close()
        certificates= self.allCertificates.getAllCertificates()
        self.certificateDataLoder= self.certificateDataLoder.load(certificates ,'names.csv',False)       
        
        certificateFile = self.mdGen.genMDBulkIssue(pathToSave ,'https://certifyme.online/devopsma/' ,  self.allCertificates )
        path, dirs, files = next(os.walk(pathToSave))
        file_count = len(files)
        self.assertEqual(file_count,len(certificates))


    def test_genDefaults(self):
        pathToSave = './md'        

        self.f = open('names.csv', "w")
        self.f.write("No,First Name ,Second Name" +"\n")
        self.f.write("1 ,ranjith, tharayil " +"\n")
        self.f.write("2 ,anju, M dominic " +"\n")
        self.f.write("3 ,Suraj, Meaheta " +"\n")
        self.f.close()
        certificates= self.allCertificates.getAllCertificates()
        self.certificateDataLoder= self.certificateDataLoder.load(certificates ,'names.csv',False)       
        
        defaultFile = self.mdGen.genDefaults(pathToSave , self.issue , self.event ,self.ad)
        self.assertTrue(os.path.exists(defaultFile))


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(test_mdGen)
    unittest.TextTestRunner(verbosity=2).run(suite)