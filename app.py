import os
from flask import Flask, json, render_template, jsonify
from config import Config

app = Flask(__name__)

app.config.from_object(Config)

@app.route('/')
def hello():
    return "hello world"

@app.route("/template")
def template_view():
    return render_template("first.html")

@app.route("/json")
def json_view():
    response = {
        "status" : True,
        "Data": {
            "some_data" : [1, 2, 3, 4]
        },
        "message" : "Response from JSON Endpoint."
    }
    return jsonify(response)

@app.route("/layout")
def layout():
    return render_template("index.html")



if __name__=='__main__':
    app.run()