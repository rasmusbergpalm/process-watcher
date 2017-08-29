import os

from slacker import Slacker

client = Slacker(os.environ['SLACK_TOKEN'])


def send(channel=None, process=None, subject_format='{pid} ended'):
    client.chat.post_message(channel, subject_format.format(pid=process), username='Process notifier')
