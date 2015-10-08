class DWord:
  def __init__(self, word, occurrences=None, extra=None):
    self.word = word
    if occurrences is None:
      self.occurrences = 1
    else:
      self.occurrences = occurrences
    self.extra = extra or ''

  def to_h(self):
    return { "word": self.word, "occurrences": str(self.occurrences), "extra": self.extra }
