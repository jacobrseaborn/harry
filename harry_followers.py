from flask import Flask
from flask import request
from flask import render_template
import stringComparison


import instaloader

app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template("index.html") # this should be the name of your html file

@app.route('/', methods=['POST'])
def my_form_post():
    L = instaloader.Instaloader()

    profile = instaloader.Profile.from_username(L.context, "harry_.wilkins")
    return "<h1>" + profile.followers + "</h1>"

if __name__ == '__main__':
    app.run()
