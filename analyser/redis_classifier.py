from database_connection.d_words import DWords
from models.d_word import DWord
from spell_checker.spell_checker import SpellChecker
class RedisClassifier(object):

  def __init__(self):
    self.spell_checker = SpellChecker()
    return
    
  def classify(self, word):
    w_string = word.string.lower()
    w_lemma = word.lemma.lower()
    #Se usaria el corrector si no encuentra nada.
    d_word = DWords.find_word(w_string) or DWords.find_word(w_lemma) 
    if d_word is None:
      d_word = DWords.find_word(self.spell_checker.correct(w_string.encode("utf-8"))) or DWord(w_string)
      d_word.word = d_word.word.decode("utf-8")
    d_word.extra = word

    return d_word