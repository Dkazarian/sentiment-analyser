class SWord:
  def __init__(self, word, polarity = None, modifier = None):
    self.word = word
    self.polarity = polarity
    self.modifier = modifier

  def has_polarity(self):
    return self.polarity is not None

  def is_modifier(self):
    return self.modifier is not None

  def __str__(self):
    if self.is_modifier():
      s = "%s \tmodifier: %s" % (self.word, self.modifier)
    else:
      s = "%s \tpolarity: %s" % (self.word, self.polarity)
    return s