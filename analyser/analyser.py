#!/usr/bin/python
# coding: UTF-8 
from pdb import set_trace as bp
from pattern.es import parsetree
import logging
import sys
from math import fabs

class Analyser(object):

    def __init__(self):
  
      self.__log_setup()
      self.__db_setup()
      return

    def process(self, text):
      tree = parsetree(text, relations=True, lemmata=True)
      self.logger.debug("TREE: %s\n", tree)
      value = 0

      #TODO: Actualmente no tiene en cuenta la jerarquía.
      # - Agregar sentence_value y chunk_value
      # - Un modificador puede afectar todo un chunk
      # - En algunas oraciones el objeto directo me lo tira afuera del predicado. No se si es asi o es un error. Considerarlo y parchearlo.
      # - A veces un modificador de un chunk me queda adentro del anterior. Suponer que si un modificador es la última palabra del chunk éste afecta al siguiente.
      # - Ver cómo stackear modifiers (por ahora los estoy multiplicando entre sí)
      # - Integrar con Mongo y cargar palabras del excel

      for sentence in tree:
        self.reset_modifier()

        for chunk in sentence.chunks:
          
          #self.logger.debug("CHUNK %s", repr([chunk.type, chunk.relation, chunk.words])) 
          
          for word in chunk.words:
            word_data = self.classify(word)
            
            if self.word_has_value(word_data):
              value += self.apply_modifier(word_data)
              self.reset_modifier()
           
            elif self.word_is_modifier(word_data):
              self.set_modifier(self.word_mod(word_data))
    
            self.logger.debug("acum: %s, next_mod: %s\n", value, self.current_mod)

      return value


    def classify(self, word):
      #TODO: Obtener de mongo
      if word.lemma == "bueno" or word.lemma == "bonito":
        word_data = {'word': word.string, 'value': 1}
      elif word.lemma == "malo":
        word_data = {'word': word.string, 'value': -1}
      elif word.string == "no":
        word_data = {'word': word.string, 'mod':  -1}
      elif word.string == "muy":
        word_data = {'word': word.string, 'mod':  3}
      else:
        word_data = {'word': word.string}

      self.logger.debug("\'%s\' value: %s mod: %s", word.string, self.word_value(word_data), self.word_mod(word_data))  

      return word_data

    def set_modifier(self, modifier):
      if self.current_mod!=1:
        word_mod = fabs(modifier)
      self.current_mod *= modifier

    def modifier_present(self):
      return self.current_mod!=1

    def apply_modifier(self, word_data):
      return self.word_value(word_data)*self.current_mod 
           
    def reset_modifier(self):
      self.current_mod = 1

    def word_is_modifier(self, word_data):
      return self.word_mod(word_data)!= 1

    def word_has_value(self, word_data):
      return self.word_value(word_data)!=0

    def word_value(self, word_data):
      return word_data.get("value", 0)

    def word_mod(self, word_data):
      return word_data.get("mod", 1)

    def __log_setup(self):
      self.logger = logging.getLogger()
      self.logger.setLevel(logging.DEBUG)
      ch = logging.StreamHandler(sys.stdout)
      ch.setFormatter(logging.Formatter("\033[1;31m%s\033[1;0m" % '%(message)s'))
      ch.setLevel(logging.DEBUG)
      self.logger.addHandler(ch)


    def __db_setup(self):
      return




an = Analyser()
print an.process("La comida no es muy buena.")
