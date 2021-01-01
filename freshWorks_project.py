import threading
import time

#using this import time to check whether time expires or not

dictionary = {} #assign this dictionary as global variable
#I assume this login page as netbanking for anybank...The netbanking has the feature of login expiry time and
#we can delete or deactivate the account when we won't need....So that the reason I choose this netbanking for my project

print(".....Welcome to our netbanking Login page!.....")
print(" Please enter Account name and password with login expiry time as min ")
def create_account( acc_name , password , login_expiry_time ):
    if acc_name in dictionary:
        print(" Sorry this name is already exists....please enter a new name ")
    else:
        if acc_name.isalpha():
            if( len(dictionary) < (1024*1024*1024) and password <= (16*1024*1024)):
                list_name = [ password , time.time() + login_expiry_time * 60] # (3600) used for long duration to logout 
                if len(acc_name)<=32:
                    dictionary[acc_name] = list_name
                    print(" Congratulations! You successfully create an account! ")
            else:
                print(" Please enter valid digit password ")
        else:                
            print(" Error : please enter valid account name that must contains only alphabets! ")
            


def login_accountAsRead( acc_name ):
    if acc_name not in dictionary:
        print(" Sorry! Given account name does not exists in our database... please enter valid name..") #error message
    else:
        checking = []
        checking = dictionary[acc_name]
        #print(checking)
        
        if int(time.time()) <= int(checking[1]):
            print(" Hi ",acc_name,"!",sep="")
            print(" You are successfully login to your account! ")
            print(" This login page will expired in",int(checking[1] - time.time()),"seconds")
        else:
            print(" Error : Sorry this",acc_name,"login page has expired! please login again ")



def delete_account( acc_name):
    if acc_name not in dictionary:
        print(" Sorry! Given account name does not exist in our database... please enter a valid name..") #error message
    else:
        del dictionary[acc_name]
        print(" Your account successfully deleted ")



def changing_password( acc_name , new_password ):
    if acc_name not in dictionary:
        print(" Sorry! Given account name does not exist in our database... please enter a valid name..")
    else:
        checking = []
        checking = dictionary[acc_name]
        checking[0] = new_password
        print(" Your password registered successfully ")
        







            
                  
        


