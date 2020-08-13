import os
import requests
# from download_local_gutenberg_texts import *

# turkish texts
turkish_100 =''
with open('lm_corpus_turkish_100_small', 'r', encoding="utf-8") as current_file:
    text = current_file.read().encode('utf-8')[1:]
    turkish_100 = text.decode('utf-8', 'ignore')

turkish_90 =''
with open('lm_corpus_turkish_90_small', 'r', encoding="utf-8") as current_file:
    text = current_file.read().encode('utf-8')[1:]
    turkish_90 = text.decode('utf-8', 'ignore')

turkish_10 =''
with open('lm_corpus_turkish_10_small', 'r', encoding="utf-8") as current_file:
    text = current_file.read().encode('utf-8')[1:]
    turkish_10 = text.decode('utf-8', 'ignore')

print("turkish texts loaded!")

# language = "turkish"
# # # turkish texts
# turkish_100 =''
# with open('lm_corpus_turkish_100', 'r', encoding="utf-8") as current_file:
#     text = current_file.read().encode('utf-8')[1:]
#     turkish_100 = text.decode('utf-8', 'ignore')
#     turkish_100 = turkish_100[:int(len(turkish_100)/3)]
# file = open("lm_corpus_"+language+"_100_small", "w")
# file.write(turkish_100)


# turkish_90 =''
# with open('lm_corpus_turkish_90', 'r', encoding="utf-8") as current_file:
#     text = current_file.read().encode('utf-8')[1:]
#     turkish_90 = text.decode('utf-8', 'ignore')
#     turkish_90 = turkish_90[:int(len(turkish_90)/3)]
#     # turkish_90 = turkish_90[:int(len(turkish_90))]
# file = open("lm_corpus_"+language+"_90_small", "w")
# file.write(turkish_90)

# turkish_10 =''
# with open('lm_corpus_turkish_10', 'r', encoding="utf-8") as current_file:
#     text = current_file.read().encode('utf-8')[1:]
#     turkish_10 = text.decode('utf-8', 'ignore')
#     turkish_10 = turkish_10[:int(len(turkish_10)/3)]
#     # turkish_10 = turkish_10[:int(len(turkish_10))]
# file = open("lm_corpus_"+language+"_10_small", "w")
# file.write(turkish_10)

