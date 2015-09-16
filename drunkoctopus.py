import os
import time
from slackclient import SlackClient


DO_ALY_CHAN = "D0AQXL0CX"

# sc = SlackClient(TOKEN)

# From: https://medium.com/@julianmartinez/how-to-write-a-slack-bot-end-to-end-d6a8542c854b
# greeting = "Hello elevensies!\nLet's have some wine!"
# print sc.api_call("chat.postMessage",
# 	              as_user = True,
# 	              channel = DO_ALY_CHAN,
# 	              text = greeting)

# while True:
# 	new_evts = sc.rtm_read()
# 	for evt in new_evts:
# 		print evt
# 		if "type" in evt:
# 			if evt["type"] == "message" and "text" in evt:
# 				message = evt["text"]
# 		time.sleep(3)


# if sc.rtm_connect():
# 	while True:
# 		print sc.rtm_read()
# 		time.sleep(1)
# else:
# 	print "Connection failed, invalid token?"

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
		# Is drunkoctopus mentioned?

		while True:
			new_evts = self.slack_client.rtm_read()
			for evt in new_evts:
				print evt
				if evt.get('type') == 'message':
					message = evt.get('text')
					if 'drunkoctopus' in message:
						channel = evt.get('channel')
						self.reply(message, channel)
				time.sleep(3)

	def reply(self, message, channel):
		# when drunkoctopus is mentioned, return a message

		if message in ['stress', 'stressed', 'stressful']:
			reply = "It's going to be okay. Let's have some wine!"
			self.slack_client.rtm_send_message(channel, reply)
		
		elif message in ['5:00', '5:30', "I'm going home"]:
			reply = "It's beer-o-clock!"
			self.slack_client.rtm_send_message(channel, reply)

		else:
			reply = "Oh hi!"
			self.slack_client.rtm_send_message(channel, reply)



if __name__ == "__main__":
	
	TOKEN = os.environ['SLACK_BOT_TOKEN']
	drunkoctopus = slackbot(TOKEN)
	drunkoctopus.connect()
	drunkoctopus.get_events()