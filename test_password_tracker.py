import unittest
from password_trucker import User #importing user class 

class TestUser (unittest.TestCase):
  '''
  Defined test case for user class
  '''
  def test_init(self):
    '''
    testing object initialization
    '''
    def setUp(self):
      '''
      fixture setup
      '''
      self.new_user = User("richardkefa","#12345")
    def test_init(self):
      '''
      testing objest initialization
      '''
      self.assertEqual(self.new_user.username,"richard")
      self.assertEqual(self.new_user.password,"#12345")

if __name__ == "__main__":
    unittest.main()

