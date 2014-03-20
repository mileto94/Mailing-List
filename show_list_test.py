import mail
import unittest
import sys


class TestShowListContent(unittest.TestCase):
    """docstring for TestShowListContent"""

    # def setUp(self):
    #     self.file_to_read = sys.argv[1]


    def test_show_list_content(self):
        file_open = open("FMI.txt", "r")
        content = file_open.read()
        self.assertEqual(content, mail.show_list_content(file_open))
        file_open.close()

if __name__ == '__main__':
    unittest.main()
