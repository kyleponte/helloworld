import unittest

class fooTest(unittest.TestCase):

    def test_hello(self):
        self.assertEqual(5, 5, 'Five equals five')


if __name__ == '__main__':
    print('Testing...')
    unittest.main(verbosity=2)