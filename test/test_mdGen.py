import os
import unittest
from Model.Certificates import Certificate
from Model.Certificates import AllCertificates
from CertificateDataLoder import CertificateDataLoder
from mdGen import mdGen
import shutil  

class test_mdGen(unittest.TestCase):
   

    def setUp(self):
        self.allCertificates = AllCertificates()
        self.certificateDataLoder = CertificateDataLoder()
        self.mdGen = mdGen()

    def test_genMDFile(self):
        pathToSave = './md'
        
        if os.path.isdir(pathToSave):
            shutil.rmtree(pathToSave)
        os.mkdir(pathToSave) 
        certificate =Certificate('Rahul Panday','rahul@panday.com')
        
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


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(test_mdGen)
    unittest.TextTestRunner(verbosity=2).run(suite)