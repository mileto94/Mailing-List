class Mail_list():
    """docstring for Mail_List"""
    def __init__(self, list_persons):
        self.list_persons = list_persons
    def get_mail(self, name):
        return self.list_persons[name]


