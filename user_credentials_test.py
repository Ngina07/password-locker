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
		self.assertEqual(len(User.users_list),3)

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
		self.new_user = User('Phillis', 'Ngina', 'Ngish1234')
		self.new_user.save_user()
		user2 = User('James', 'Njoroge', 'Njosh1234')
		user2.save_user()

		for user in User.users_list:
			if user.first_name == user2.first_name and user.password == user2.password:
				current_user = user.first_name
		return current_user

		self.assertEqual(current_user,Credential.check_user(user2.password,user2.first_name))

	def setUp(self):
		'''
		Function to create an accounts credentials before each test
		'''
		self.new_credential = Credential('Harlem', 'Twitter', 'Harlemy', 'Harlem1234')

	def test__init__(self):
		'''
		Test to if check the initialization/creation of credential instances is properly done
		'''
		self.assertEqual(self.new_credential.user_name,'Harlem')
		self.assertEqual(self.new_credential.site_name,'Twitter')
		self.assertEqual(self.new_credential.account_name,'Harlemy')
		self.assertEqual(self.new_credential.password,'Harlem1234')

	def test_save_credentials(self):
		'''
		Test to check if the new credential information is saved into credentials list
		'''
		self.new_credential.save_credentials()
		twitter = Credential('Harlem','Twitter','Harlemy','Harlem1234')
		twitter.save_credentials()
		self.assertEqual(len(Credential.credentials_list),2)

if __name__ == '__main__':
    unittest.main()