import os
import time
from slackclient import SlackClient


DO_ALY_CHAN = "D0AQXL0CX"

class slackbot(object):
	# a class for fun slackbots

	def __init__(self, token):
		self.token = token
		self.slack_client = None

	def connect(self):
		# setup the SlackClient and connect to the RTM API

		self.slack_client = SlackClient(self.token)
		self.slack_client.rtm_connect()

	def get_events(self):
		# get all events from the RTM API
		# Is drunkoctopus or a keyword mentioned?

		while True:
			new_evts = self.slack_client.rtm_read()
			for evt in new_evts:
				print evt
				if evt.get('type') == 'message':
					message = evt.get('text')
					if 'drunkoctopus' in message:
						channel = evt.get('channel')
						self.reply(message, channel)
					if 'wine' in message:
						channel = evt.get('channel')
						self.reply(message, channel)
					if 'beer' in message:
						channel = evt.get('channel')
						self.reply(message, channel)
					if 'cocktail\*' in message:
						channel = evt.get('channel')
						self.reply(message, channel)
				time.sleep(3)

	def reply(self, message, channel):
		# when drunkoctopus is mentioned, return a message

		if ('stress' in message) or ('stressed' in message) or ('stressful' in message):
			reply = "It's going to be okay. Let's have some wine!"
			self.slack_client.rtm_send_message(channel, reply)
		
		elif ('5:00' in message) or ('5:30' in message) or ("I'm going home" in message):
			reply = "It's beer-o-clock!"
			self.slack_client.rtm_send_message(channel, reply)

		elif ('wine' in message) or ('beer' in message) or ('cocktail' in message):
			reply = "I'd like some, please!"
			self.slack_client.rtm_send_message(channel, reply)
		elif 'picture' in message:
			reply = "Sure! Here's a picture of me at a bar. http://i.imgur.com/AICvMCj.jpg"

		else:
			reply = "Oh hi!"
			self.slack_client.rtm_send_message(channel, reply)



if __name__ == "__main__":
	
	TOKEN = os.environ['SLACK_BOT_TOKEN']
	drunkoctopus = slackbot(TOKEN)
	drunkoctopus.connect()
	drunkoctopus.get_events()