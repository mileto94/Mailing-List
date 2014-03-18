import unittest
import mail

class TestMail(unittest.TestCase):
    """docstring for TestMail"""
    def test_exist_name_and_email(self):
        new_list = mail.Mail_list({"ana":"ana@gmail.com" , "joro": "joro.dir.bg"})

        self.assertEqual("ana@gmail.com",new_list.get_mail("ana"))

if __name__ == '__main__':
    unittest.main()
