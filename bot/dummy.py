"""
Dummies as in crash test dummies, not useless dummies.
"""

from slack import WebClient
import os


class Dummy:
    def __init__(self, token, name):
        self.name = name
        self.client = WebClient(token=token)

    def send_message(self, message, channel):
        self.client.chat_postMessage(text=message, channel=channel)
