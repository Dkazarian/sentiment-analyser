class SWord:
  def __init__(self, word, polarity = None, modifier = None):
    self.word = word
    self.polarity = polarity
    self.modifier = modifier

  def has_polarity(self):
    return self.polarity is not None

  def is_modifier(self):
    return self.modifier is not None