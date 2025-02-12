"""Main script, uses other modules to generate sentences."""
from flask import Flask
from dictogram import Dictogram
import re


app = Flask(__name__)

# TODO: Initialize your histogram, hash table, or markov chain here.
# Any code placed here will run only once, when the server starts.
with open("sherlock_holmes.txt", "r") as file:
        text = file.read().lower()
        words = re.split(r"\W+", text)

dictogram = Dictogram(words)

@app.route("/")
def home():
    """Route that returns a web page containing the generated text."""
    rand_word = dictogram.sample()
    return f"<p>{rand_word}</p>"


if __name__ == "__main__":
    """To run the Flask server, execute `python app.py` in your terminal.
       To learn more about Flask's DEBUG mode, visit
       https://flask.palletsprojects.com/en/2.0.x/server/#in-code"""
    app.run(debug=True)
