"""Main script, uses other modules to generate sentences."""
from flask import Flask, request, render_template, redirect
from random_word import random_word
from histogram import histogram
from markov_chain import MarkovChain
from twitter import tweet  # Import the tweet function

app = Flask(__name__)

# TODO: Initialize your histogram, hash table, or markov chain here.
# Any code placed here will run only once, when the server starts.
histogram = histogram('data/metamorphosis.txt')
word_list = list(histogram.keys())
markov_chain = MarkovChain(word_list)

@app.route("/")
def home():
    """Route that returns a web page containing the generated text."""
    sentence = markov_chain.generate_sentence()
    return render_template('index.html', sentence=sentence)

@app.route('/tweet', methods=['POST'])
def tweet_route():
    status = request.form['sentence']
    tweet(status)  # Call the tweet function to send the tweet
    return redirect('/')

if __name__ == "__main__":
    """To run the Flask server, execute `python app.py` in your terminal.
       To learn more about Flask's DEBUG mode, visit
       https://flask.palletsprojects.com/en/2.0.x/server/#in-code"""
    app.run(debug=True)