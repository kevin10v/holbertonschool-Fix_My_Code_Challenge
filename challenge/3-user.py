#!/usr/bin/python3
"""
User Model
"""
import hashlib
import uuid


class User():
    """
    User class:
    - id: public string unique (uuid)
    - password: private string hash in SHA256
    """

    def __init__(self):
        """
        Initialize a User instance
        """
        self.id = str(uuid.uuid4())
        self.__password = None

    @property
    def password(self):
        """
        Password getter
        """
        return self.__password

    @password.setter
    def password(self, pwd):
        """
        Password setter
        """
        if pwd is None or type(pwd) is not str:
            self.__password = None
        else:
            self.__password = hashlib.sha256(pwd.encode()).hexdigest().lower()

    def is_valid_password(self, pwd):
        """
        Valid password
        """
        if pwd is None or type(pwd) is not str:
            return False
        if self.password is None:
            return False
        pwd_e = pwd.encode()
        pwd_hashed = hashlib.sha256(pwd_e).hexdigest().lower()
        return pwd_hashed == self.password
