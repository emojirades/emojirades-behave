import os
from slack import RTMClient
import threading

class BddRTMClient:

    event_trail = []

    def __init__(self):
        slack_token = os.environ["SLACK_BDD_API_TOKEN"]
        self.rtm_client = RTMClient(token=slack_token)

        self.rtm_client.on(event="message", callback=self.listen)
        self.rtm_thread = threading.Thread(name="rtm_client", target=self.rtm_client.start)
        self.rtm_thread.start()

    def listen(self, **payload):
        self.event_trail.append(payload["data"])

    def stop(self):
        self.rtm_client.stop()
