from wuggy import WuggyGenerator
from custom_orthographic_german.orthographic_german import LanguagePlugin

import pandas as pd

word_stim = pd.read_csv('01_words.csv')
prac_word_stim = pd.read_csv('01_practice_words.csv')

g = WuggyGenerator()
g.load('custom_orthographic_german', LanguagePlugin())

practice_pseudoword_matches = g.generate_classic(prac_word_stim.word)
g.export_classic_pseudoword_matches_to_csv(practice_pseudoword_matches, '02_practice_pseudowords.csv')

pseudoword_matches = g.generate_classic(word_stim.word)
g.export_classic_pseudoword_matches_to_csv(pseudoword_matches, '02_pseudowords.csv')
