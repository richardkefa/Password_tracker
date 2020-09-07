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
  
def delete_credential(user):
  '''
  Function delete ctredential
  '''
  user.delete_credential()
  
def display_credentials():
  '''
  function that returns all saved credentials
  '''
  return Credentials.display_credentials()

def copy_credentials():
  '''
  function to copy password
  '''
  return Credentials.copy_credentials(account)


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
    print("-"*20)
  else:
    print("Enter correct username and password")
    print("\n")
  
  while True:
      print("User these short codes: cc - create new credentials, dc - Display credentials, dlc - Delete a credential, cp - copy credential password, ex - Exit app")
    
      short_code = input().lower()
    
      if short_code == 'cc':
        print("New Credential")
        print("-"*20)
        
        print("Enter account")
        account = input()
        
        print("Enter account username")
        account_username = input()
        
        print("Enter account password")
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
        
        print("\n")
        print(f"Are you sure you want to delete {delete_account} Enter Y to accept and N to cancel")
        confirm = input().lower()
        if confirm == "y":
          delete_credential(delete_account)
          print(f"{delete_account} deleted successfuly")
        elif confirm == "n":
          print("Delete action canceled")
          break
        else:
          print("Use correct letter")
          
      elif short_code == "cp":
        print("Enter account to copy passsword from")
        copy_account_password = input()
        copy_credentials(copy_account_password)
        print("\n")
        print("Pasword copied succefuly")
        
      elif short_code == "ex":
        print("\n")
        print("Bye......")
        break
      else:
        print("Please use correct short code")
  
if __name__ == "__main__":
  main()