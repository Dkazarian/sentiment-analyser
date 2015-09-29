class SWord:
  def __init__(self, word, polarity = None):
    self.word = word
    self.polarity = polarity

  def has_polarity(self):
    return self.polarity is not None