#!/usr/bin/python
# coding: UTF-8 
from pdb import set_trace as bp
from pattern.es import parsetree
import logging
import sys
from math import fabs

class Analyser(object):

    def __init__(self):
  
      #Log
      self.logger = logging.getLogger()
      self.logger.setLevel(logging.DEBUG)
      ch = logging.StreamHandler(sys.stdout)
      ch.setFormatter(logging.Formatter("\033[1;31m%s\033[1;0m" % '%(message)s'))
      ch.setLevel(logging.DEBUG)
      self.logger.addHandler(ch)
      

      #TODO: Conectarse a mongo
      return

    def process(self, text):
      tree = self.parse(text)
      self.logger.debug("TREE: %s\n", tree)
      value = 0

      for sentence in tree:
        current_mod = 1
        for chunk in sentence.chunks:
          
          #self.logger.debug("CHUNK %s", repr([chunk.type, chunk.relation, chunk.words])) 
          
          for word in chunk.words:
            word_data = self.classify(word)
            word_value = word_data.get("value", 0)
            word_mod = word_data.get("mod", 1)
            self.logger.debug("\'%s\' value: %s mod: %s current_mod: %s", word.string, word_value, word_mod, current_mod)
            
            if word_value != 0:
              value += word_value*current_mod 
              current_mod = 1
           
            if word_mod != 1:
              if current_mod!=1:
                word_mod = fabs(word_mod)
              current_mod *= word_mod 
    
            self.logger.debug("acum: %s, next_mod: %s\n", value, current_mod)

      return value


    def parse(self, text):
      return parsetree(text, relations=True, lemmata=True)

    def classify(self, word):
      #TODO: Obtener de mongo
      if word.lemma == "bueno" or word.lemma == "bonito":
        return {'word': word.string, 'value': 1}
      elif word.lemma == "malo":
        return {'word': word.string, 'value': -1}
      elif word.string == "no":
        return {'word': word.string, 'mod':  -1}
      elif word.string == "muy":
        return {'word': word.string, 'mod':  3}
      else:
        return {'word': word.string}





#an = Analyser()
#print an.process("La comida no es muy buena, pero el lugar es muy pero muy bonito.")
