from lm_results import *
from small_modulate_text import *

print('english_gutenberg_1m[:200000]')
print("spacy1:")
train_spacy = SmallModulateText(english_gutenberg_1m[:200000], tokenizer="spacy1")
print("spacy3:")
train_spacy = SmallModulateText(english_gutenberg_1m[:200000], tokenizer="spacy3")
print("nltk:")
train_nltk = SmallModulateText(english_gutenberg_1m[:200000], tokenizer="nltk")

print('english_gutenberg_1m[:500000]')
print("spacy1:")
train_spacy = SmallModulateText(english_gutenberg_1m[:500000], tokenizer="spacy1")
print("spacy3:")
train_spacy = SmallModulateText(english_gutenberg_1m[:500000], tokenizer="spacy3")
print("nltk:")
train_nltk = SmallModulateText(english_gutenberg_1m[:500000], tokenizer="nltk")

print('english_gutenberg_1m[:1000000]')
print("spacy1:")
train_spacy = SmallModulateText(english_gutenberg_1m[:1000000], tokenizer="spacy1")
print("spacy3:")
train_spacy = SmallModulateText(english_gutenberg_1m[:1000000], tokenizer="spacy3")
print("nltk:")
train_nltk = SmallModulateText(english_gutenberg_1m[:1000000], tokenizer="nltk")

print('english_gutenberg_1m[:1500000]')
print("spacy1:")
train_spacy = SmallModulateText(english_gutenberg_1m[:1500000], tokenizer="spacy1")
print("spacy3:")
train_spacy = SmallModulateText(english_gutenberg_1m[:1500000], tokenizer="spacy3")
print("nltk:")
train_nltk = SmallModulateText(english_gutenberg_1m[:1500000], tokenizer="nltk")

print('english_gutenberg_1m[:2000000]')
print("spacy1:")
train_spacy = SmallModulateText(english_gutenberg_1m[:2000000], tokenizer="spacy1")
print("spacy3:")
train_spacy = SmallModulateText(english_gutenberg_1m[:2000000], tokenizer="spacy3")
print("nltk:")
train_nltk = SmallModulateText(english_gutenberg_1m[:2000000], tokenizer="nltk")

print('english_gutenberg_1m[:2500000]')
print("spacy1:")
train_spacy = SmallModulateText(english_gutenberg_1m[:2500000], tokenizer="spacy1")
print("spacy3:")
train_spacy = SmallModulateText(english_gutenberg_1m[:2500000], tokenizer="spacy3")
print("nltk:")
train_nltk = SmallModulateText(english_gutenberg_1m[:2500000], tokenizer="nltk")

print('english_gutenberg_1m[:5000000]')
print("spacy1:")
train_spacy = SmallModulateText(english_gutenberg_1m[:5000000], tokenizer="spacy1")
print("spacy3:")
train_spacy = SmallModulateText(english_gutenberg_1m[:5000000], tokenizer="spacy3")
print("nltk:")
train_nltk = SmallModulateText(english_gutenberg_1m[:5000000], tokenizer="nltk")

print('english_gutenberg_1m')
print("spacy1:")
train_spacy = SmallModulateText(english_gutenberg_1m, tokenizer="spacy1")
print("spacy3:")
train_spacy = SmallModulateText(english_gutenberg_1m, tokenizer="spacy3")
print("nltk:")
train_nltk = SmallModulateText(english_gutenberg_1m, tokenizer="nltk")