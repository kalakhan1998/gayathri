from chatterbot.trainers import ListTrainer
from chatterbot import chatBot
import os
bot = chatBot('Test')
conv = open('chattext','r').readlines()
bot.set_trainer(ListTrainer)
bot.train(conv)
while True:
	request = input('you: ')
	response = bot.get_response(request)
	print('Bot: ',response)
