#!/usr/bin/python
import sys
import requests
import json

requests.post("http://127.0.0.1:5000/analyse", headers={'Content-Type': 'application/json'}, data=json.dumps({'classifier': 'mongo', 'sentences': [{"text": "la comida es buena", "user_info": 1}, {"text": "la comida es fea", "user_info": 2}]}))