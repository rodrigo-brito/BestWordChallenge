# Author: Rodrigo Ferreira de Brito (contato@rodrigobrito.net)
import unicodedata
class Database:
	def __init__(self):
		# Dictionary for letters points
		self.letters = { "E": 1, "A" : 1, "I": 1, "O": 1, "N": 1, "R": 1, "T": 1, "L": 1, "S": 1, "U": 1, "W":2, "D":2, "G":2, "B": 3, "C": 3, "M": 3, "P": 3, "F": 4, "H": 4, "V": 4, "J": 8, "X":8, "Q": 10, "Z": 10 }
		# Load and fix words
		self.words = self.fixWords( self.loadWords('./files/words.txt') )

	# Fix words upscale and special characters
	# words [list] list of words avaliable
	# return [list] list of words fixed
	def fixWords(self, words):
		wordsFixed = []
		for word in words:
			wordFixed = unicodedata.normalize('NFKD', unicode(word, 'utf-8')).encode('ASCII', 'ignore')
			wordFixed = wordFixed.replace("\n", "")
			wordsFixed.append( wordFixed.upper() )
		return wordsFixed

	# Load a list of words from a file
	# fileName [string] file address to open
	# return [list] list of words
	def loadWords( self, fileName ):
		file = open( fileName )
		words = file.readlines()
		file.close()
		return words