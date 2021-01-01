Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:43:08) [MSC v.1926 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
========== RESTART: C:\Users\LENOVO\Documents\freshersWork_project.py ==========
.....Welcome to our netbanking Login page!.....
 Please enter Account name and password with login expiry time as min 
>>> create_account("john",216753,15) # to create an account
 Congratulations! You successfully create an account! 
>>> 
>>> login_accountAsRead("john") # to read the data in our existing account
 Hi john!
 You are successfully login to your account! 
 This login page will expired in 869 seconds
>>> 
>>> changing_password("john",31768) # to change the password in existing account
 Your password registered successfully 
>>> 
>>> login_accountAsRead("john") # try to read the data after password reset
 Hi john!
 You are successfully login to your account! 
 This login page will expired in 818 seconds
>>> 
>>> create_account("google",178642,20)
 Congratulations! You successfully create an account! 
>>> 
>>> create_account("john",127683,20) # try to create an account with same name
 Sorry this name is already exists....please enter a new name 
>>> 
>>> create_account("John sarife diwa",1654871,20) # try to create an account name with greater than our word limit and with using space
 Error : please enter valid account name that must contains only alphabets! 
>>> 
>>> create_account("dashi",217491976,15) # try to create an account with greater than our password limitation
 Please enter valid digit password 
>>> 
>>> login_accountAsRead("john")
 Hi john!
 You are successfully login to your account! 
 This login page will expired in 712 seconds
>>> 
>>> delete_account("Goggle") # try to delete an account which not in our database
 Sorry! Given account name does not exist in our database... please enter a valid name..
>>> 
>>> delete_account("google") # try to delete an account with existing account
 Your account successfully deleted 
>>> 
>>> login_accountAsRead("john") # try to read with expired time limit
 Hi john!
 You are successfully login to your account! 
 This login page will expired in 640 seconds
>>> 
>>> changing_password("Google",63762) # try to change account password which not in our database
 Sorry! Given account name does not exist in our database... please enter a valid name..
>>> 
>>> 