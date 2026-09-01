from flask import Flask, render_template
import random as rd

app = Flask(__name__)
@app.route("/")
def landingpage():
    return render_template("rqg.html")

@app.route("/randomquotegenerator", methods=["GET"])
def randomquotegenerator():
    quotes = ["The only true wisdom is in knowing you know nothing.", "In the middle of difficulty lies opportunity.", "The purpose of our lives is to be happy.",
          "Life is what happens when you're busy making other plans.", "It always seems impossible until it's done." ,"The unexamined life is not worth living.",
          "Be the change that you wish to see in the world.", "Spread love everywhere you go. Let no one ever come to you without leaving happier.", 
          "Do not go where the path may lead, go instead where there is no path and leave a trail.", 
          "The future belongs to those who believe in the beauty of their dreams."]
    
    random_quotes = rd.choice(quotes)
    return render_template("rqg.html", randomquote = random_quotes)













