import unittest

from translator  import EnglishToFrench, FrenchToEnglish

class TestFrenchToEnglish(unittest.TestCase): 
    def test_f2e1(self): 
        self.assertNotEqual(FrenchToEnglish('Néant'), '') # Test for null input for frenchToEnglish the output is null.
    def test_f2e2(self): 
        self.assertEqual(FrenchToEnglish('Bonjour'), 'Hello')  
    def test_f2e3(self): 
        self.assertEqual(FrenchToEnglish('Dormir'), 'Sleeping')   


class TestEnglishToFrench(unittest.TestCase): 
    def test_e2f1(self): 
        self.assertNotEqual(EnglishToFrench('None'), '') # Test for null input for frenchToEnglish the output is null.
    def test_e2f2(self): 
        self.assertEqual(EnglishToFrench('Hello'), 'Bonjour')     
    def test_e2f3(self): 
        self.assertEqual(EnglishToFrench('Sleeping'), 'Dormir')   


unittest.main()