


import unittest
from nlu import *

class TestPOS(unittest.TestCase):

    def test_pos_model(self):
        df = nlu.load('pos',verbose=True).predict('Part of Speech Tags identify each token in a sentence with a grammatical label')
        for c in df.columns: print(df[c])




if __name__ == '__main__':
    unittest.main()

