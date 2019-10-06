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

def verify_user(firstname,lastname,password):
	'''
	Function that verifies the existence of the user before creating user credentials
	'''
	verify_user = Credential.check_user(firstname,lastname,password)
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
















