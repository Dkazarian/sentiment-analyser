#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re, collections
from database_connection.d_words import DWords
from models.d_word import DWord

class SpellChecker:
  def __init__(self):
    self.NWORDS = collections.defaultdict(lambda: 1)
    self.alphabet = 'aábcdeéfghiíjklmnoópqrstuúvwxyz'


  def train_with_occurrences(self, file_name):
    f = file(file_name)
    for word_oc in f:
      splitted = word_oc.split(" ")
      if(self.valid_training_group(splitted)):
        splitted_0 = splitted[0]
        splitted_1 = splitted[1]
        d_word = DWords.find_word(splitted_0) or DWord(splitted_0, occurrences=0)
        d_word.occurrences += int(splitted_1)
        DWords.insert_word(d_word)

  def valid_training_group(self, group):
    return len(group) == 2 and type(group[0]) is str and self.int_parsable(group[1])

  def int_parsable(self, num):
    try:
      int(num)
      return True
    except ValueError:
      return False

  # def _extract_words(self, text): return re.findall('[a-z]+', text.lower())

  # def train(self, file_name):
  #   features = self._extract_words(file(file_name).read())
  #   model = collections.defaultdict(lambda: 1)
  #   for f in features:
  #       model[f] += 1
  #   for word in model:
  #     DWords.insert_word(DWord(word, occurrences=model[word]))

  def edits1(self, word):
    splits     = [(word[:i], word[i:]) for i in range(len(word) + 1)]
    deletes    = [a + b[1:] for a, b in splits if b]
    transposes = [a + b[1] + b[0] + b[2:] for a, b in splits if len(b)>1]
    replaces   = [a + c + b[1:] for a, b in splits for c in self.alphabet if b]
    inserts    = [a + c + b     for a, b in splits for c in self.alphabet]
    return self.reject_by_rules(set(deletes + replaces + inserts))

  def known_edits2(self, word):
    return set(e2 for e1 in self.edits1(word) for e2 in self.edits1(e1) if DWords.find_word(e2))

  def known(self, words): return set(w for w1 in words for w in [DWords.find_word(w1)] if w)

  def correct(self, word):
    candidates = self.known([word])
    if(len(candidates) is 0):
      edits_1 = self.edits1(word)
      candidates = self.known(edits_1) or self.known(self.edits2(edits_1)) or [DWord(word)]
    return max(candidates, key=lambda word: word.occurrences).word

  def edits2(self, edits_1):
    return set(e2 for e1 in edits_1 for e2 in self.edits1(e1))

  def reject_by_rules(self, words):
    wrongs = ['mv', 'np', 'nb']
    wrongs.extend(list(triple for l in self.alphabet for triple in ["".join([l,l,l])]))
    not_rejected = []
    for word in words:
      if(not any(m for wrong in wrongs for m in [re.search(wrong, word)])):
        not_rejected.append(word)
    return not_rejected



# spell_checker = SpellChecker()
# spell_checker.train_with_occurrences(file("spell_checker/training_files/words_and_occurrences_small.txt").read())

# print spell_checker.correct("hla")
# print spell_checker.correct("hlay")