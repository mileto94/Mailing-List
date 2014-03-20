import glob


class Mail_list():
    """docstring for Mail_List"""
    def __init__(self, list_persons):
        self.list_persons = list_persons
    def get_mail(self, name):
        return self.list_persons[name]
    # def show_list(self, 1):
    #   list_to_display=[]
    #   for key in self.list_persons:
    #       list_to_display.append(key)
    #   return list_to_display

    def show_list_content(self):
        file_content = file_open.read()
        return file_content

    def add_person(self,name, email):
        self.list_persons[name] = email
        return self.list_persons

def create (name):
    list_of_files=glob.glob(".txt")
    if name not in list_of_files:
        filename=name
        file=open(name+".txt", 'w')
        file.write('')
        file.close
        name=Mail_list({})
        return "new list was created"


def show_lists():
    list_of_files=glob.glob("*.txt")
    files = []
    k=1
    for filename in list_of_files:
        print ('['+str(k)+'] '+filename)
        files.append(filename)
        k=k+1
    return files

def write_into_file(filename, list_persons):
    file = open(filename, "w+")
    for people in list_persons:
        file_content = file.write(people + " " + file_persons[people])
    file.close()
