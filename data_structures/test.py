import unittest

class MyTests(unittest.TestCase):

    def setUp(self):
        """
        This method is called before each test
        """
        self.mylist = [1,2,3]

    def test_not_equal(self):
        self.assertNotEqual(1, "1")

    def test_equal(self):
        self.assertEqual(1, int("1"))

    def test_true(self):
        self.assertTrue( 3 == len(self.mylist))

    def test_false(self):
        self.assertFalse( 5 == len(self.mylist))

    def test_raise(self):
        self.assertRaises(IndexError, lambda: self.mylist[4])

    def tearDown(self):
        """
        This method is called after each test
        """
        pass

if __name__ == '__main__':
    unittest.main()
