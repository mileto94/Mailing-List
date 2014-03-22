import glob


class Mail_list():
    """docstring for Mail_List"""
    def __init__(self, list_persons):
        self.list_persons = list_persons

    def get_mail(self, name):
        return self.list_persons[name]

    def show_list_content(self, file_open):
        file_content = (file_open).read()
        names_and_mails1 = file_content.split('\n')
        del names_and_mails1[len(names_and_mails1) - 1]
        names_and_mails2 = []
        for item in names_and_mails1:
            names_and_mails2.append(item.split(' - '))
        file_content = {}
        for couple in names_and_mails2:
            file_content[couple[0]] = couple[1]
        return file_content

    def add_person(self, file_to_write, name, email):
        self.list_persons[name] = email
        file_write = open(file_to_write + '.txt', "w")
        for key in self.list_persons:
            file_write.write(key + " - " + self.list_persons[key] + "\n")
        file_write.close()
        return self.list_persons


def create(name):
    list_of_files = glob.glob(".txt")
    if name not in list_of_files:
        file = open(name + ".txt", 'w')
        file.write('')
        file.close
        name = Mail_list({})
        return "new list was created"


def show_lists():
    list_of_files = glob.glob("*.txt")
    files = []
    k = 1
    for filename in list_of_files:
        print ('[' + str(k) + '] ' + filename)
        files.append(filename)
        k = k + 1
    return files


def search_mail(name):
    files = show_lists()
    matches = []
    for file in files:
        file_to_read = open(file, 'r')
        file_content = file_to_read.read()
        if name in file_content:
            matches.append(file)
    return matches
