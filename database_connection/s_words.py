from db_collection import DbCollection

class SWords(DbCollection):
  collection = None

  @classmethod
  def collection_name(self):
    return "words"