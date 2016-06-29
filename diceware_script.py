from random import randint
from words import dictionary
import json

words = 4

dice_pass = {
	"password" : []
}

def make_word():
	word_in_numbers = ""
	for roll in range (0,5):
		number = str(randint(1,6))
		word_in_numbers = word_in_numbers + number
	word_in_numbers = word_in_numbers
	word = dictionary[word_in_numbers]
	return (word)

def make_password(length):
	password = ""
	for x in range(length):
		word = make_word()
		dice_pass["password"].append(word)
	print (dice_pass)	




run =  make_password(words)

#print (json.dumps(d))