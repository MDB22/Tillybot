import re

class Tillybot():

	def __init__(self):
		vocab_file = open('resources/vocabulary.txt')
		vocabulary = vocab_file.read()
		self.vocabulary = vocabulary.split()

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
		pass

	def respond(self, message_text):
		pass
