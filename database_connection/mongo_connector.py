from pymongo import MongoClient;
from database_connector import DatabaseConnector;

class MongoConnector(DatabaseConnector):
  host = "localhost"
  port = 27017
  db_name = "sentiments_development"
  current_instance = None
  client = None
  db = None

  @classmethod
  def init_client(self, host, port):
    self.client = MongoClient(host, port)

  @classmethod
  def init_db(self, db_name):
    self.db = self.client[db_name]