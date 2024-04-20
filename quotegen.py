from flask import Flask, render_template, redirect, url_for, request
import random

app = Flask(__name__)

quotes = [
    "The only way to do great work is to love what you do. – Steve Jobs",
    "Innovation distinguishes between a leader and a follower. – Steve Jobs",
    "Your time is limited, don’t waste it living someone else’s life. – Steve Jobs",
    "Stay hungry, stay foolish. – Steve Jobs",
    "Don’t let the noise of other’s opinions drown out your own inner voice. – Steve Jobs",
    "The road to success and the road to failure are almost exactly the same. – Colin R. Davis",
    "Success usually comes to those who are too busy to be looking for it. – Henry David Thoreau",
    "Opportunities don't happen. You create them. – Chris Grosser",
    "Don't be afraid to give up the good to go for the great. – John D. Rockefeller",
    "I find that the harder I work, the more luck I seem to have. – Thomas Jefferson",
    "Success is not the key to happiness. Happiness is the key to success. If you love what you are doing, you will be successful. – Albert Schweitzer",
    "The only limit to our realization of tomorrow will be our doubts of today. – Franklin D. Roosevelt",
    "You miss 100% of the shots you don't take. – Wayne Gretzky",
    "The best time to plant a tree was 20 years ago. The second best time is now. – Chinese Proverb",
    "You don't have to be great to start, but you have to start to be great. – Zig Ziglar"
]

@app.route('/')
def main():
    return render_template('quotes.html')

@app.route('/generate')
def generate_quotes():
    res = random.choice(quotes)
    return render_template('quotes.html', result=res)

@app.route('/submit', methods=['POST'])
def generate():
    res = random.choice(quotes)
    return render_template('quotes.html', result=res)

if __name__ == '__main__':
    app.run(debug=True)
