#!/usr/bin/python

#Uso: ./run_analyser.py "texto" -debug

import sys
from analyser.analyser import Analyser
from spell_checker.spell_checker import SpellChecker
from analyser.dummy_classifier import DummyClassifier
from analyser.mongo_classifier import MongoClassifier
from analyser.redis_classifier import RedisClassifier

text = sys.argv[1]
debug = len(sys.argv) == 3 and sys.argv[2]=="-debug"


sc = SpellChecker()
#cl = DummyClassifier(sc)
cl = RedisClassifier(sc)
#cl = MongoClassifier(sc)
an = Analyser(cl, debug)
result = an.process(sys.argv[1])
print "%s (%s)" % ("Positivo" if result > 0 else "Negativo" if result < 0 else "Neutro", result)
