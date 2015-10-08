from models.s_word import SWord
class DummyClassifier(object):

  def classify(self, word):
    if word.lemma == "bueno" or word.lemma == "bonito":
      word_data = SWord(word.string, polarity=1)
    elif word.lemma == "malo":
      word_data = SWord(word.string, polarity=-1)
    elif word.string == "no":
      word_data = SWord(word.string, modifier=-1)
    elif word.string == "muy":
      word_data = SWord(word.string, modifier=3)
    else:
      word_data = SWord(word.string, extra = word)
    return word_data
