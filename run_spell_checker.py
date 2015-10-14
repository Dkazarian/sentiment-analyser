#!/usr/bin/python

#Uso: ./run_spell_checker.py "palabra" [-to|-t] [file_name]
import sys
from spell_checker.spell_checker import SpellChecker

word = sys.argv[1]
train = len(sys.argv) > 2 and sys.argv[2]

spell_checker = SpellChecker()

if train == "-to":
  file_name = (len(sys.argv) > 3 and sys.argv[3]) or "spell_checker/training_files/words_and_occurrences_small.txt"
  spell_checker.train_with_occurrences(file_name)
elif train == "-t":
  spell_checker.train(sys.argv[3])
print spell_checker.correct(word)


