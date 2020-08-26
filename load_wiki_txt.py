import os
import requests
# from download_local_gutenberg_texts import *

# english texts
english_100 =''
english_gutenberg = ''
english_wiki = ''
with open('gutenberg_corpus_english_100', 'r', encoding="utf-8") as current_file:
    text = current_file.read().encode('utf-8')[1:]
    english_100 = text.decode('utf-8', 'ignore')
    english_gutenberg = english_100

with open('wiki_corpus_english_100', 'r', encoding="utf-8") as current_file:
    text = current_file.read().encode('utf-8')[1:]
    english_wiki = text.decode('utf-8', 'ignore')

dutch_100 =''
dutch_gutenberg = ''
dutch_wiki = ''
with open('gutenberg_corpus_dutch_100', 'r', encoding="utf-8") as current_file:
    text = current_file.read().encode('utf-8')[1:]
    dutch_100 = text.decode('utf-8', 'ignore')
    dutch_gutenberg = dutch_100

with open('wiki_corpus_dutch_100', 'r', encoding="utf-8") as current_file:
    text = current_file.read().encode('utf-8')[1:]
    dutch_wiki = text.decode('utf-8', 'ignore')


mandarin_100 =''
mandarin_gutenberg = ''
mandarin_wiki = ''
with open('gutenberg_corpus_mandarin_100', 'r', encoding="utf-8") as current_file:
    text = current_file.read().encode('utf-8')[1:]
    mandarin_100 = text.decode('utf-8', 'ignore')
    mandarin_gutenberg = mandarin_100

with open('wiki_corpus_mandarin_100', 'r', encoding="utf-8") as current_file:
    text = current_file.read().encode('utf-8')[1:]
    mandarin_wiki = text.decode('utf-8', 'ignore')

polish_wiki = ''
with open('wiki_corpus_polish_100', 'r', encoding="utf-8") as current_file:
    text = current_file.read().encode('utf-8')[1:]
    polish_wiki = text.decode('utf-8', 'ignore')

portuguese_wiki = ''
with open('wiki_corpus_portuguese_100', 'r', encoding="utf-8") as current_file:
    text = current_file.read().encode('utf-8')[1:]
    portuguese_wiki = text.decode('utf-8', 'ignore')

turkish_wiki = ''
with open('wiki_corpus_turkish_100', 'r', encoding="utf-8") as current_file:
    text = current_file.read().encode('utf-8')[1:]
    turkish_wiki = text.decode('utf-8', 'ignore')

hungarian_100 =''
hungarian_gutenberg = ''
hungarian_wiki = ''
with open('gutenberg_corpus_hungarian_100', 'r', encoding="utf-8") as current_file:
    text = current_file.read().encode('utf-8')[1:]
    hungarian_100 = text.decode('utf-8', 'ignore')
    hungarian_gutenberg = hungarian_100

with open('wiki_corpus_hungarian_100', 'r', encoding="utf-8") as current_file:
    text = current_file.read().encode('utf-8')[1:]
    hungarian_wiki = text.decode('utf-8', 'ignore')

print("ALL TEXTS LOADED (en, du, zh, pl, po, tk, hu)")

# english_90 =''
# with open('gutenberg_corpus_english_90', 'r', encoding="utf-8") as current_file:
#     text = current_file.read().encode('utf-8')[1:]
#     english_90 = text.decode('utf-8', 'ignore')

# english_10 =''
# with open('gutenberg_corpus_english_10', 'r', encoding="utf-8") as current_file:
#     text = current_file.read().encode('utf-8')[1:]
#     english_10 = text.decode('utf-8', 'ignore')

# print("english texts loaded!")






# language = "english"
# # # english texts
# english_100 =''
# with open('lm_corpus_english_100', 'r', encoding="utf-8") as current_file:
#     text = current_file.read().encode('utf-8')[1:]
#     english_100 = text.decode('utf-8', 'ignore')
#     english_100 = english_100[:int(len(english_100)/3)]
# file = open("lm_corpus_"+language+"_100_small", "w")
# file.write(english_100)


# english_90 =''
# with open('lm_corpus_english_90', 'r', encoding="utf-8") as current_file:
#     text = current_file.read().encode('utf-8')[1:]
#     english_90 = text.decode('utf-8', 'ignore')
#     english_90 = english_90[:int(len(english_90)/3)]
#     # english_90 = english_90[:int(len(english_90))]
# file = open("lm_corpus_"+language+"_90_small", "w")
# file.write(english_90)

# english_10 =''
# with open('lm_corpus_english_10', 'r', encoding="utf-8") as current_file:
#     text = current_file.read().encode('utf-8')[1:]
#     english_10 = text.decode('utf-8', 'ignore')
#     english_10 = english_10[:int(len(english_10)/3)]
#     # english_10 = english_10[:int(len(english_10))]
# file = open("lm_corpus_"+language+"_10_small", "w")
# file.write(english_10)
# english texts
# english_100 =''
# with open('lm_corpus_english_100_small', 'r', encoding="utf-8") as current_file:
#     text = current_file.read().encode('utf-8')[1:]
#     english_100 = text.decode('utf-8', 'ignore')

# english_90 =''
# with open('lm_corpus_english_90_small', 'r', encoding="utf-8") as current_file:
#     text = current_file.read().encode('utf-8')[1:]
#     english_90 = text.decode('utf-8', 'ignore')

# english_10 =''
# with open('lm_corpus_english_10_small', 'r', encoding="utf-8") as current_file:
#     text = current_file.read().encode('utf-8')[1:]
#     english_10 = text.decode('utf-8', 'ignore')

# print("english texts loaded!")

# language = "english"
# # # english texts
# english_100 =''
# with open('lm_corpus_english_100', 'r', encoding="utf-8") as current_file:
#     text = current_file.read().encode('utf-8')[1:]
#     english_100 = text.decode('utf-8', 'ignore')
#     english_100 = english_100[:int(len(english_100)/3)]
# file = open("lm_corpus_"+language+"_100_small", "w")
# file.write(english_100)


# english_90 =''
# with open('lm_corpus_english_90', 'r', encoding="utf-8") as current_file:
#     text = current_file.read().encode('utf-8')[1:]
#     english_90 = text.decode('utf-8', 'ignore')
#     english_90 = english_90[:int(len(english_90)/3)]
#     # english_90 = english_90[:int(len(english_90))]
# file = open("lm_corpus_"+language+"_90_small", "w")
# file.write(english_90)

# english_10 =''
# with open('lm_corpus_english_10', 'r', encoding="utf-8") as current_file:
#     text = current_file.read().encode('utf-8')[1:]
#     english_10 = text.decode('utf-8', 'ignore')
#     english_10 = english_10[:int(len(english_10)/3)]
#     # english_10 = english_10[:int(len(english_10))]
# file = open("lm_corpus_"+language+"_10_small", "w")
# file.write(english_10)

