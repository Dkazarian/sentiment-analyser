#!/usr/bin/python

#Uso: ./run_analyser.py "texto" -debug

import sys
from analyser.analyser import Analyser
from spell_checker.spell_checker import SpellChecker
from analyser.dummy_classifier import DummyClassifier
from analyser.redis_classifier import RedisClassifier

next_is_textfile = False
debug = False
text = None

for arg in sys.argv[1:]:
  if next_is_textfile:
    text = file(arg).read()
    next_is_textfile = False
  elif arg=="-debug":
    debug = True
  elif arg == "-f":
    next_is_textfile = True
  elif not text:
    text = arg

sc = SpellChecker()
#cl = DummyClassifier(sc)
cl = RedisClassifier(sc)
an = Analyser(cl, debug)
result = an.process(text)
print "%s (%s)" % ("Positivo" if result > 0 else "Negativo" if result < 0 else "Neutro", result)
