import unittest

import program.main as main


class Test(unittest.TestCase):
    '''  '''
    def setUp(self):
        pass

    def test_remove_duplicates(self):
        c = main.CaesarEncryption("REGENSCHIRMSTAENDER")
        self.assertEqual(c._remove_duplicates("aabbcc"), "ABC")

    def test_generate_key_alphabet(self):
        '''  '''
        test_key = "REGENSCHIRMSTAENDER"
        c = main.CaesarEncryption(test_key)
        self.assertEqual(c.key_alphabet, "REGNSCHIMTADZYXWVUQPOLKJFB")

    def test_encrypt(self):
        c = main.CaesarEncryption("REGENSCHIRMSTAENDER")
        self.assertEqual(c.encrypt("WASSER KOCHT IM TEEKESSEL"), "KRQQSU AXGIP MZ PSSASQQSD")

if __name__ == "__main__":
    unittest.main()
