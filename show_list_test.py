import mail
import unittest


class TestShowListContent(unittest.TestCase):
    """docstring for TestShowListContent"""

    def setUp(self):
        self.file_to_read = "FMI.txt"

    def test_show_list_content(self):
        file_open = open(self.file_to_read, "r")
        content = file_open.read()
        file_open.seek(0)
        new_list = mail.Mail_list({"lili": "lili@gmail.com"})
        names_and_mails1 = content.split('\n')
        del names_and_mails1[len(names_and_mails1) - 1]
        names_and_mails2 = []
        for item in names_and_mails1:
            names_and_mails2.append(item.split(' - '))
        content = {}
        for couple in names_and_mails2:
            content[couple[0]] = couple[1]
        self.assertEqual(content, new_list.show_list_content(file_open))
        file_open.close()


if __name__ == '__main__':
    unittest.main()
