import os
import requests
# from download_local_gutenberg_texts import *

# hungarian texts
hungarian_100 =''
with open('gutenberg_corpus_hungarian_100', 'r', encoding="utf-8") as current_file:
    text = current_file.read().encode('utf-8')[1:]
    hungarian_100 = text.decode('utf-8', 'ignore')

hungarian_90 =''
with open('gutenberg_corpus_hungarian_90', 'r', encoding="utf-8") as current_file:
    text = current_file.read().encode('utf-8')[1:]
    hungarian_90 = text.decode('utf-8', 'ignore')

hungarian_10 =''
with open('gutenberg_corpus_hungarian_10', 'r', encoding="utf-8") as current_file:
    text = current_file.read().encode('utf-8')[1:]
    hungarian_10 = text.decode('utf-8', 'ignore')

print("hungarian texts loaded!")








# language = "hungarian"
# # # hungarian texts
# hungarian_100 =''
# with open('lm_corpus_hungarian_100', 'r', encoding="utf-8") as current_file:
#     text = current_file.read().encode('utf-8')[1:]
#     hungarian_100 = text.decode('utf-8', 'ignore')
#     hungarian_100 = hungarian_100[:int(len(hungarian_100)/3)]
# file = open("lm_corpus_"+language+"_100_small", "w")
# file.write(hungarian_100)


# hungarian_90 =''
# with open('lm_corpus_hungarian_90', 'r', encoding="utf-8") as current_file:
#     text = current_file.read().encode('utf-8')[1:]
#     hungarian_90 = text.decode('utf-8', 'ignore')
#     hungarian_90 = hungarian_90[:int(len(hungarian_90)/3)]
#     # hungarian_90 = hungarian_90[:int(len(hungarian_90))]
# file = open("lm_corpus_"+language+"_90_small", "w")
# file.write(hungarian_90)

# hungarian_10 =''
# with open('lm_corpus_hungarian_10', 'r', encoding="utf-8") as current_file:
#     text = current_file.read().encode('utf-8')[1:]
#     hungarian_10 = text.decode('utf-8', 'ignore')
#     hungarian_10 = hungarian_10[:int(len(hungarian_10)/3)]
#     # hungarian_10 = hungarian_10[:int(len(hungarian_10))]
# file = open("lm_corpus_"+language+"_10_small", "w")
# file.write(hungarian_10)
# hungarian texts
# hungarian_100 =''
# with open('lm_corpus_hungarian_100_small', 'r', encoding="utf-8") as current_file:
#     text = current_file.read().encode('utf-8')[1:]
#     hungarian_100 = text.decode('utf-8', 'ignore')

# hungarian_90 =''
# with open('lm_corpus_hungarian_90_small', 'r', encoding="utf-8") as current_file:
#     text = current_file.read().encode('utf-8')[1:]
#     hungarian_90 = text.decode('utf-8', 'ignore')

# hungarian_10 =''
# with open('lm_corpus_hungarian_10_small', 'r', encoding="utf-8") as current_file:
#     text = current_file.read().encode('utf-8')[1:]
#     hungarian_10 = text.decode('utf-8', 'ignore')

# print("hungarian texts loaded!")

# language = "hungarian"
# # # hungarian texts
# hungarian_100 =''
# with open('lm_corpus_hungarian_100', 'r', encoding="utf-8") as current_file:
#     text = current_file.read().encode('utf-8')[1:]
#     hungarian_100 = text.decode('utf-8', 'ignore')
#     hungarian_100 = hungarian_100[:int(len(hungarian_100)/3)]
# file = open("lm_corpus_"+language+"_100_small", "w")
# file.write(hungarian_100)


# hungarian_90 =''
# with open('lm_corpus_hungarian_90', 'r', encoding="utf-8") as current_file:
#     text = current_file.read().encode('utf-8')[1:]
#     hungarian_90 = text.decode('utf-8', 'ignore')
#     hungarian_90 = hungarian_90[:int(len(hungarian_90)/3)]
#     # hungarian_90 = hungarian_90[:int(len(hungarian_90))]
# file = open("lm_corpus_"+language+"_90_small", "w")
# file.write(hungarian_90)

# hungarian_10 =''
# with open('lm_corpus_hungarian_10', 'r', encoding="utf-8") as current_file:
#     text = current_file.read().encode('utf-8')[1:]
#     hungarian_10 = text.decode('utf-8', 'ignore')
#     hungarian_10 = hungarian_10[:int(len(hungarian_10)/3)]
#     # hungarian_10 = hungarian_10[:int(len(hungarian_10))]
# file = open("lm_corpus_"+language+"_10_small", "w")
# file.write(hungarian_10)

