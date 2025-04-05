import unittest
from my_awesome_lib.data_utils import read_file, write_file

class TestDataUtils(unittest.TestCase):
    def test_read_file(self):
        write_file('test.txt', 'Hello, World!')
        self.assertEqual(read_file('test.txt'), 'Hello, World!')

    def test_write_file(self):
        write_file('test_write.txt', 'Test Content')
        self.assertEqual(read_file('test_write.txt'), 'Test Content')

if __name__ == '__main__':
    unittest.main()
