#!/usr/bin/python
#Uso: ./redis_words_loader.py -mode file_name
import sys
from database_connection.d_words import DWords
from models.d_word import DWord



def load_modifiers(file_name):
  return

def load_polarities(file_name):
  return

def interactive_loader(file_name):
  GROUP_SIZE = 3

  words = file(file_name).read().split(" ")


  for word_group in zip(*[iter(words)]*GROUP_SIZE):
     
      
    options = ""

    d_words = []

    for word in word_group:
      d_word = DWords.find_word(word) or DWord(word)
      if not (d_word.has_polarity() or d_word.is_modifier()):
        d_words.append(d_word)

    if len(d_words) == 0:
      continue


    while len(options)!=len(d_words):
      print "\t".join(word_group)
      options = list(raw_input("0:neutral\t1:positive\t2: negative\t3:inversor\t5:minimizer\t6:maximizer\n")[:len(d_words)])
    
    for d_word in d_words:
      option = options.pop()
      if option=="0":
        d_word.polarity = 0
      elif option=="1": 
        d_word.polarity = 1 
      elif option=="2":
        d_word.polarity = -1
      elif option == "3":
        d_word.modifier = -1
      elif option == "5":
        d_word.modifier = 0.5
      elif option == "6":
        d_word.modifier = 2
      DWords.insert_word(d_word)
      if d_word.is_modifier():
        with open("modifiers.txt", "a") as f:
          f.write(d_word.word+" "+str(d_word.modifier)+"\n")
      elif d_word.has_polarity():
        with open("polarities.txt", "a") as f:
          f.write(d_word.word+" "+str(d_word.polarity)+"\n")
    print "\n\n\n"


mode = sys.argv[1]

if mode == "-i":
  interactive_loader(sys.argv[2])

elif mode == "-m":
  load_modifiers(sys.argv[2])
elif mode == "-p":
  load_polarities(sys.argv[2])

