from redis_connector import RedisConnector
import json

class RedisConnection:
  @classmethod
  def db(self):
    return RedisConnector.current().db

  @classmethod
  def insert(self, key, item):
    self.db().set(key, json.dumps(item))

  @classmethod
  def find_one(self, key):
    result = self.db().get(key)
    if result is not None:
      return json.loads(result)
    else:
      return None
