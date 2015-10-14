from db_collection import DbCollection
from redis_connection import RedisConnection
from models.d_word import DWord

class DWords(RedisConnection):
  collection = None

  @classmethod
  def collection_name(self):
    return "d_words"

  @classmethod
  def find_word(self, word):
    database_word = self.find_one(word)
    if database_word:
      return DWord(word, occurrences= database_word.get("occurrences"), polarity= database_word.get("polarity"), modifier= database_word.get("modifier"))
    else:
      return None

  @classmethod
  def insert_word(self, d_word):
    self.insert(d_word.word, d_word.to_h())
    # if not (d_word.has_polarity() or d_word.is_modifier()):
    #   with open("polarity_pending.txt", "a") as f:
    #     f.write(d_word.word+" ")
    

  # @classmethod
  # def most_common_known_word(self, words):
  #   words = list(words)
  #   result = self.get_collection().find({"word": { "$in": words } } ).sort("occurrences", -1)
  #   if result.count() > 0:
  #     return result.next().get("word")
  #   else:
  #     None


  # @classmethod
  # def most_common_known_word(self, words):
  #   most_common_known_word = None
  #   print "Looking most common known word"
  #   for word in words:
  #     result = self.find_one(word)
  #     if(most_common_known_word is None and result is not None):
  #       most_common_known_word = result
  #     if(result is not None and most_common_known_word is not None):
  #         most_common_known_word = max([result, most_common_known_word], key=lambda w: w.get('occurrences'))
  #   if(most_common_known_word):
  #     return most_common_known_word.get('word')
  #   else:
  #     return None




