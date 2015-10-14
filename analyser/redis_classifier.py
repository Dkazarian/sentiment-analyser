from database_connection.d_words import DWords
from models.d_word import DWord

class RedisClassifier(object):
  def classify(self, word):
    #Se usaria el corrector si no encuentra nada.
    d_word = DWords.find_word(word.string.lower()) or DWords.find_word(word.lemma.lower()) or DWord(word.string.lower())
    d_word.extra = word 
    return d_word