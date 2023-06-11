from user import User

class ChatSession:
    def __init__(self, user: User):
        self.user = user
        self.chat_history = []

    def add_message(self, message: str):
        self.chat_history.append(message)

    def get_chat_history(self):
        return self.chat_history
