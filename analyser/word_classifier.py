class WordClassifier(object):
  def __init__(self, spell_checker = None):
    self.spell_checker = spell_checker
    return

  def classify(self, p_word):
    w_string = p_word.string.lower()
    w_lemma = p_word.lemma.lower()

    word_data = self.find_word(w_string) or self.find_word(w_lemma)

    if word_data is None:
      word_data  = self.correct(w_string) or self.new_word(w_string)

    word_data.extra = p_word 

    return word_data 

  def find_word(self, word_string):
    return None 

  def correct(self, word_string):
    word_data = None 
    if self.spell_checker:
      word_data  = self.find_word(self.spell_checker.correct(word_string.encode("utf-8")))
      if word_data:
        word_data.word = word_data.word.decode("utf-8")
    return word_data 


  def new_word(self, word_string):
    return None

