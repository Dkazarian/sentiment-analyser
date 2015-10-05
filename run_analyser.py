#!/usr/bin/python
from analyser.analyser import Analyser
from analyser.dummy_classifier import DummyClassifier
from analyser.mongo_classifier import MongoClassifier

#cl = DummyClassifier()
cl = MongoClassifier()
an = Analyser(cl)
print an.process("La comida no es muy buena.")
