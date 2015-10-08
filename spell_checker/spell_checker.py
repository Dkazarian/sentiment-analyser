import re, collections
from database_connection.d_words import DWords
from models.d_word import DWord

class SpellChecker:
  def __init__(self):
    self.NWORDS = collections.defaultdict(lambda: 1)
    self.alphabet = 'abcdefghijklmnopqrstuvwxyz'

  def _extract_words(self, text): return re.findall('[a-z]+', text.lower())

  def train_with_occurrences(self, file_name):
    f = file(file_name)
    for word_oc in f:
      splitted = word_oc.split(" ")
      if(self.valid_training_group(splitted)):
        splitted_0 = splitted[0]
        splitted_1 = splitted[1]
        d_word = DWords.find_word(splitted_0) or DWord(splitted_0, occurrences=0)
        d_word.occurrences += int(splitted_1)
        DWords.insert(d_word.to_h())

  def valid_training_group(self, group):
    return len(group) == 2 and type(group[0]) is str and self.int_parsable(group[1])

  def int_parsable(self, num):
    try:
      int(num)
      return True
    except ValueError:
      return False

  def train(self, file_name):
    features = self._extract_words(file(file_name).read())
    model = collections.defaultdict(lambda: 1)
    for f in features:
        model[f] += 1
    for word in model:
      DWords.insert(DWord(word, occurrences=model[word]).to_h())

  def edits1(self, word):
    splits     = [(word[:i], word[i:]) for i in range(len(word) + 1)]
    deletes    = [a + b[1:] for a, b in splits if b]
    transposes = [a + b[1] + b[0] + b[2:] for a, b in splits if len(b)>1]
    replaces   = [a + c + b[1:] for a, b in splits for c in self.alphabet if b]
    inserts    = [a + c + b     for a, b in splits for c in self.alphabet]
    return set(deletes + transposes + replaces + inserts)

  def known_edits2(self, word):
    return set(e2 for e1 in self.edits1(word) for e2 in self.edits1(e1) if DWords.find_word(e2))

  def known(self, words): return set(w for w in words if DWords.find_word(w))

  def correct(self, word):
    candidates = self.known([word]) or self.known(self.edits1(word)) or self.known_edits2(word) or [word]
    return max(candidates, key=lambda word: self.d_word_occurrences(word))

  def edits2(self, edits_1):
    return set(e2 for e1 in edits_1 for e2 in self.edits1(e1))

  def correct2(self, word):
    edits_1 = self.edits1(word)
    return self.known([word]) or DWords.most_common_known_word(edits_1) or DWords.most_common_known_word(self.edits2(edits_1)) or word

  def flatten(self, l):
    return [item for sublist in l for item in sublist]

  def d_word_occurrences(self, word):
    d_word = DWords.find_word(word)
    if d_word is None:
      return 1
    else:
      return d_word.occurrences

  def reject_by_rules(self, words):
    wrongs = ['mv', 'np', 'nb']
    not_rejected = []
    for word in words:
      if(not any(m for wrong in wrongs for m in [re.search(wrong, word)])):
        not_rejected.append(word)
    return not_rejected



# spell_checker = SpellChecker()
# spell_checker.train_with_occurrences(file("spell_checker/training_files/words_and_occurrences_small.txt").read())

# print spell_checker.correct("hla")
# print spell_checker.correct("hlay")