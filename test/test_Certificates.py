import unittest
from Model.Certificates import Certificate
from Model.Certificates import AllCertificates

class Certificates(unittest.TestCase):
    
    def setUp(self):
        self.allCertificates = AllCertificates()
        self.allCertificates.getAllCertificates().append(Certificate('Ranjith Tharayil','r@gmail.com'))
        self.allCertificates.getAllCertificates().append(Certificate('R Tharayil','rp@gmail.com'))
        self.allCertificates.getAllCertificates().append(Certificate('anjith Tharayil','riop@gmail.com'))

    def test_AddingCertificates(self):
        
        self.allCertificates.getAllCertificates().clear()
        self.allCertificates.getAllCertificates().append(Certificate('Ranjith Tharayil','r@gmail.com'))
        self.allCertificates.getAllCertificates().append(Certificate('Ranjith Tharayil','r@gmail.com'))
        self.allCertificates.getAllCertificates().append(Certificate('Ranjith Tharayil','r@gmail.com'))
        self.assertEqual(3 ,len(self.allCertificates.getAllCertificates()))
    
    def test_getACertificatesName(self):

        self.allCertificates.getAllCertificates().clear()
        self.allCertificates.getAllCertificates().append(Certificate('Ranjith Tharayil','r@gmail.com'))
        
        for c in self.allCertificates.getAllCertificates():
            self.assertEqual('Ranjith Tharayil' ,c.Name())

    def test_getACertificatesEmail(self):

        self.allCertificates.getAllCertificates().clear()
        self.allCertificates.getAllCertificates().append(Certificate('Ranjith Tharayil','r@gmail.com'))
        
        for c in self.allCertificates.getAllCertificates():
            self.assertEqual('r@gmail.com' ,c.Email())

    def test_QRCodeLocation(self):
        self.allCertificates.setQRCodeLocation(1000,300)
        x,y = self.allCertificates.getQRCodeLocation()
        self.assertEqual(1000,x)
        self.assertEqual(300,y)

    def test_NameLocation(self):
        self.allCertificates.setNameLocation(1001,301)
        x,y = self.allCertificates.getNameLocation()
        self.assertEqual(1001,x)
        self.assertEqual(301,y)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(Certificates)
    unittest.TextTestRunner(verbosity=2).run(suite)