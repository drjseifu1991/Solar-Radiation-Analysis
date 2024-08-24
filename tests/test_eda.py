import unittest
import pandas as pd
from scripts.eda import load_data

class TestEDA(unittest.TestCase):
    def test_load_data(self):
        df = load_data('../data/benin.csv')
        self.assertIsInstance(df, pd.DataFrame)

if __name__ == '__main__':
    unittest.main()
