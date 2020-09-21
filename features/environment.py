import os

from behave import fixture, use_fixture

from bot.dummy import Dummy
from bot.rtm_client import BddRTMClient


@fixture
def slack_rtm_client(context):
    context.slack_rtm_client = BddRTMClient()


def before_all(context):
    use_fixture(slack_rtm_client, context)
    context.robbins_bot = Dummy(os.environ["ROBBINS_BOT_TOKEN"], "Robbins")
    context.dave_bot = Dummy(os.environ["DAVE_BOT_TOKEN"], "Dave")
    context.fendy_bot = Dummy(os.environ["FENDY_BOT_TOKEN"], "Fendy")


def after_all(context):
    context.slack_rtm_client.stop()
