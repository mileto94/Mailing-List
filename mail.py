import glob


class Mail_list():
    """docstring for Mail_List"""
    def __init__(self, list_persons):
        self.list_persons = list_persons

    def get_mail(self, name):
        return self.list_persons[name]

    def show_list_content(self, file_open):
        file_content=file_open.read()
        return file_content


    def add_person(self,file_to_write, name):
        self.list_persons[name] = self.email
        file_write = open(file_to_write, "w")
        for key in self.list_persons:
            print(key, self.list_persons[key])
            file_write.write(key+" "+self.list_persons[key]+ "\n")
        file_write.close()
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

