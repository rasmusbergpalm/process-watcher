import os

from slacker import Slacker

client = Slacker(os.environ['SLACK_TOKEN'])


def send(channel=None, process=None, subject_format='{executable} process {pid} ended'):
    client.chat.post_message(channel, subject_format.format(**process.__dict__), username='Process notifier')
