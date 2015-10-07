#!/usr/bin/python
# coding: UTF-8 
#from pdb import set_trace as bp
from pattern.es import parsetree
from math import fabs
import logging
import sys

class Analyser(object):

    def __init__(self, classifier, debug = False):
      self.classifier = classifier
      self.__log_setup(debug)
      return

    def process(self, text):

      sentences = self.parse(text)
      text_value = 0

      for sentence in sentences:
        sentence_value = 0
        self.clear_modifiers()
        for s_word in sentence:  
          self.logger.debug(s_word)         
          if s_word.has_polarity():
            sentence_value += self.apply_modifiers(s_word)
            self.clear_modifiers()           
          elif s_word.is_modifier():
            self.add_modifier(s_word)

        text_value += sentence_value

      return text_value

    def parse(self, text):
      p_tree = parsetree(text, relations=True, lemmata=True)
      sentences = []
      for p_sentence in p_tree:
        sentence = []
        for p_word in p_sentence.words:
          sentence.append(self.classifier.classify(p_word))
        sentences.append(sentence)
      return sentences


    def add_modifier(self, modifier):
      self.modifiers.append(modifier)

    def apply_modifiers(self, s_word):
      word_value = s_word.polarity

      if self.modifiers:
        word_value *= self.modifiers[0].modifier
        for modifier in self.modifiers[1:]:
          word_value *= abs(modifier.modifier)
      return word_value
           
    def clear_modifiers(self):
      self.modifiers = []


    def __log_setup(self, debug):
      print debug
      self.logger = logging.getLogger()
      self.logger.setLevel(logging.DEBUG)
      ch = logging.StreamHandler(sys.stdout)
      ch.setFormatter(logging.Formatter("\033[1;31m%s\033[1;0m" % '%(message)s'))
      if debug:
        ch.setLevel(logging.DEBUG)
      else:
        ch.setLevel(logging.ERROR)
      self.logger.addHandler(ch)
