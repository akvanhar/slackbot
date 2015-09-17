import os
import time
import random
from slackclient import SlackClient

DO_ALY_CHAN = "D0AQXL0CX"

possible_replies = {
	'wine': "I'd like some too!",
	'beer': "Hook an octopus up!",
	'cocktail': "My favorite cocktail is a dark and stormy",
	"stress": "Hang in there.",
	"stressful": "It's going to be okay. Let's have a glass of wine.",
	"stressed": "You got this.",
	"picture": "Here's one of me! http://i.imgur.com/AICvMCj.jpg",
	"silly": ["http://giphy.com/gifs/pixel-art-octopus-PxdWYostrUcz6", 
			  "http://giphy.com/gifs/lol-octopus-hehehe-ZW9ufudBCnqyk",
			  "http://giphy.com/gifs/funny-banana-ISaEiQgQ6F81a"],
	"5:00": "It's beer-o-clock!",
	"5:30": "It's beer-o-clock!",
}

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
						self.reply(message, DO_ALY_CHAN)
					if 'wine' in message:
						channel = evt.get('channel')
						self.reply(message, DO_ALY_CHAN)
					if 'beer' in message:
						channel = evt.get('channel')
						self.reply(message, DO_ALY_CHAN)
					if 'cocktail' in message:
						channel = evt.get('channel')
						self.reply(message, DO_ALY_CHAN)
				time.sleep(1)

	def reply(self, message, channel):
		# when drunkoctopus is mentioned, return a message
		
		if "going home" in message:
			reply = "It's beer-o-clock!"
		
		elif "I'll miss you" in message:
			reply = "Awwww. You guys are the best."
		
		else: 
			words_in_message = message.split(' ')
			print words_in_message
			for word in words_in_message:
				print word
				reply = possible_replies.get(word)
				print reply
				if reply:
					if type(reply) is list:
						reply = random.choice(reply)
						print reply
						break
					break
				else:
					reply = "Oh hi! Let's fight!"
		
		self.slack_client.rtm_send_message(channel, reply)



if __name__ == "__main__":
	
	TOKEN = os.environ['SLACK_BOT_TOKEN']
	drunkoctopus = slackbot(TOKEN)
	drunkoctopus.connect()
	drunkoctopus.get_events()