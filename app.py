import os
from flask import Flask, render_template
from config import Config

app = Flask(__name__)

app.config.from_object(Config)

@app.route('/')
def hello():
    return "hello world"

@app.route("/template")
def template_view():
    return render_template("first.html")


if __name__=='__main__':
    app.run()