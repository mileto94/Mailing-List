import glob

class Mail_list():
	"""docstring for Mail_List"""
	def __init__(self, list_persons):
		self.list_persons = list_persons
	def get_mail(self, name):
		return self.list_persons[name]
	# def show_list(self, 1):
	# 	list_to_display=[]
	# 	for key in self.list_persons:
	# 		list_to_display.append(key)
	# 	return list_to_display

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
	list_of_files=glob.glob(".txt")
	k=1
	for filename in list_of_files:
		print ('['+str(k)+']'+filename)
		k=k+1
	return list_of_files





