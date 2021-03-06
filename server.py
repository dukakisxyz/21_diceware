#application spesific imports
import flask
from random import randint
from words import dictionary
from flask import request
import json

#21 imports
from two1.wallet import Wallet
from two1.bitserv.flask import Payment
import yaml

app = flask.Flask(__name__)
payment = Payment(app, Wallet())

@app.route('/')
@app.route('/make_password/')
@app.route('/make_password/<int:length>')
@payment.required(1000)
def make_password(length = None):
	length = length

	if length == None:
		length = 5
	elif length > 16:
		length = 16

	dice_pass = {
	"password" : []
}
	password = ""
	for x in range(length):
		word_in_numbers = ""
		for roll in range (0,5):
			number = str(randint(1,6))
			word_in_numbers = word_in_numbers + number
		word_in_numbers = word_in_numbers
		word = dictionary[word_in_numbers]
		dice_pass["password"].append(word)
	return json.dumps(dice_pass)



if __name__ == "__main__":
    app.run(host=”::”, port=8000)
