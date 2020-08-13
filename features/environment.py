import os

from behave import fixture, use_fixture

from bot.dummy import Dummy
from bot.rtm_client import BddRTMClient


@fixture
def slack_rtm_client(context):
    context.slack_rtm_client = BddRTMClient()


def before_all(context):
    use_fixture(slack_rtm_client, context)
    context.robbins_bot = Dummy(os.environ.get("ROBBINS_BOT_TOKEN", None), "Robbins")


def after_all(context):
    context.slack_rtm_client.stop()
