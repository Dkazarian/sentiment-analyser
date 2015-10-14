from pymongo import MongoClient;

class DatabaseConnector:
  host = "localhost"
  current_instance = None

  def __init__(self, host, port, db_name):
    self.init_client(host, port, db_name)
    self.init_db(db_name)

  @classmethod
  def init_client(self, host, port):
    raise NotImplementedError

  @classmethod
  def init_db(self, db_name):
    raise NotImplementedError

  @classmethod
  def current(self):
    if self.current_instance is None:
      self.current_instance = self(self.host, self.port, self.db_name)
    return self.current_instance