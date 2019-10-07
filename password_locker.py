#!/usr/bin/env python3.6

import pyperclip
from user import User
from credentials import Credential

def create_user(firstname,lastname,password):
	'''
	Function to create a new user account
	'''
	new_user = User(firstname,lastname,password)
	return new_user

def save_user(user):
	'''
	Function to save new user account
	'''
	User.save_user(user)

def verify_user(firstname,password):
	'''
	Function that verifies the existence of the user before creating user credentials
	'''
	verify_user = Credential.check_user(firstname,password)
	return verify_user

def create_credential (user_name, site_name, account_name, password):
	'''
	Function creates new credential
	'''
	new_credential = Credential ( user_name, site_name, account_name, password)
	return new_credential

def save_credential(credential):
	'''
	Function to save a newly created credential
	'''
	Credential.save_credentials (credential)

def display_credentials(user_name):
	'''
	Function to display credentials created and saved by the user
	'''
	return Credential.display_credentials (user_name)

def main():
	print(' ')
	print('******Hey there, welcome to password locker*****')
	while True:
		print(' ')
		print('I would like to: \n 1-Create an Account \n 2-Log In \n 3-Exit-app')
		print(' ')
		short_code = input('Enter a choice: ').lower().strip()
		if short_code == '3':
			break

		elif short_code == '1':
			print("-"*69)
			print(' ')
			print("let's create you an account")
			first_name = input('Enter your first name - ').strip()
			last_name = input('Enter your last name - ').strip()
			password = input('Enter your password - ').strip()
			save_user(create_user(first_name,last_name,password))
			print(" ")
			print(f'New Account Created for: {first_name} {last_name}  password: {password}')
			print("-"*69)

		elif short_code == '2':
			print("-"*60)
			print(' ')
			print('To login, enter your account details:')
			firstname = input('Enter your first name - ').strip()
			password = str(input('Enter your password - '))
			user_exists = verify_user(firstname,password)
			if user_exists == firstname:
				print(" ")
				print(f'Welcome {firstname}. Please choose an option to continue.')
				print(' ')
			else: 
				print ("Wrong details")

		else: 
			print ("Wrong details")


if __name__ == '__main__':
	main()














