from database_connection.d_words import DWords
from models.d_word import DWord
from spell_checker.spell_checker import SpellChecker
from word_classifier import WordClassifier

class RedisClassifier(WordClassifier):

  def find_word(self, word_string):
    return DWords.find_word(word_string)   

  def new_word(self, word_string):
    return DWord(word_string)