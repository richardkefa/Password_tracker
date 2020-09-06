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
  return Credentials.copy_credentials()