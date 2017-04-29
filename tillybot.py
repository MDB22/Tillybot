import re

class Tillybot():

	def __init__(self):
		vocab_file = open('resources/vocabulary.txt')
		vocabulary = vocab_file.read()
		self.vocabulary = vocabulary.split()
		self.responses = {
			"alien": "Aliens don't look like that!",
			"automatic": "If I drive an automaitc I just can't *feel* the car...",
			"spelling": "I don't care if you don't spell it that way, language is fluid.",
			"regardless": "I believe the correct word is 'irregardless'...",
			"pineapple": "Get that shit off my pizza."
		}

		self.keywords = []

	def itillianise(self, message_text):
		word_list = re.sub("[^\w]", " ",  message_text).split()
		message_text_new = ""
		
		for word in word_list:
			try:
				word_index = self.vocabulary.index(word)
				word_replacement = self.vocabulary[word_index+1]
			except ValueError:
				word_replacement = word
			message_text_new += word_replacement
			
			if word != word_list[len(word_list)-1]:
				message_text_new += " "
		
		message_text_new += "."
		return message_text_new

	def has_keywords(self, message_text):

		keywords = []

		for keyword in self.responses:
			if keyword in message_text:
				keywords.append(keyword)

		self.keywords = keywords

		return True if keywords else False

	def respond(self, message_text):
		return self.responses[self.keywords[0]]
