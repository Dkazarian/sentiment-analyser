#!/usr/bin/python
# coding: UTF-8 
#from pdb import set_trace as bp
from pattern.es import parsetree
from math import fabs
from dummy_classyfier import DummyClassifier

class Analyser(object):

    def __init__(self, classifier):
      self.classifier = classifier
      return

    def process(self, text):

      sentences = self.parse(text)
      text_value = 0

      for sentence in sentences:
        sentence_value = 0
        self.clear_modifiers()
        for word in sentence:            
          if self.word_has_value(word):
            sentence_value += self.apply_modifiers(word)
            self.clear_modifiers()           
          elif self.word_is_modifier(word):
            self.add_modifier(word)

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

    def apply_modifiers(self, word_data):
      word_value = self.word_value(word_data)

      if self.modifiers:
        word_value *= self.word_mod(self.modifiers[0])
        for modifier in self.modifiers[1:]:
          word_value *= abs(self.word_mod(modifier))

      return word_value
           
    def clear_modifiers(self):
      self.modifiers = []

    def word_is_modifier(self, word_data):
      return self.word_mod(word_data)!= 1

    def word_has_value(self, word_data):
      return self.word_value(word_data)!=0

    def word_value(self, word_data):
      return word_data.get("value", 0)

    def word_mod(self, word_data):
      return word_data.get("mod", 1)

      

if __name__ == '__main__':

  cl = DummyClassifier()
  an = Analyser(cl)
  print an.process("La comida no es muy buena.")
