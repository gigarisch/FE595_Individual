# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 13:55:17 2019

@author: gordon.garisch
"""

from flask import Flask

app = Flask(__name__)

@app.route("/hello", methods=["GET","POST"])
def hello_world():
    print("What should I print?")
    return "Hello, world!"

@app.route("/hello/<name>", methods=["GET"])
def hello_person(name):
    return "Hello, {}!".format(name)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
