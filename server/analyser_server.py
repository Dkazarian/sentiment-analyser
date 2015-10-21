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
# {
#   "classifier": ["redis"|"mongo"],
#   "debug": ["True" | "False"],
#   "sentences": [{"text": "the sentence to analyse", "user_info": "user relevant information"}],
#   "respond_to": url,
#   "sincr": ["True"] //blocks call
# }
def analyse():
  data = json.loads(json.dumps(request.get_json(force=True)))
  classifier = data.get("classifier")
  if(classifier != None and classifier != "mongo" and classifier != "redis"):
    classifier = None
  debug = data.get("debug") is not None
  sentences = data.get("sentences")
  url = data.get("respond_to")
  sincr = data.get("sincr") or False
  spellcheck =  data.get("spellcheck") is not None
  opts = {
    "classifier": classifier or "redis" or "mongo",
    "debug": debug or False,
    "spellcheck": spellcheck or False,
    "sentences": sentences or [],
    "respond_to": url or ""
  }

  print opts

  if sincr is False:
    thr = threading.Thread(target=AnalyserTask.perform, kwargs=opts)
    thr.start()
    return jsonify(
      info="Running with classifier: %s, spellcheck is %s and debug mode is %s." % ( opts["classifier"], ("on" if opts["spellcheck"] else "off"), ("on" if opts["debug"] else "off")) 
    )
  else:
    return jsonify(
      results=AnalyserTask.perform(**opts)
    )

if __name__ == "__main__":
  app.run(debug=True)
