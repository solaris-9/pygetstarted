#from markov import Markov
import markov
import unittest


class TestMarkov(unittest.TestCase):
    def test_markov(self):
        m = markov.Markov('ab')
        res = m.predict('a')
        self.assertEqual(res, 'b')

    def test_markov2(self):
        m = markov.Markov('abc', size=2)
        res = m.predict('ab')
        self.assertEqual(res, 'c')

    def test_word_markov(self):
        m = markov.WordMarkov(['hello', 'world'])
        res = m.predict('hello')
        self.assertEqual(res, 'world')
        
    def test_get_table(self):
        res = markov.get_table('ab')
        self.assertEqual(res, {'a': {'b': 1}})

    def test_get_table2(self):
        res = markov.get_table('abc', size=2)
        self.assertEqual(res, {'ab': {'c': 1}})

    def test_get_table_word(self):
        #import pdb; pdb.set_trace()
        res = markov.get_table(['hello', 'world'])
        self.assertEqual(res, {'hello': {'world': 1}})



if __name__ == '__main__':
    unittest.main()
