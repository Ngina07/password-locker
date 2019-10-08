## PASSWORD LOCKER
### This is an app to create, view and delete one's account(s) credentials
#### By : Phillis Ngina Njoroge

### Description
Password Locker is a terminal run python application that allows users to create their own account and store details of their other accounts i.e. usernames and passwords of their various accounts.

## BDD
These are the behaviours that the application implements for use by a user.

The user would like to :

To create an account with my details - log in and password
Store my existing login credentials
Generate a password for a new credential/account
Copy my credentials to the clipboard

### Specifications
| Behaviour | Input |Output 
| ----------- | ----------- |----------|
| Display codes for navigation | In terminal: $./password_locker.py |I would like to:  1-Create an Account  2-Log In  3-Exit'
|Display prompt for creating an account | Enter:1 | Enter your username and password
|Display prompt for login in | Enter:1 | Enter your account name and password
|Display codes for main menu navigation|Login was successful |AD- Add credential VW- View existing credentials  RM- Delete credential EX- Exit application
|Display prompt for creating a credential| Enter: AD| Enter the account name, your username and password
|Display a list of credentials|Enter: VW|Prints a list of saved credentials
|Exit application| Enter: EX| Exit the current navigation stage

## Set-up/ Installation requirements
#### Prerequisites
* Python3.6
* pip
* pyperclip
* xclip

#### cloning
* In your terminal
>$ git clone https://github.com/Ngina07/password-locker 
$ cd password-locker

## Running the application
* In your terminal
>  $ chmod +x password_locker.py
  $ ./password_locker.py
## Known bugs
There are no known bugs

## Support and contact details
In the event any issue arises while using the webpage feel free to contact me through my email address, phillis.njoroge@strathmore.edu. Any and all contributions to the code are highly encouraged and appreciated

## Technologies Used
This site was build using

* Python3.6

## License
MIT License

Copyright (c) [2019] [Phillis Ngina Njoroge]

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.