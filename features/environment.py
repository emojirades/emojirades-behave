import os
import shutil
from time import sleep

from behave import fixture, use_fixture

from bot.dummy import Dummy
from bot.rtm_client import BddRTMClient


def get_from_root(path):
    return os.path.join(
        os.path.dirname(os.path.realpath(__file__)),
        "..",
        path
    )


def get_file_path(env_name):
    return get_from_root(os.environ[env_name])


SCORE_FILE_PATH = get_file_path("SCORE_FILE")
STATE_FILE_PATH = get_file_path("STATE_FILE")


def bootstrap_emojirade_files():
    score_template = get_from_root("config/score.json.template")
    state_template = get_from_root("config/state.json.template")

    shutil.copy2(score_template, SCORE_FILE_PATH)
    shutil.copy2(state_template, STATE_FILE_PATH)


@fixture
def slack_rtm_client(context):
    context.slack_rtm_client = BddRTMClient()


def before_all(context):
    # TODO wait for emojirade to start instead of sleeping
    sleep(2)

    bootstrap_emojirade_files()
    use_fixture(slack_rtm_client, context)
    context.robbins_bot = Dummy(os.environ["ROBBINS_BOT_TOKEN"], "Robbins")
    context.dave_bot = Dummy(os.environ["DAVE_BOT_TOKEN"], "Dave")
    context.fendy_bot = Dummy(os.environ["FENDY_BOT_TOKEN"], "Fendy")


def after_all(context):
    context.slack_rtm_client.stop()
