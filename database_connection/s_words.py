from db_collection import DbCollection
from models.s_word import SWord

class SWords(DbCollection):
  collection = None

  @classmethod
  def collection_name(self):
    return "words"

  @classmethod
  def find_word(self, word):
    word_doc = self.find_one({"word": word})


    if word_doc: 
      s_word = SWord(word)
      polarity = word_doc.get("polarity")
      modifier = word_doc.get("modifier")
      if polarity:
        s_word.polarity = float(polarity)
      if modifier:
        s_word.modifier = float(modifier)
      return s_word
    else:
      return None
  


