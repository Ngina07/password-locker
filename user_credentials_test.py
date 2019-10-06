import unittest
import pyperclip
from user import User
from credentials import Credential

class TestUser(unittest.TestCase):
	'''
	Test class that defines test cases for the user class behaviours.
	Args:
	    unittest.TestCase: helps in creating test cases
	'''
	def setUp(self):
		'''
		Function to create a user account before each test
		'''
		self.new_user = User('Phillis','Ngina','Ngish1234')

	def test__init__(self):
		'''
		Test to if check if user instances are initialized properly
		'''
		self.assertEqual(self.new_user.first_name,'Phillis')
		self.assertEqual(self.new_user.last_name,'Ngina')
		self.assertEqual(self.new_user.password,'Ngish1234')

	# def test_save_user(self):
	# 	'''
	# 	Test to check if the new users info is saved into the users list
	# 	'''
	# 	self.new_user.save_user()
	# 	self.assertEqual(len(User.users_list),1)

if __name__ == '__main__':
    unittest.main()