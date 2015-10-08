from spell_checker.spell_checker import SpellChecker

spell_checker = SpellChecker()
spell_checker.train_with_occurrences("spell_checker/training_files/words_and_occurrences.txt")