import unittest
from Event.Event import AnEvent

class TestInputReader(unittest.TestCase):

   

    def setUp(self):
        self.myEvent = AnEvent('XP2020','Thomas K')

    def test_CheckProgrameName(self):        
        self.assertEqual("XP2020" ,self.myEvent.getProgram())

    def test_CheckIssuer(self):
        self.assertEqual('Thomas K', self.myEvent.getIssuer())
    
    
    
       
 
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
    suite = unittest.TestLoader().loadTestsFromTestCase(TestStringMethods)
    unittest.TextTestRunner(verbosity=2).run(suite)