import pytest
from login import Login

def test_valid_login():
   login=Login("Vinitha","Test123")
   assert login.check_login() == "Login successful"


def test_invalid_username():
   login=Login("Vinitha11","Test123")
   assert login.check_login() == "Invalid username or password"

def test_invalid_password():
   login=Login("Vinitha","Testing123")
   assert login.check_login() == "Invalid username or password"

def test_invalid_username_password():
   login=Login("Vinitha22","Test12")
   assert login.check_login() == "Invalid username or password"

def test_invalid_nousername():
   login=Login("","Test12")
   assert login.check_login() == "Invalid username or password"

def test_invalid_nopassword():
   login=Login("Vinitha","")
   assert login.check_login() == "Invalid username or password"