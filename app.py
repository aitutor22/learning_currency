# http://flask.pocoo.org/
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
	return "Hello"

if __name__ == "__main__":
	app.run()