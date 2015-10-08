from db_collection import DbCollection
from models.d_word import DWord

class DWords(DbCollection):
  collection = None

  @classmethod
  def collection_name(self):
    return "d_words"

  @classmethod
  def find_word(self, word):
    database_word = self.find_one({"word": word})
    if database_word:
      return DWord(word, database_word.get("occurrences"))
    else:
      return None

  @classmethod
  def most_common_known_word(self, words):
    words = list(words)
    result = self.get_collection().find({"word": { "$in": words } } ).sort("occurrences", -1)
    if result.count() > 0:
      return result.next().get("word")
    else:
      None