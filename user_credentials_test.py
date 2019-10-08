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
		self.new_user = User('Ngina','Ngish1234')

	def test__init__(self):
		'''
		Test to if check if user instances are initialized properly
		'''
		# self.assertEqual(self.new_user.account,"Phillis")
		self.assertEqual(self.new_user.username,"Ngina")
		self.assertEqual(self.new_user.password,"Ngish1234")

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
	def setUp(self):
		'''
		'''
		self.new_credential = Credential('Google','Ngina','Ngish1234')
		
	def test__init__(self):
		'''
		Test to if check the initialization/creation of credential instances is properly done
		'''
		self.assertEqual(self.new_credential.account,'Google')
		self.assertEqual(self.new_credential.userName,'Ngina')
		self.assertEqual(self.new_credential.password,'Ngish1234')
	

	def test_save_credentials(self):
		'''
		Test to check if the new credential information is saved into credentials list
		'''
		self.new_credential.save_credentials()
		self.assertEqual(len(Credential.credentials_list),1)

	def test_save_many_account(self):
		'''
		'''
		self.new_credential.save_credentials()
		test_credentials =  Credential('Google','Ngina','Ngish1234')
		test_credentials.save_credentials()
		self.assertEqual(len(Credential.credentials_list),3)

	def test_delete_credentials(self):
		'''
		'''
		self.new_crendetials.save_credentials()
		test_credentials = Credential('Google','Ngina','Ngish1234')
		test_credentials.save_credentials()
		test_credential.save_credentials()
        
		self.new_credential.delete_credentials()
		self.assertEqual(len(Credential.credentials_list),1)



	# # def test_generate_password(self):
	# # 	'''
	# # 	Test to check if new password is being generated
	# # 	'''
	# # 	self.twitter = Credential ('Twitter', 'Harlem', '')
	# # 	self.twitter.password = generate_password ()
	# # 	self.assertEqual()

	# def test_display_credentials(self):
	# 	'''
	# 	Test to check if credentials are displayed
	# 	'''
	# 	self.new_credential.save_credentials()
	# 	twitter = Credential ('Phillis','Twitter', 'Philly', 'philly1234')
	# 	twitter.save_credentials()
	# 	self.assertEqual(len(Credential.display_credentials(twitter.user_name)),1)
	
	# def test_find_credentials(self):
	# 	self.new_credential.save_credentials()
	# 	test_credentials = Credential ('Phillis','Twitter', 'Philly', 'philly1234')
	# 	test_credentials.save_credentials()

if __name__ == '__main__':
    unittest.main()