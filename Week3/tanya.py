# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 13:55:17 2019

@author: gordon.garisch
"""

from flask import Flask

app = Flask(__name__)

@app.route("/Tanya", methods=["GET"])
def hello_world():
    return "Lief vir jou!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
