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

