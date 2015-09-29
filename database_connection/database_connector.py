from pymongo import MongoClient;

class DatabaseConnector:
  host = "localhost"
  port = 27017
  db_name = "sentiments_development"
  current_instance = None

  def __init__(self, host, port, db_name):
    self.client = MongoClient(host, port)
    self.db = self.client[db_name]

  @classmethod
  def current(self):
    if self.current_instance is None:
      self.current_instance = self(self.host, self.port, self.db_name)
    return self.current_instance