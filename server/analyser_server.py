#!/usr/bin/python
# coding: UTF-8
import sys
from flask import Flask, render_template, request, jsonify
import threading
import json

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
  data = json.loads(json.dumps(request.get_json(force=True)))
  classifier = data.get("classifier")
  if(classifier != None and classifier != "mongo" and classifier != "redis"):
    classifier = None
  debug = data.get("debug") is not None
  sentences = data.get("sentences")
  url = data.get("respond_to")

  opts = {
    "classifier": classifier or "redis" or "mongo",
    "debug": debug or False,
    "sentences": sentences or [],
    "respond_to": url or ""
  }

  print opts

  thr = threading.Thread(target=AnalyserTask.perform, kwargs=opts)
  thr.start()

  return jsonify(
    info="Running with classifier: " +
    opts["classifier"] + " and debug mode is " +
    ("on" if opts["debug"] else "off") + "."
  )

if __name__ == "__main__":
  app.run()
