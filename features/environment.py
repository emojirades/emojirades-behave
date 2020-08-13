from behave import fixture, use_fixture
from bot.rtm_client import BddRTMClient


@fixture
def slack_rtm_client(context):
    context.slack_rtm_client = BddRTMClient()


def before_all(context):
    use_fixture(slack_rtm_client, context)