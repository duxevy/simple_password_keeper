import random

from config import INIT_QUERY


class Password:
    def __init__(self, strong: int, length: int = 8):
        self.password_length = length
        self.strong = strong
        self.password = ""

    def __str__(self) -> str:
        return "Password object"

    @staticmethod
    def shuffle_str_query():
        random.shuffle(INIT_QUERY)

    def create_passwords(self) -> None:
        self.shuffle_str_query()
        self.password = "".join([i for i in INIT_QUERY[:self.password_length]])

    def encode_password(self):
        ...

    def get_password_length(self):
        return self.password_length

    def get_password(self):
        self.create_passwords()
        return self.password


pass_object = Password(5, 12)
print(pass_object.get_password())
