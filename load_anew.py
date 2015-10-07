#!/usr/bin/python
import math
from database_connection.s_words import SWords
from models.s_word import SWord

import xlrd
book = xlrd.open_workbook("analyser/data/Redondo-BRM-2007/Redondo(2007).xls")
sh = book.sheet_by_index(0)
for rx in range(1, sh.nrows):
  word = sh.cell_value(rowx=rx, colx=2)
  polarity = sh.cell_value(rowx=rx, colx=3) - 5

  
  s_word = SWord(word, polarity= polarity)
  SWords.insert_word(s_word)
  print "%s %s" % (word, polarity)

