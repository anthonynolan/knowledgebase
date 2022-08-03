#!/usr/bin/env python3

from flask import Flask, render_template, request, redirect, url_for
from write_db import export_data

from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def hello_world():
    return render_template("index.html", items=db.keys())

@app.route("/pages/<name>")
def get_page(name=None):
    page_content = db[name]
    return render_template('content_template.html', page_content=page_content)

@app.route("/new_item")
def new_item():
    return render_template('new_item.html')
    
@app.route("/put_new_item", methods=["POST"])
def put_new_item():
    name = request.form['name']
    content = request.form['content']
    global db
    db[name] = content
    print(db)
    export_data(db)
    return redirect('/')

@app.route('/items')
def get_items():
    return db

import pickle

with open('data/db.pkl', 'rb') as f:
    db = pickle.load(f)
