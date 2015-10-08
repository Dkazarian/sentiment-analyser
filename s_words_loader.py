#!/usr/bin/python


#Uso: ./s_words_loader.py -mode file_name 
# mode: -m para modifiers, -p para polarity


import sys
from database_connection.s_words import SWords
from models.s_word import SWord


mode = sys.argv[1]
file_name = sys.argv[2]




import xlrd
book = xlrd.open_workbook(file_name)
sh = book.sheet_by_index(0)
for rx in range(sh.nrows):
  word = sh.cell_value(rowx=rx, colx=0)
  value = float(sh.cell_value(rowx=rx, colx=1))

  polarity = None
  modifier = None 
  if mode == "-m":
    modifier = value 
  elif mode == "-p":
    polarity = value 

  s_word = SWord(word, polarity= polarity, modifier=modifier)
  SWords.insert_word(s_word)
  print "%s %s" % (word, value)

