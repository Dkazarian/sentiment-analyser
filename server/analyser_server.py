#!/usr/bin/python
# coding: UTF-8
import sys
from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

@app.route("/", methods=['GET'])
def index():
  return render_template("index.html")

@app.route("/info.json", methods=['GET'])
def info():
  return jsonify(
    version="1.0",
    year="2015",
    authors=[
      "Pablo Fernández",
      "Daniela Kazarián",
      "Aldana Laura Quintana Munilla",
      "Ariel Umansky"
    ]
  )

@app.route("/analyse", methods=['POST'])
def analyse():
  classifier = request.form.get("classifier")
  if(classifier != None and classifier != "mongo" and classifier != "redis"):
    classifier = None
  debug = request.form.get("debug") is not None
  opts = {
    "classifier": classifier or "redis" or "mongo",
    "debug": debug or False
  }

  return jsonify(
    info="Running with classifier: " +
    opts["classifier"] + " and debug mode is " +
    ("on" if opts["debug"] else "off") + "."
  )

if __name__ == "__main__":
  app.run()