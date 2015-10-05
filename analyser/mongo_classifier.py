from database_connection.s_words import SWords
from models.s_word import SWord

class MongoClassifier(object):
  def classify(self, word):
    return SWords.find_word(word.lemma) or SWord(word.string)
