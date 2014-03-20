import unittest
import mail

class TestMail(unittest.TestCase):
    """docstring for TestMail"""


    def test_exist_name_and_email(self):
        new_list = mail.Mail_list({"ana":"ana@gmail.com" , "joro": "joro.dir.bg"})
        self.assertEqual("ana@gmail.com",new_list.get_mail("ana"))

    def test_add_new_person(self):
        new_list = mail.Mail_list({"george": "george@sbv.bg", "emma": "emma@abv.bg"})
        new_list.add_person("john", "john@gmail.bg")
        self.assertEqual("john@gmail.bg", new_list.get_mail("john"))

    def test_write_into_file(self):
        new_file = mail.create("test")
        file = open()


if __name__ == '__main__':
    unittest.main()
