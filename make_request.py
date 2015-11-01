#!/usr/bin/python
import sys
import requests
import json
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/post_response", methods=['POST'])
def post_response():
  print "got an answer!"
  data = json.loads(json.dumps(request.get_json(force=True)))
  print data


if __name__ == "__main__":
  requests.post("http://127.0.0.1:5000/analyse", headers={'Content-Type': 'application/json'}, data=json.dumps({'classifier': 'redis', 'respond_to': "http://127.0.0.1:5001/post_response", 'sentences': [{"text": "la comida es buena", "user_info": 1}, {"text": "la comida es fea", "user_info": 2}]}))
  app.run(port=5001)


