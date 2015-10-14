#!/usr/bin/python
import sys
from database_connection.s_words import SWords

SWords.get_collection().remove({})



sys.argv = [sys.executable, "analyser/data/Redondo-BRM-2007/Redondo(2007).xls"]
execfile( "load_anew.py")

sys.argv = [sys.executable, "-m", "analyser/data/modifiers.xls"]
execfile( "s_words_loader.py")


sys.argv = [sys.executable, "-p", "analyser/data/polarity.xls"]
execfile( "s_words_loader.py")