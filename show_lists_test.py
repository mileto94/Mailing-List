import unittest
import mail
import glob


class show_listsTest(unittest.TestCase):
	"""docstring for show_listsTest"""
	def test_showing_lists(self):
		mail.create("FMI")
		list_file=glob.glob(".txt")
		self.assertEqual(list_file, mail.show_lists())


if __name__ == '__main__':
	unittest.main()
