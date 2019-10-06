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

	def test_save_user(self):
		'''
		Test to check if the new users info is saved into the users list
		'''
		self.new_user.save_user()
		self.assertEqual(len(User.users_list),1)

class TestCredentials(unittest.TestCase):
	'''
	Test class that defines test cases for the credentials class behaviours.
	Args:
	    unittest.TestCase: helps in creating test cases
	'''
	def test_check_user(self):
		'''
		Function to test whether the login in function check_user works as expected
		'''
		self.new_user = User('Phillis','Ngina','Ngish1234')
		self.new_user.save_user()
		user2 = User('James','Njoroge','Njosh1234')
		user2.save_user()

		for user in User.users_list:
			if user.first_name == user2.first_name and user.password == user2.password:
				current_user = user.first_name
		return current_user

		self.assertEqual(current_user,Credential.check_user(user2.password,user2.first_name))

if __name__ == '__main__':
    unittest.main()