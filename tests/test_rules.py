import unittest
import sys

sys.path.append('src')
from rules import Rules
from bookkeeping import Directions

class TestRules(unittest.TestCase):

    def test_type_verification(self):

        # does value error get raised before type error? why??
        with self.assertRaises(TypeError):
            rules = Rules(columns = 6.5)

        with self.assertRaises(TypeError):
            rules = Rules(rows = 6.5)

        with self.assertRaises(TypeError):
            rules = Rules(connect_to_win= 4.5)

        with self.assertRaises(TypeError):
            rules = Rules(versus_human= 'true')

        with self.assertRaises(TypeError):
            rules = Rules(points_to_win=1.5)

        with self.assertRaises(TypeError):
            rules = Rules(exclude_directions=[Directions('H')])

        with self.assertRaises(TypeError):
            rules = Rules(exclude_directions=set('H'))

    def test_value_verification(self):

        with self.assertRaises(ValueError):
            rules = Rules(columns=5)

        with self.assertRaises(ValueError):
            rules = Rules(rows=5)

        with self.assertRaises(ValueError):
            rules = Rules(connect_to_win=3)

        with self.assertRaises(ValueError):
            rules = Rules(points_to_win=0)

if __name__ == '__main__':
    unittest.main()