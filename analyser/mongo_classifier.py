from database_connection.s_words import SWords
from models.s_word import SWord
from word_classifier import WordClassifier

class MongoClassifier(WordClassifier):

  def find_word(self, word_string):
    return SWords.find_word(word_string)   

  def new_word(self, word_string):
    return SWord(word_string)