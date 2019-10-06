import pyperclip
import string
# from user import User

class Credential:
	'''
	Class to create  account credentials, generate passwords and save credentials and passwords
	'''
	# Class Variables

	credentials_list =[]
	user_credentials_list = []

	@classmethod
	def check_user(cls,first_name,password):
		'''
		Method that checks if the name and password entered match entries saved in the users_list
		'''
		current_user = ''
		for user in User.users_list:
			if (user.first_name == first_name and user.password == password):
				current_user = user.first_name
		return current_user

	def __init__(self,user_name,site_name,account_name,password):

		'''
		Method to define the properties for each user object will hold.
		'''

		# instance variables
		self.user_name = user_name
		self.site_name = site_name
		self.account_name = account_name
		self.password = password

	def save_credentials(self):
		'''
		save_credentials method saves a newly created users to credentials_list
		'''
		# global users_list
		Credential.credentials_list.append(self)
	
	# def generate_password(size=8, char=string.ascii_uppercase+string.ascii_lowercase+string.digits):
	# 	'''
	# 	Method to generate an 8 character password for a user 
	# 	'''
	# 	user_password = ''.join(random.choice(char) for _ in range(size))
	# 	return user_password

	@classmethod
	def display_credentials(cls,user_name):
		'''
		Class method to display the list of credentials saved
		'''
		user_credentials_list = []
		for credential in cls.credentials_list:
			if credential.user_name == user_name:
				user_credentials_list.append(credential)
		return user_credentials_list
				

	
	# @classmethod
	# def find_by_site_name(cls, site_name):
	# 	'''
	# 	Method that takes in a site_name and returns credentials that matches that site_name.
	# 	'''
	# 	for credential in cls.credentials_list:
	# 		if credential.site_name == site_name:
	# 			return credential

	# @classmethod
	# def copy_credential(cls,site_name):
	# 	'''
	# 	Class method that copies a credential's info after the credential's site name is entered
	# 	'''
	# 	find_credential = Credential.find_by_site_name(site_name)
	# 	return pyperclip.copy(find_credential.password)
