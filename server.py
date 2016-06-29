#secure & memorable passwords for everyone

import flask
from two1.wallet import Wallet
from two1.bitserv.flask import Payment
import yaml
import json

app = flask.Flask(__name__)
payment = Payment(app, Wallet())

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


@app.route('/make_password')
@payment.required(5000)
def make_password():
	length = request.args.get('text')
	password = ""
	for x in range(length):
		word = make_word()
		dice_pass["password"].append(word)
	return (dice_pass)


'''
@app.route('/manifest')
def manifest():
    """Provide the app manifest to the 21 crawler.
    """
    with open('./manifest.yaml', 'r') as f:
        manifest = yaml.load(f)
    return json.dumps(manifest)
'''

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)