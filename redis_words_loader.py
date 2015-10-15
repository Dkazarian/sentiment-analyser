#!/usr/bin/python
#Uso: ./redis_words_loader.py -mode file_name
#mode:
#   i: interactivo, se le pasa un archivo con texto y se clasifican a mano las palabras que no estan cargadas
#   m: archivo de modifiers (varios renglones palabra <espacio> valor)
#   p: archivo de polaridades (palabra <espacio> polaridad)
import sys
from database_connection.d_words import DWords
from models.d_word import DWord
from pattern.es import parsetree


def load_modifiers(file_name):
  print "Loading modifiers from "+file_name
  load_polarity_or_modifier(file_name, "modifier")

def load_polarities(file_name):
  print "Loading polarities from "+file_name
  load_polarity_or_modifier(file_name, "polarity")

def load_polarity_or_modifier(file_name, attrname):
  words = file(file_name).read().split("\n")
  for word_value in words:
    if len(word_value.split()) != 2:
      print "Invalid line: \""+word_value+"\""
      continue
    word, value = word_value.split()
    print word_value
    d_word =  DWords.find_word(word) or DWord(word)
    setattr(d_word, attrname, float(value))
    DWords.insert_word(d_word)

def interactive_loader(file_name):
  GROUP_SIZE = 3

  text = file(file_name).read()

  words = parsetree(text, tags=False, chunks=False).words

  for word_group in zip(*[iter(words)]*GROUP_SIZE):
     
    options = ""

    d_words = []

    for word in word_group:
      d_word = DWords.find_word(word.string) or DWord(word.string)
      if not (d_word.has_polarity() or d_word.is_modifier()):
        d_words.append(d_word)

    if len(d_words) == 0:
      continue


    while len(options)!=len(d_words):
      print "\t".join(map((lambda w: w.string), word_group))
      options = list(raw_input("0:neutral\t1:positive\t2: negative\t3:inversor\t5:minimizer\t6:maximizer\n")[:len(d_words)])
    
    for d_word in d_words:
      option = options.pop(0)
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
      save_in_file(d_word)
    print "\n\n\n"

def save_in_file(d_word):
  if d_word.is_modifier():
    with open("analyser/data/modifiers.txt", "a") as f:
      f.write("\n" + d_word.word.encode('utf-8')+" "+str(d_word.modifier))
  elif d_word.has_polarity():
    with open("analyser/data/polarities.txt", "a") as f:
      f.write("\n" + d_word.word.encode('utf-8')+" "+str(d_word.polarity))

mode = sys.argv[1]

if mode == "-i":
  interactive_loader(sys.argv[2])

elif mode == "-m":
  load_modifiers(sys.argv[2])
elif mode == "-p":
  load_polarities(sys.argv[2])

