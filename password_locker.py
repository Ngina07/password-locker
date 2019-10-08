import pyperclip
from user import User
from credentials import Credential
import string

def create_user(username,password):
	'''
	Function to create a new user account
	'''
	new_user = User(username,password)
	return new_user

def save_user(user):
	'''
	Function to save new user account
	'''
	user.save_user()

def user_exist (name):
	'''
	Checks if user exists
	'''
	return User.user_exists(name)
		
# def verify_user(firstname,password):
# 	'''
# 	Function that verifies the existence of the user before creating user credentials
# 	'''
# 	verify_user = Credential.check_user(firstname,password)
# 	return verify_user

def create_credential (account, userName, password):
	'''
	Function creates new credential
	'''
	new_credential = Credential ( account, userName, password)
	return new_credential


def save_credential(credential):
	'''
	Function to save a newly created credential
	'''
	Credential.save_credentials ()

def find_credentials():
	'''
	Method to find credentials
	'''
	return Credential.find_credentials(account)

def check_credentials(account):
	'''
	Checks if credential exists
	'''
	return Credential.credential_exists(account)

def delete_credentials(credential):
	'''
	Deletes credential after user command 
	'''
	return Credential.delete_credential(credential)

def display_credentials(user_name):
	'''
	Function to display credentials created and saved by the user
	'''
	return Credential.display_credentials (user_name)

def generate_password(self):
			'''
			Method to generate an 8 character password for a user 
			'''
			ge_password = Credential.generate_password()
			return ge_password

			
def main():
			print(' ')
			print('******Hey there, welcome to password locker***** I would like to: \n 1-Create an Account \n 2-Log In \n 3-Exit')
			short_code = input().lower().strip()
			if short_code == "1":
				print("Enter username")
				user_name = input()
				while True:
					print(" TP - To type your own password:\n GP - To generate random Password")
					short_code = input().lower().strip()
					if selected_choice  == 'tp':
					password = input("Input your password")
					break
				elif selected_choice == "gp":
					password = generate_password(password)
					break
				else: 
					print("Password error")
					save_user(create_user(first_name,last_name,password))
					print(" ")
					print(f"New Account Created for: {first_name} {last_name}  password: {password}")
					print("-"*69)

			elif short_code == '2':
					print("-"*60)
					print(' ')
					print('To login, enter your account details:')
					firstname = input('Enter your first name - ').strip()
					password = str(input('Enter your password - '))
					login = login_user(user_name,password)
					if login_user == login:
						print(" ")	
						print(f'Welcome {firstname}.')
						print(' ')
			while True
						print(" CR - to create new credentials: \n DC to Display credentials: \n RM- Delete credentials: \n CP- Copy credentials to clipboard")	
						short_code = input().lower().strip()
						if short_code == "cr":
							print("create new credentials")
							print("account name....")
							account = input().lower().strip()
							print("Your account username")
							userName = input()
							while True:
								print(" TP - To type your own pasword if you already have an account:\n GP - To generate random Password")
								password_Choice = input().lower().strip()
								if password_Choice == 'tp':
									password = input("Enter Your Own Password\n")
									break
								elif password_Choice == 'gp':
									password = generate_password(password)
									break
					else:
						print("Invalid password please try again")
				save_credentials(create_new_credential(account,userName,password))

		if __name__ == '__main__':
			main()














