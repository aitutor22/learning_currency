# http://flask.pocoo.org/
import flask
from flask import Flask, jsonify, render_template
import requests

app = Flask(__name__)

@app.route("/")
def index():
	return render_template("index.html")

#returns latest currency
@app.route("/currency")
def currency():
	r = requests.get("http://api.fixer.io/latest").json()
	return jsonify(r)

@app.route("/changecurrency", methods=["POST"])
def change_currency():
	originalCurrency = flask.request.form["originalCurrency"].upper()
	newCurrency = flask.request.form["newCurrency"].upper()
	numberBags = int(flask.request.form["number"])
	price = float(flask.request.form["price"])

	params = {
		"base": originalCurrency
	}

	data = requests.get("http://api.fixer.io/latest", params=params).json()
	currency_rates = data["rates"]
	currency_rate_for_user = currency_rates[newCurrency]
	total_price = numberBags * price * currency_rate_for_user
	
	results = {
		"status": 200,
		"total_price": total_price
	}

	return jsonify(results)

	
	
	# currency_rate_for_user = 
	# return currency_rates


if __name__ == "__main__":
	app.run()

