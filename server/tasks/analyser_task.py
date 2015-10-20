from analyser.mongo_classifier import MongoClassifier
from analyser.redis_classifier import RedisClassifier
from analyser.analyser import Analyser
import requests
import json


class AnalyserTask:
  @classmethod
  def perform(self, classifier, debug, sentences, respond_to):
    if classifier == "redis":
      cl = RedisClassifier()
    else:
      cl = MongoClassifier()

    results = []

    an = Analyser(cl, debug)
    for sentence in sentences:
      result = {}
      result["text"] = sentence["text"]
      result["user_info"] = sentence["user_info"]
      result["result"] = an.process(sentence["text"])
      results.append(result)

    if len(respond_to) > 0:
      requests.post(respond_to, headers={'Content-Type': 'application/json'}, data=json.dumps(results))
    else:
      return results
