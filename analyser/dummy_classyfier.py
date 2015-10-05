class DummyClassifier(object):

  def classify(self, word):
    if word.lemma == "bueno" or word.lemma == "bonito":
      word_data = {'word': word.string, 'value': 1}
    elif word.lemma == "malo":
      word_data = {'word': word.string, 'value': -1}
    elif word.string == "no":
      word_data = {'word': word.string, 'mod':  -1}
    elif word.string == "muy":
      word_data = {'word': word.string, 'mod':  3}
    else:
      word_data = {'word': word.string}
    return word_data
