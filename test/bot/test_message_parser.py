from unittest import TestCase

from bot.config import Config, User
from bot.message_parser import MessageParser


class TestMessageParser(TestCase):
    def setUp(self) -> None:
        users = [
            User("robbins", "TESTID"),
            User("fendy", "NONE1")
        ]
        self.mp = MessageParser(Config(users))

    def test_uid_to_tag_single_user(self):
        assert self.mp.with_message(
            "Say hi to @fendy"
        ).uid_to_tag().parse() == "Say hi to <@NONE1>"

    def test_uid_to_tag_single_multiple_users(self):
        assert self.mp.with_message(
            "@robbins says hi to @fendy"
        ).uid_to_tag().parse() == "<@TESTID> says hi to <@NONE1>"

