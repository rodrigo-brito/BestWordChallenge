#!/usr/bin/python
#-*- coding: utf-8 -*-
# Author: Rodrigo Ferreira de Brito (contato@rodrigobrito.net)
from database import Database
from word import Word

# Verify letters not used in process
# source [string] initial letters avaliable for construction
# word [string] word contructed
def unusedLetters (source, word):
	for letter in source:
		if letter in word:
			# For each ocorrency remove the letter
			source = source.replace(letter, "", 1)
			word = word.replace(letter, "", 1)
	return list(source)

# Search for words avaliable for the list construction
# lettersAvaliable [string] list of letters avaliable for the construction
# database [Database] database object with letters points and words
def searchWords(lettersAvaliable, database):
	wordsList = []
	# Verify each word avaliable
	for word in database.words:
		accept = True
		# Verifify letter avaliable
		for letter in word:
			# verify for each letter if exists in the source and if occurrence is greater than that available
			if letter not in lettersAvaliable or word.count( letter ) > lettersAvaliable.count( letter ) :
				accept = False
				break # stop de the loop to next word
		# If accepted, save the infornation in final list
		if accept:
			wordData = Word(word, database)
			wordData.saveSourceInformation( lettersAvaliable,  unusedLetters( lettersAvaliable, word ) )
			wordsList.append(wordData)
	return wordsList

# Load words and letters database
database = Database()

# Data input
inputUser = raw_input("Digite as letras disponíveis nesta jogada: ")
print inputUser

# Searching for words
listWordsAccepted = searchWords(inputUser.upper(), database)

# Sort list by points and size
listWordsAccepted.sort( key=lambda x: (x.points, 1.0/len(x.content)), reverse=True )

# Verify output array size
if listWordsAccepted:
	bestWord = listWordsAccepted[0]
	print bestWord.content, ", palavra tem ",bestWord.points, " pontos."
	if bestWord.unusedLetters:
		print "Sobraram: ", " ".join( bestWord.unusedLetters )
else:
	print "Nenhuma palavra disponível para as letras informadas."