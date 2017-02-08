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
	def saveSourceInformation(self, sourceLetters):
		self.sourceLetters = sourceLetters
		self.unusedLetters = self.getUnusedLetters( self.sourceLetters, self.content )

	# Verify letters not used in construction
	# source [string] initial letters avaliable for construction
	# word [string] final word contructed
	def getUnusedLetters (self, source, word):
		for letter in source:
			if letter in word:
				# For each ocorrency remove the letter
				source = source.replace(letter, "", 1)
				word = word.replace(letter, "", 1)
		return list(source)

	# Summarizes the word information
	# return [string] word information
	def __str__(self):
		output = self.content + ", palavra tem "  + str( self.points ) + " pontos."
		if self.unusedLetters:
			output += "\nSobraram: " + " ".join( self.unusedLetters )
		return output