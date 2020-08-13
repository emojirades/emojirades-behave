import os
from slack import RTMClient


class BddRTMClient:

    event_trail = []

    def __init__(self):
        slack_token = os.environ["SLACK_BDD_API_TOKEN"]
        rtm_client = RTMClient(token=slack_token)

        rtm_client.on(event="message", callback=self.say_hello)
        rtm_client.start()

    def say_hello(self, **payload):
        self.event_trail.append(payload["data"])
