from lm_results import *
from small_modulate_text import *

print("spacy:")
train_spacy = SmallModulateText(english_gutenberg_1m, tokenizer="spacy")
print("nltk:")
train_nltk = SmallModulateText(english_gutenberg_1m, tokenizer="nltk")