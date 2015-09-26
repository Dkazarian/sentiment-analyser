import re, collections

class SpellChecker:
  def __init__(self):
    self.NWORDS = collections.defaultdict(lambda: 1)
    self.alphabet = 'abcdefghijklmnopqrstuvwxyz'

  def _extract_words(self, text): return re.findall('[a-z]+', text.lower())

  def train_with_occurrences(self, text):
    words_and_occurrences = text.split('\r\n')
    for word_oc in words_and_occurrences:
      splitted = word_oc.split(" ")
      self.NWORDS[splitted[0]] += int(splitted[1]) - 1

  def train(self, file_name):
    features = self._extract_words(file(file_name).read())
    model = collections.defaultdict(lambda: 1)
    for f in features:
        model[f] += 1
    self.NWORDS = model

  def edits1(self, word):
    splits     = [(word[:i], word[i:]) for i in range(len(word) + 1)]
    deletes    = [a + b[1:] for a, b in splits if b]
    transposes = [a + b[1] + b[0] + b[2:] for a, b in splits if len(b)>1]
    replaces   = [a + c + b[1:] for a, b in splits for c in self.alphabet if b]
    inserts    = [a + c + b     for a, b in splits for c in self.alphabet]
    return set(deletes + transposes + replaces + inserts)

  def known_edits2(self, word):
    return set(e2 for e1 in self.edits1(word) for e2 in self.edits1(e1) if e2 in self.NWORDS)

  def known(self, words): return set(w for w in words if w in self.NWORDS)

  def correct(self, word):
    candidates = self.known([word]) or self.known(self.edits1(word)) or self.known_edits2(word) or [word]
    return max(candidates, key=self.NWORDS.get)

# spell_checker = SpellChecker()
# spell_checker.train("training_files/words_and_occurrences_small.txt")

# print spell_checker.correct("hla")
# print spell_checker.correct("hlay")