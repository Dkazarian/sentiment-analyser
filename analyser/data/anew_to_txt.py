#!/usr/bin/python
# coding: UTF-8
import sys
import xlrd

file_name = "Redondo-BRM-2007/Redondo(2007).xls"
book = xlrd.open_workbook(file_name)
sh = book.sheet_by_index(0)
for rx in range(1, sh.nrows):
  word = sh.cell_value(rowx=rx, colx=2)
  polarity = int(sh.cell_value(rowx=rx, colx=3) - 5)
  if polarity != 0:
    polarity = polarity/4.0
  with open("anew.txt", "a") as f:
    f.write(word.encode('utf-8')+" "+str(polarity)+"\n")