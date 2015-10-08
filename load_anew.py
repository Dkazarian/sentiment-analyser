#!/usr/bin/python
from database_connection.s_words import SWords
from models.s_word import SWord
import sys
import xlrd

file_name = sys.argv[1] if len(sys.argv) == 2 else "analyser/data/Redondo-BRM-2007/Redondo(2007).xls"
book = xlrd.open_workbook(file_name)
sh = book.sheet_by_index(0)
for rx in range(1, sh.nrows):
  word = sh.cell_value(rowx=rx, colx=2)
  polarity = sh.cell_value(rowx=rx, colx=3) - 5

  
  s_word = SWord(word, polarity= polarity)
  SWords.insert_word(s_word)
  print "%s %s" % (word, polarity)

