import unittest
import mail


class createTest(unittest.TestCase):
	"""docstring for createTest"""
	def test_create1(self):
		self.assertEqual("new list was created", mail.create("new_list"))
	def test_create2(self):
		self.assertEqual("new list was created", mail.create("Hack Bulgaria"))
if __name__ == '__main__':
	unittest.main()

