import unittest
from Model.Certificates import Certificate
from Model.Certificates import AllCertificates
from CertificateDataLoder import CertificateDataLoder

class test_CertificateDataLoder(unittest.TestCase):
   

    def setUp(self):
        self.allCertificates = AllCertificates()
        self.certificateDataLoder = CertificateDataLoder()
        
        
    
    def test_CertificateLoading(self):
        
        self.f = open('names.csv', "w")
        self.f.write("No,First Name ,Second Name, email" +"\n")
        self.f.write("1 ,ranjith, tharayil ,rt@rt.com" +"\n")
        self.f.write("2 ,anju, M dominic ,anju@rt.com" +"\n")
        self.f.close()
        certificates= self.allCertificates.getAllCertificates()
        self.certificateDataLoder= self.certificateDataLoder.load(certificates ,'names.csv',True)
        self.assertEqual(2 ,len(certificates))
        
    def test_CertificateLoadingNoEmail(self):
        
        self.f = open('names.csv', "w")
        self.f.write("No,First Name ,Second Name" +"\n")
        self.f.write("1 ,ranjith, tharayil " +"\n")
        self.f.write("2 ,anju, M dominic " +"\n")
        self.f.write("2 ,anju, M dominic " +"\n")
        self.f.close()
        certificates= self.allCertificates.getAllCertificates()
        self.certificateDataLoder= self.certificateDataLoder.load(certificates ,'names.csv',False)
        self.assertEqual(3 ,len(certificates))

    def test_CertificateLoadingDataCheckWithEmail(self):
        
        self.f = open('names.csv', "w")
        self.f.write("No,First Name ,Second Name, email" +"\n")
        self.f.write("1 ,Ranjith, Tharayil ,rt@rt.com" +"\n")
        self.f.close()
        certificates= self.allCertificates.getAllCertificates()
        self.certificateDataLoder= self.certificateDataLoder.load(certificates ,'names.csv',True)
        for c in certificates:
            self.assertEqual('Ranjith Tharayil' ,c.Name())
            self.assertEqual('rt@rt.com' ,c.Email())


    def test_CertificateLoadingDataCheckWithNoEmail(self):
        
        self.f = open('names.csv', "w")
        self.f.write("No,First Name ,Second Name" +"\n")
        self.f.write("1 ,Ranjith, Tharayil " +"\n")
        self.f.close()
        certificates= self.allCertificates.getAllCertificates()
        self.certificateDataLoder= self.certificateDataLoder.load(certificates ,'names.csv',False)
        for c in certificates:
            self.assertEqual('Ranjith Tharayil' ,c.Name())
            

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(test_CertificateDataLoder)
    unittest.TextTestRunner(verbosity=2).run(suite)