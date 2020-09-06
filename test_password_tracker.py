import unittest
from password_trucker import User  # importing user class
from password_trucker import Credentials # importing credentials class


class TestUser (unittest.TestCase):
  '''
  Defined test case for user class
  '''

  def setUp(self):
    '''
    fixture setup
    '''
    self.new_user = User("richard", "#12345")

  def test_init(self):
    '''
    testing objest initialization
    '''
    self.assertEqual(self.new_user.username, "richard")
    self.assertEqual(self.new_user.password, "#12345")

  def test_save_user(self):
    '''
    testing saving user credentials
     '''
    self.new_user.save_user()  # saving new user
    self.assertEqual(len(User.user_list),1)
    
  def tearDown(self):
    '''
    method to clean up after every test
    '''
    User.user_list=[]
    
  # def test_login(self):
  #   '''
  #   testing validity of user credentials
  #   '''
  #   self.new_user.save_user()
  #   test_user = User("kefa","12345")
  #   test_user.save_user()
  #   login_info = User.user_login("kefa","12345")
  #   self.assertTrue(login_info)
    
  def test_login_exists(self):
    self.new_user.save_user()
    test_user = User("kefa","12345")
    test_user.save_user()
    user_exists = User.user_exists("richard","#12345")
    self.assertTrue(user_exists)


  # Credentials Tests
class Testcredentials(unittest.TestCase):    
  def setUp(self):
    '''
    credentials fixture
    '''
    self.new_credentials = Credentials("Twiter","richardkefa","rich2020")
  def tearDown(self):
    '''
    Method to clean up new_credentials after every run
    '''
    Credentials.credentials_list=[]
   
  def test_credentials_init(self):
    '''
    testing object initialization
    '''
    self.assertEqual(self.new_credentials.account,"Twiter")
    self.assertEqual(self.new_credentials.account_username,"richardkefa")
    self.assertEqual(self.new_credentials.account_password,"rich2020")
    
    
  def test_credential_save(self):
    '''
    Testing saving of new credential object
    '''
    self.new_credentials.save_credentials()
    self.assertEqual(len(Credentials.credentials_list),1)
    
  
if __name__ == "__main__":
    unittest.main()
