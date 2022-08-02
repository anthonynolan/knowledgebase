#!/usr/bin/env python3

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html", items=db.keys())

@app.route("/pages/<name>")
def get_page(name=None):
    page_content = db[name]
    return render_template('content_template.html', page_content=page_content)


import pickle

with open('data/db.pkl', 'rb') as f:
    db = pickle.load(f)

print(db)