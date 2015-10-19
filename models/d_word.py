class DWord:
  def __init__(self, word, occurrences=None, polarity=None, modifier=None, extra=None):
    self.word = word
    if occurrences is None:
      self.occurrences = 1
    else:
      self.occurrences = int(occurrences)
    self.extra = extra or ''
    self.polarity = float(polarity) if polarity is not None else polarity
    self.modifier = float(modifier) if modifier is not None else modifier

  def to_h(self):
    h = { "word": self.word, "occurrences": str(self.occurrences)}
    if self.has_polarity():
      h["polarity"] = self.polarity
    elif self.is_modifier():
      h["modifier"] = self.modifier
    return h

  def has_polarity(self):
    return self.polarity is not None 

  def is_neutral(self):
    return self.has_polarity() and self.polarity==0

  def is_modifier(self):
    return self.modifier is not None

  
  def __str__(self):
    s = "\"%s\" %s: %.2f" % (self.word, "M" if self.is_modifier() else "P", self.modifier or self.polarity or 0)
    return s