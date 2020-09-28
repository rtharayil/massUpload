import unittest
from Model.Ad import Advertisement

class TestAd(unittest.TestCase):
   

    def setUp(self):
        self.myAd = Advertisement()

    
    def test_EventText(self):
        self.myAd.setMessage('A write-up about the event and why are you awarding this certificate in less than 50 words ')
        self.assertEqual('A write-up about the event and why are you awarding this certificate in less than 50 words ',self.myAd.getMessage())
    
    def test_Logo(self):
        self.myAd.setLogo('logo')
        self.assertEqual('logo',self.myAd.getLogo())
    
    def test_Banner(self):
        self.myAd.setBanner('Banner')
        self.assertEqual('Banner',self.myAd.getBanner())

    def test_CTALink(self):
        self.myAd.setCTALink('CTALink')
        self.assertEqual('CTALink',self.myAd.getCTALink())

    def test_CTAMessage(self):
        self.myAd.setCTAMessage('CTAMsg')
        self.assertEqual('CTAMsg',self.myAd.getCTAMessage())


    def test_CheckProgrameName(self):
        self.myAd.setPhone('91 9887734034')
        self.assertEqual('91 9887734034',self.myAd.getPhone())

    def test_CheckEmail(self):
        self.myAd.setEmail('rt@ep.com')
        self.assertEqual('rt@ep.com',self.myAd.getEmail())

    def test_CheckWebLink(self):
        self.myAd.setWebLink('WebLink')
        self.assertEqual('WebLink',self.myAd.getWebLink())
'''
    def test_CheckProgrameName(self):  
        self.myEvent.setProgram('XP2020')     
        self.assertEqual("XP2020", self.myEvent.getProgram())

    def test_CheckIssuer(self):
        self.myEvent.setIssuer('Thomas K')   
        self.assertEqual('Thomas K', self.myEvent.getIssuer())
    
    def test_Institution(self):
        self.myEvent.setInstitution('quadralogics') 
        self.assertEqual('quadralogics',self.myEvent.getInstitution())
    
    def test_DateOfEvent(self):
        self.myEvent.setDate('22.Aug.2020')
        self.assertEqual('22.Aug.2020',self.myEvent.getDate())

    
 
    
       

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)
'''

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestAd)
    unittest.TextTestRunner(verbosity=2).run(suite)