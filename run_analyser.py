#!/usr/bin/python
from analyser.analyser import Analyser
from analyser.dummy_classifier import DummyClassifier


cl = DummyClassifier()
an = Analyser(cl)
print an.process("La comida no es muy buena.")
