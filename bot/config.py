import os
from typing import List


class User:
    def __init__(self, name, uid):
        self.name = name
        self.uid = uid


class Config:
    users: List[User] = []

    def __init__(self, users: List[User] = None):
        if not users:
            self.users = [
                self.__create_user_config("robbins", "ROBBINS_USERID"),
                self.__create_user_config("fendy", "FENDY_USERID"),
                self.__create_user_config("dave", "DAVE_USERID"),
                self.__create_user_config("emojirade", "EMOJIRADE_USERID")
            ]
        else:
            self.users = users

    def __create_user_config(self, name, env) -> User:
        return User(name, os.environ[env])

