#!/usr/bin/python
# coding: UTF-8 
from pdb import set_trace as bp
from pattern.es import parsetree
from math import fabs
import logging
import sys

class Analyser(object):

    def __init__(self, classifier, debug = False):
      self.classifier = classifier
      self.MODIFIER_WINDOW = 5
      self.__log_setup(debug)
      return

    def process(self, text):

      sentences = self.parse(text)
      text_value = 0

      for sentence in sentences:
        sentence_value = 0
        self.clear_modifiers()
        neutral_skipped = 0
        for s_word in sentence["words"]:  
          if s_word.has_polarity() and not self.ignore_word(s_word):
            if neutral_skipped > self.MODIFIER_WINDOW or not s_word.is_neutral():
              sentence_value += self.apply_modifiers(s_word)
              self.clear_modifiers() 
              neutral_skipped = 0          
            elif s_word.is_neutral():
              neutral_skipped+=1
          elif s_word.is_modifier():
            self.add_modifier(s_word)
          
          self.__log_step(s_word, sentence_value)     
        text_value += sentence_value
        self.logger.debug("\n\"%s\"", sentence["string"])
        self.logger.debug("\nTotal oración: %.2f\n\n", sentence_value)
      return text_value

    def parse(self, text):
      p_tree = parsetree(text, relations=True, lemmata=True)
      sentences = []
      for p_sentence in p_tree:
        sentence = []
        for p_word in p_sentence.words:
          sentence.append(self.classifier.classify(p_word))
        sentences.append({"words": sentence, "string": p_sentence.string})

      return sentences

    def ignore_word(self, s_word):
      return False#s_word.is_neutral() #or (s_word.extra.chunk \
      #  and not s_word.extra.chunk.role == "OBJ" \
      #  and (s_word.extra.chunk.role == "SBJ" or s_word.extra.chunk.type == "NP"))

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
      self.logger = logging.getLogger()
      self.logger.setLevel(logging.DEBUG)
      ch = logging.StreamHandler(sys.stdout)
      ch.setFormatter(logging.Formatter("\033[1;31m%s\033[1;0m" % '%(message)s'))
      if debug:
        ch.setLevel(logging.DEBUG)
      else:
        ch.setLevel(logging.ERROR)
      self.logger.addHandler(ch)

    def __log_step(self, s_word, sentence_value):
      self.logger.debug("===================")
      try:
        self.logger.debug("\"%s\" [%s] [%s] [%s] [%s]", 
          s_word.extra.string, 
          s_word,
          s_word.extra.type, 
          s_word.extra.chunk.role if s_word.extra.chunk else None, 
          s_word.extra.chunk.type if s_word.extra.chunk else None)   
      except UnicodeEncodeError:
        self.logger.debug("\"%s\" [%s] [%s] [%s] [%s]", 
          s_word.extra.string, 
          s_word.polarity,
          s_word.extra.type, 
          s_word.extra.chunk.role if s_word.extra.chunk else None, 
          s_word.extra.chunk.type if s_word.extra.chunk else None)  
       
      self.logger.debug("Acumulado: %.2f", sentence_value)    

      try:
        self.logger.debug("Modificadores: %s", map(lambda x: str(x), self.modifiers))  
      except UnicodeEncodeError:
        self.logger.debug("Modificadores: %s", map(lambda x: x.modifier, self.modifiers))

