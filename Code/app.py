"""Main script, uses other modules to generate sentences."""
from flask import Flask, url_for
from dictogram import Dictogram
from markov import MarkovChain
from tokens import tokenize


app = Flask(__name__, static_url_path='/static')

# TODO: Initialize your histogram, hash table, or markov chain here.
# Any code placed here will run only once, when the server starts.
with open("data/pages.txt", "r") as file:
        text = file.read()
        words = tokenize(text)
        markov_chain = MarkovChain(words)

@app.route("/")
def home():
    """Route that returns a web page containing the generated text."""
    walk1 = markov_chain.walk()
    walk2 = markov_chain.walk()
    walk3 = markov_chain.walk()

    html = f"""
    <html>
    <head>
        <title>Sanderson Generator</title>
        <link rel="preconnect" href="https://fonts.googleapis.com">
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
        <link href="https://fonts.googleapis.com/css2?family=MedievalSharp&display=swap" rel="stylesheet">
        <style>
            body {{
                display: flex;
                justify-content: center;
                align-items: center;
                padding: 0;
                margin: 0;

                background-image: url('{url_for('static', filename='images/way_of_kings_cover.jpg')}');
                background-size: cover;
                background-position: center;
            }}
            .container {{
                padding: 4em;
                box-shadow: 2px 3px 20px black, 0 0 60px #8a4d0f inset;
                background: #fffef0;
                # filter: url(#wavy2);
            }}
            .generated-text {{
                font-family: "MedievalSharp", cursive;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>From the desk of Brandon Sanderson:</h1>
            <div class="generated-text">
                <p>{walk1}</p>
            </div>
            <div class="generated-text">
                <p>{walk2}</p>
            </div>
            <div class="generated-text">
                <p>{walk3}</p>
            </div>
        </div>
    </body>
    </html>
    """
    return html


if __name__ == "__main__":
    """To run the Flask server, execute `python app.py` in your terminal.
       To learn more about Flask's DEBUG mode, visit
       https://flask.palletsprojects.com/en/2.0.x/server/#in-code"""
    app.run(debug=True)
