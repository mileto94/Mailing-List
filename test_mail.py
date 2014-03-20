import unittest
import mail

class TestMail(unittest.TestCase):
    """docstring for TestMail"""


    def test_exist_name_and_email(self):
        new_list = mail.Mail_list({"ana gosdsad":"ana@gmail.com" , "joro": "joro.dir.bg"})
        self.assertEqual("ana@gmail.com",new_list.get_mail("ana gosdsad"))

    def test_add_person(self):
        new_file = open("FMI", "w+")
        new_list = mail.Mail_list({"george": "george@sbv.bg", "emma": "emma@abv.bg", "Daniel Lilov":'didi@didi'})
        new_list.add_person("FMI", "ani", "ani@abv.bg")
        self.assertEqual({'george':"george@sbv.bg", "emma":"emma@abv.bg", "ani":"ani@abv.bg", "Daniel Lilov":'didi@didi'}, new_list.show_list_content(new_file))
        new_file.close()



if __name__ == '__main__':
    unittest.main()
