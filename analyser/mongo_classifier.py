from database_connection.s_words import SWords
from models.s_word import SWord

class MongoClassifier(object):
  def classify(self, word):
    s_word = SWords.find_word(word.string.lower()) or SWords.find_word(word.lemma.lower()) or SWord(word.string.lower())
    s_word.extra = word 
    return s_word