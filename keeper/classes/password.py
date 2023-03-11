import random

from keeper.config import INIT_QUERY


class Password:
    def __init__(self, strong: int, length: int = 10):
        self.password_length = length
        self.strong = strong
        self.password = ""

    def __str__(self) -> str:
        return "Password object"

    @staticmethod
    def shuffle_str_query():
        random.shuffle(INIT_QUERY)

    def create_passwords(self) -> str:
        self.shuffle_str_query()
        self.password = "".join([i for i in INIT_QUERY[:self.password_length]])
        return self.password

    def encode_password(self):
        ...

    def get_password_length(self):
        return self.password_length


pass_object = Password(5)
print(pass_object.create_passwords())
