from behave import when

from bot.config import Config
from bot.message_parser import MessageParser


def bot_message(bot, message):
    mp = MessageParser(Config())
    channel_id = "#bdd"
    bot.send_message(mp.with_message(message).uid_to_tag().parse(), channel_id)


@when('Robbins says "{message}"')
def robbins_says(context, message):
    bot_message(context.robbins_bot, message)


@when('Dave says "{message}"')
def dave_says(context, message):
    bot_message(context.dave_bot, message)


@when('Fendy says "{message}"')
def fendy_says(context, message):
    bot_message(context.fendy_bot, message)


@when('Emojirade says "{message}"')
def emojirade_says(context, message):
    bot_message(context.emojirade_bot, message)
