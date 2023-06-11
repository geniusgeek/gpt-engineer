from user import User

class Authentication:
    def __init__(self):
        pass

    def login(self, username: str, password: str) -> User:
        # Implement login logic here
        return User(id=1, username=username, password=password, email="user@example.com")

    def register(self, username: str, password: str, email: str) -> User:
        # Implement registration logic here
        return User(id=1, username=username, password=password, email=email)
