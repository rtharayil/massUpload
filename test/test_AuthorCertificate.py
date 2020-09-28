import os
import unittest
from Model.Certificates import Certificate
from Model.Certificates import AllCertificates
from CertificateDataLoder import CertificateDataLoder
from IssueCertificate import IssueCertificate
import shutil  

class test_IssueCertificate(unittest.TestCase):
   

    def setUp(self):
        self.allCertificates = AllCertificates()
        self.certificateDataLoder = CertificateDataLoder()
        self.issue = IssueCertificate()

    def test_Create(self):
        
        pathToSave = './temp'
        shutil.rmtree(pathToSave)
        os.mkdir(pathToSave) 
        certificate =Certificate('Rahul Panday','rahul@panday.com')
        
        certificateFile = self.issue.Create(395,58,186,200, 'template.png' , './res/Angelica Caroline.ttf' ,pathToSave ,'https://certifyme.online/devopsma/' ,  certificate )
        
        self.assertTrue(os.path.exists(pathToSave+ '/'+ certificateFile))

    def test_BulkIssue(self):

        pathToSave = './temp'
        shutil.rmtree(pathToSave)
        os.mkdir(pathToSave)

        self.f = open('names.csv', "w")
        self.f.write("No,First Name ,Second Name" +"\n")
        self.f.write("1 ,ranjith, tharayil " +"\n")
        self.f.write("2 ,anju, M dominic " +"\n")
        self.f.write("3 ,Suraj, Meaheta " +"\n")
        self.f.close()
        certificates= self.allCertificates.getAllCertificates()
        self.certificateDataLoder= self.certificateDataLoder.load(certificates ,'names.csv',False)
        self.allCertificates.setQRCodeLocation(1700,10)
        self.allCertificates.setNameLocation(700,440)
        
        certificateFile = self.issue.BulkIssue('AnuMDominic.png','./res/Angelica Caroline.ttf' ,pathToSave ,'https://certifyme.online/devopsma/' ,  self.allCertificates )
        path, dirs, files = next(os.walk(pathToSave))
        file_count = len(files)
        self.assertEqual(file_count,len(certificates))


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(test_IssueCertificate)
    unittest.TextTestRunner(verbosity=2).run(suite)
        