import pyperclip

class User:
  '''
  User login info class 
  '''
  def __init__(self,username,password):

    self.username = username
    self.password = password

  user_list=[]
  
  def save_user(self):
    '''
    saves user object to user list
    '''
    User.user_list.append(self)
  
  @classmethod
  def user_exists(cls,usernames,passwords):
    '''
    metod takes login credentials and compares them to saved ones before allowing user to login
    '''
    for user in cls.user_list:
      if user.username == usernames and user.password == passwords:
         return True
    return False  

class Credentials:
  '''
  User cresentils class
  '''
  def __init__(self,account,account_username,account_password):
    
    self.account = account
    self.account_password = account_password
    self.account_username = account_username
    
  credentials_list = []

  def save_credentials(self):
    '''
    saves credential object to credential list
    '''
    Credentials.credentials_list.append(self)
    
  
  def delete_credential(self):
    '''
    delete_credential method deletes saved credential from the credentials_list
    '''
    Credentials.credentials_list.remove(self)
    
  @classmethod
  def credential_search(cls,account):
    '''
    Searching Through credentials by accouunt
    
    Args:
    account: account to ser for
    returns:
    credentials that match the account
    '''
    for credentials in cls.credentials_list:
      if credentials.account == account:
        return credentials

    
  @classmethod
  def display_credentials(cls):
    return cls.credentials_list
  
  @classmethod
  def copy_credentials(cls,account):
    credentials_found = Credentials.credential_search(account)
    pyperclip.copy(credentials_found.account_password)

    
    