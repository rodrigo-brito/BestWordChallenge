# Author: Rodrigo Ferreira de Brito (contato@rodrigobrito.net)
class Word:
	# Constructor
	# content [string] word content
	# database [Database] database of letters and words
	def __init__(self, content, database):
		self.content = content
		self.database = database
		self.points = self.getPoints()
		self.sourceLetters = ""
		self.unusedLetters = []

	# Get total points for the word content
	# return [int] total points
	def getPoints(self):
		points = 0
		for letter in self.content:
			points += self.database.letters[letter]
		return points

	# Save the aditional information from words
	# sourceLetters [string] avaliable letters for construct
	# unusedLetters [list] list of unused letters
	def saveSourceInformation(self, sourceLetters, unusedLetters):
		self.sourceLetters = sourceLetters
		self.unusedLetters = unusedLetters

	# Print the object information
	def __str__(self):
		unusedLetters = ''.join(self.unusedLetters)
		return self.content + " " + unusedLetters+ " " + str(self.points)