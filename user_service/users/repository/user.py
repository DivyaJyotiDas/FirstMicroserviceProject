from user_service.users.repository.user_repository import db_api
from user_service.users.model.models import UserTable

class User(object):
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password
        self.db = db_api

    def load_user_table(self):
        user_model = UserTable(username=self.username,
                        email=self.email,
                        password=self.password)
        return user_model

    def user_create(self):
        user_obj = self.load_user_table()
        self.db.users_create(user_obj)
        return True

    def is_exists(self):
        user_obj = self.load_user_table()
        if  self.username in  [self.db.users_get(user_obj.username).username]:
            return True
        return False


