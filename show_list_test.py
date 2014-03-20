import mail
import unittest


class TestShowListContent(unittest.TestCase):
    """docstring for TestShowListContent"""

    def setUp(self):
        self.file_to_read = "FMI"


    def test_show_list_content(self):
        file_open = open(self.file_to_read, "r")
        content = file_open.read()
        file_open.seek(0) #returns the pointer at the begging of the file
        new_list = mail.Mail_list({"lili":"lili@gmail.com"})
        self.assertEqual(content, new_list.show_list_content(file_open))
        file_open.close()

if __name__ == '__main__':
    unittest.main()
