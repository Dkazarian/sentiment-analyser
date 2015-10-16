from models.s_word import SWord
from word_classifier import WordClassifier

class DummyClassifier(WordClassifier):

  def find_word(self, word_string):
    word_data = None

    if word_string == "bueno" or word_string == "bonito":
      word_data = SWord(word_string, polarity=1)
    elif word_string == "malo":
      word_data = SWord(word_string, polarity=-1)
    elif word_string == "no":
      word_data = SWord(word_string, modifier=-1)
    elif word_string == "muy":
      word_data = SWord(word_string, modifier=3)
    return word_data

  def new_word(self, word_string):
    return SWord(word_string)