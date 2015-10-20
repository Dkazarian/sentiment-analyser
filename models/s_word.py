class SWord:
  def __init__(self, word, polarity = None, modifier = None, extra = None):
    self.word = word
    self.polarity = polarity
    self.modifier = modifier
    self.extra = extra

  def has_polarity(self):
    return self.polarity is not None

  def is_modifier(self):
    return self.modifier is not None

  def is_neutral(self):
    return self.has_polarity() and self.polarity==0

  def __str__(self):
    s = "\"%s\" %s: %.2f" % (self.word, "M" if self.is_modifier() else "P", self.modifier or self.polarity or 0)
    return s
