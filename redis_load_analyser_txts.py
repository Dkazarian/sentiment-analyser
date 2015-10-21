#!/usr/bin/python
import sys


sys.argv = [sys.executable, "-p", "analyser/data/anew.txt"]
execfile( "redis_words_loader.py")

sys.argv = [sys.executable, "-m", "analyser/data/modifiers.txt"]
execfile( "redis_words_loader.py")

sys.argv = [sys.executable, "-p", "analyser/data/polarities.txt"]
execfile( "redis_words_loader.py")

sys.argv = [sys.executable, "-p", "analyser/data/emojis.txt"]
execfile( "redis_words_loader.py")