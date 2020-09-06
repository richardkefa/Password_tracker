#!/usr/bin/env python
from password_trucker import User
from password_trucker import Credentials

def create_user(username,password):
  '''
  function to creat new user
  '''
  new_user = User(username,password)
  return new_user

  