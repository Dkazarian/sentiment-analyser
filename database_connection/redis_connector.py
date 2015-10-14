import redis
from database_connector import DatabaseConnector;

class RedisConnector(DatabaseConnector):
  host = "localhost"
  port = 6379
  db_name = 0
  current_instance = None
  client = None
  db = None

  @classmethod
  def init_client(self, host, port, db_name):
    self.client = redis.StrictRedis(host=host, port=port, db=db_name)

  @classmethod
  def init_db(self, db_name):
    self.db = self.client