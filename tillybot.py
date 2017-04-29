class Tillybot():

	def __init__(self):
		self.responses = {
			"alien": "Aliens don't look like that!",
			"automatic": "I love manuals. If I drive an automatic I just can't *feel* the car...",
			"spell": "I don't care if you don't spell it that way, language is fluid.",
			"regardless": "I believe the correct word is 'irregardless'...",
			"pineapple": "Get that shit off my pizza."
		}

		self.keywords = []

	def itillianise(self, message_text):
		return message_text

	def has_keywords(self, message_text):

		keywords = []

		for keyword in self.responses:
			if keyword in message_text:
				keywords.append(keyword)

		self.keywords = keywords

		return True if keywords else False

	def respond(self, message_text):
		return self.responses[self.keywords[0]]