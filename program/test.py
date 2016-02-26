import unittest

import program.main as main


class Test(unittest.TestCase):
    '''  '''
    def setUp(self):
        pass

    def test_remove_duplicates(self):
        c = main.CaeserEncryption("REGENSCHIRMSTAENDER")
        self.assertEqual(c._remove_duplicates("aabbcc"), "ABC")

    def test_generate_key_alphabet(self):
        '''  '''
        test_key = "REGENSCHIRMSTAENDER"
        c = main.CaeserEncryption(test_key)
        self.assertEqual(c.key_alphabet, "REGNSCHIMTADZYXWVUQPOLKJFB")

if __name__ == "__main__":
    unittest.main()
