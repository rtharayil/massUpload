import unittest
from Model.Event import AnEvent

class TestEvent(unittest.TestCase):
   

    def setUp(self):
        self.myEvent = AnEvent()

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

    
    def test_EventText(self):
        self.myEvent.setText('A write-up about the event and why are you awarding this certificate in less than 50 words ')
        self.assertEqual('A write-up about the event and why are you awarding this certificate in less than 50 words ',self.myEvent.getText())
    
       
 
'''
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
    suite = unittest.TestLoader().loadTestsFromTestCase(TestEvent)
    unittest.TextTestRunner(verbosity=2).run(suite)