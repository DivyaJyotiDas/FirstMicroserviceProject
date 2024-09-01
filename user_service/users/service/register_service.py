from user_service.users.repository.user import User

class RegisterService(object):
    def __init__(self):
        pass

    def register_user(self, user):
        user_obj = User(username=user.username,
                        email=user.email,
                        password=user.password)
        if user_obj.user_create():
            return "Registered successfully."
        return "User already exists."