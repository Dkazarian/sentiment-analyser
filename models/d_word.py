class DWord:
  def __init__(self, word, occurrences=None, polarity=None, modifier=None, extra=None):
    self.word = word
    if occurrences is None:
      self.occurrences = 1
    else:
      self.occurrences = occurrences
    self.extra = extra or ''
    self.polarity = polarity
    self.modifier = modifier

  def to_h(self):
    h = { "word": self.word, "occurrences": str(self.occurrences)}
    if self.has_polarity():
      h["polarity"] = self.polarity
    elif self.is_modifier():
      h["modifier"] = self.modifier
    return h

  def has_polarity(self):
    return self.polarity is not None

  def is_modifier(self):
    return self.modifier is not None