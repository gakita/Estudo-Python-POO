import utils

class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

    def get_user_info(self):
        return {
            "username": self.username,
            "email": self.email
        }

    def update_email(self, new_email):
        if utils.validate_email(new_email):
            self.email = new_email
            return True
        return False