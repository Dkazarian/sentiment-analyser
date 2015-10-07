from database_connector import DatabaseConnector
class DbCollection:
  collection = None

  @classmethod
  def db(self):
    return DatabaseConnector.current().db

  @classmethod
  def collection_name(self):
    raise NotImplementedError

  @classmethod
  def get_collection(self):
    if self.collection is None:
      collection = self.db()[self.collection_name()]
    return collection

  @classmethod
  def insert(self, item):
    self.get_collection().insert(item)

  @classmethod
  def all(self):
    return self.get_collection().find()

  @classmethod
  def find_one(self, query):
    return self.get_collection().find_one(query)