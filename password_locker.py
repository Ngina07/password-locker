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













