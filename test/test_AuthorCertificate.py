import os
import unittest
from Model.Certificates import Certificate
from Model.Certificates import AllCertificates
from CertificateDataLoder import CertificateDataLoder
from AuthorCertificate import AuthorCertificate
import shutil  

class test_IssueCertificate(unittest.TestCase):
   

    def setUp(self):
        self.allCertificates = AllCertificates()
        self.certificateDataLoder = CertificateDataLoder()
        self.issue = AuthorCertificate()

    def test_Create(self):
        
        pathToSave = './temp'
        if os.path.isdir(pathToSave):
            shutil.rmtree(pathToSave)
        
        os.mkdir(pathToSave) 
        certificate =Certificate('Rahul', 'Panday','rahul@panday.com')
        
        certificateFile = self.issue.Create( './test/data/template.png'  ,pathToSave ,'https://certifyme.online/devopsma/' ,  certificate )
        
        self.assertTrue(os.path.exists(pathToSave+ '/'+ certificateFile))

    def test_BulkIssue(self):

        pathToSave = './temp'
        

        self.f = open('names.csv', "w")
        self.f.write("No,First Name ,Second Name" +"\n")
        self.f.write("1 ,Ranjith, Tharayil " +"\n")
        self.f.write("2 ,Anju, M Dominic " +"\n")
        self.f.write("3 ,Suraj, Meaheta " +"\n")
        self.f.close()
        certificates= self.allCertificates.getAllCertificates()
        self.certificateDataLoder= self.certificateDataLoder.load(certificates ,'names.csv',False)
        self.issue.setQRCodeLocation(400,700)
        self.issue.setNameLocation(739,274)
        self.issue.setQrCodeSize(3)
        self.issue.setNameFont('./res/Font Pack/Ubuntu-B.ttf',50)
        self.allCertificates.setTemplate('./test/data/AgileNCR_Participation.png')
        certificateFile = self.issue.BulkIssue(pathToSave ,'https://certifyme.online/devopsma/' ,  self.allCertificates )
        path, dirs, files = next(os.walk(pathToSave))
        file_count = len(files)
        self.assertEqual(file_count,len(certificates))


    def test_QRCodeLocation(self):
        self.issue.setQRCodeLocation(1000,300)
        x,y = self.issue.getQRCodeLocation()
        self.assertEqual(1000,x)
        self.assertEqual(300,y)

    def test_NameLocation(self):
        self.issue.setNameLocation(1001,301)
        x,y = self.issue.getNameLocation()
        self.assertEqual(1001,x)
        self.assertEqual(301,y)
    
    def test_setQrCodeSize(self):
        self.issue.setQrCodeSize(5)
        self.assertEqual(5,self.issue.getQRCodeSize())
    

    def test_setQRCodeColor(self):
        self.issue.setQRCodeColor('black','white')
        back_color, front_color =self.issue.getQRCodeColor()
        self.assertEqual('black',back_color)
        self.assertEqual('white',front_color)

    def test_setNameFont(self):
        self.issue.setNameFont('black',10)
        font, size =self.issue.getNameFont()
        self.assertEqual('black',font)
        self.assertEqual(10,size)



if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(test_IssueCertificate)
    unittest.TextTestRunner(verbosity=2).run(suite)
        