#!/usr/bin/env python
from password_trucker import User
from password_trucker import Credentials

def create_user(username,password):
  '''
  function to creat new user
  '''
  new_user = User(username,password)
  return new_user
def save_user(user):
  '''
  function to save contact
  '''
  user.save_user()
  
def user_exists(username,password):
  '''
  function to check if user exists
  '''
  return User.user_exists(username,password)

def create_credentials(account,account_username,account_password):
  '''
  function to create credential
  '''
  new_credentials = Credentials(account,account_username,account_password)
  return new_credentials

def save_credentials(credentials):
  '''
  function to save credentials
  '''
  credentials.save_credentials()

def search_credentials(account):
  '''
  function to serch through credentials
  '''
  return Credentials.credential_search(account)
  
def delete_credential(account):
  '''
  Function delete ctredential
  '''
  return Credentials.delete_credential(account)
  
def display_credentials():
  '''
  function that returns all saved credentials
  '''
  return Credentials.display_credentials()

def copy_credentials(account):
  '''
  function to copy password
  '''
  return Credentials.copy_credentials(account)

filename = "MOCK_passwords.csv"
def open_file(filename):
  with open(filename,'r') as suggested_password:
    password = suggested_password.readline()
    return password


def main():
  print("Hello welcome to the pasword tracker.Enter username and password to create account")
  
  print("Enter username")
  username = input()
  
  print("Enter passsword")
  password = input()
  
  #creating and saving user
  save_user(create_user(username,password))
  print("\n")
  print(f"{username} created account succesfuly")
  print("\n")
  
  print("Enter username and credentials to log in")
  print("Enter username")
  username = input()
  
  print("Enter Password")
  password = input()
  
  if user_exists(username,password):
    print(f"{username} you have loged in successfuly")
    print("-"*100)
    login_test=user_exists(username,password)
  else:
    while user_exists(username,password)==False:
      print("="*150)
      print("Enter correct username and password")
      print("\n")
      print("Enter username")
      username = input()
      print("Enter Password")
      password = input()
      print("="*150)
      login_test=user_exists(username,password)
      
    
  while login_test == True:
      print("Logged in")
      print("="*30)
      print("User these short codes: cc - create new credentials, dc - Display credentials, dlc - Delete a credential, cp - copy credential password, ex - Exit app")
    
      short_code = input().lower()
    
      if short_code == 'cc':
        print("New Credential")
        print("="*100)
        
        print("Enter account")
        account = input()
        
        print("Enter account username")
        account_username = input()
        
        print(f"Enter account password Suggested password: {open_file(filename)}")
        account_password = input()
        
        #Creating and saving credentials
        save_credentials(create_credentials(account,account_username,account_password))
        print("\n")
        print(f"{account} created succesfuly")
        print("\n")
        
      elif short_code == "dc":
        if display_credentials():
          print("Here is a list of all saved credntials")
          print("\n")
          for credentials in display_credentials():
            print(f"{credentials.account} {credentials.account_username} {credentials.account_password}")
            print("\n")
        else:
          print("\n")
          print("You Have not saved any credential yet")
          print("\n")
            
      elif short_code == "dlc":
        print("Enter account to delete")
        delete_account = input()
        if search_credentials(delete_account):
          print("\n")
          print(f"Are you sure you want to delete {delete_account} Enter Y to accept and N to cancel")
          confirm = input().lower()
          if confirm == "y":
            to_delete = search_credentials(delete_account)
            to_delete.delete_credential()
            print(f"{delete_account} deleted successfuly")
          elif confirm == "n":
           print("Delete action canceled")
           break
          else:
            print("Use correct letter")
        else:
          print("Credential you wish to delete does not exist")
          
      elif short_code == "cp":
        print("Enter account to copy password from")
        copy_account_password = input()
        if search_credentials(copy_account_password):
          copy_credentials(copy_account_password)
          print("\n")
          print("Pasword copied succefuly")
          print("="*150)
          
        else:
          print("Entered acoount does not exist")

      elif short_code == "ex":
        print("\n")
        print("Bye......")
        break
      else:
        print("Please use correct short code")
  
if __name__ == "__main__":
  main()