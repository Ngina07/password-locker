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











