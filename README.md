# sentiment-analyser
Simple sentiment calculator for spanish texts. It calculates text positivity, negativity or neutrality by replacing words with their stored values and operating with them. It uses two types of words:

* **Polarities**: This words make the sentence more positive or more negative.
* **Modifiers**: This words modify the polarity of other words. 



##Requirements 

Python 2.7

pip install -r requirements.txt

Redis 

##Scripts
**./redis_words_loader.py -m <text_file>** Loads modifiers from text_file (check [modifiers.txt](https://github.com/Dkazarian/sentiment-analyser/blob/master/analyser/data/modifiers.txt))

**./redis_words_loader.py -p <text_file>** Loads polarities from text_file (check [polarities.txt](https://github.com/Dkazarian/sentiment-analyser/blob/master/analyser/data/polarities.txt))

**./spell_checker.py** Loads word ocurrences for the spellchecker.

**./redis_load_analyser_txts.py**   Uses the script above to load the text files stored in /analyser/data 


**./run_analyser.py <text> [-debug]**    Prints polarity of text

**./run_analyser.py -f <text file> [-debug]**  Prints polarity of text from text file

**./init_server.py** Starts analyzer server at localhost:5000. 

**./make_request.py** Sends a demo request to the server.


##Some links

[How to Write a Spelling Corrector](http://norvig.com/spell-correct.html).

Word values in [anew.txt](https://github.com/Dkazarian/sentiment-analyser/blob/master/analyser/data/anew.txt) values were calculated from [Spanish ANEW](http://www.uvm.edu/~pdodds/files/papers/others/2007/redondo2007a.pdf). They should be removed for commercial use.

The usage of a scoring method opposed to a probabilistic one was inspired by [Basic Sentiment Analysis with Python]( http://fjavieralba.com/basic-sentiment-analysis-with-python.html).
