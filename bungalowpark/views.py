#import x

from flask import render_template
from bungalowpark import app

@app.route('/')
def home_page():
    return render_template("home.html")

@app.route("/bungalows/<bungalow_id>")
def single_bungalow_page(bungalow_id):
  return render_template("bungalow/single.html", bungalow_id=bungalow_id)

@app.route("/bungalows")
def archive_bungalow_page():
  return render_template("bungalow/archive.html")

