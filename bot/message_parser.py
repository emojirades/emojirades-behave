from typing import List

from bot.config import Config, User


class MessageParser:
    message = None

    def __init__(self, config: Config):
        self.users: List[User] = config.users

    def with_message(self, message):
        self.message = message
        return self

    def uid_to_tag(self):
        for user in self.users:
            self.message  = self.message.replace(f"@{user.name}", f"<@{user.uid}>")
        return self

    def parse(self):
        return self.message
