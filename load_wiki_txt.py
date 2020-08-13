import os
import requests
# from download_local_gutenberg_texts import *

# dutch texts
dutch_100 =''
with open('lm_corpus_dutch_100_small', 'r', encoding="utf-8") as current_file:
    text = current_file.read().encode('utf-8')[1:]
    dutch_100 = text.decode('utf-8', 'ignore')

dutch_90 =''
with open('lm_corpus_dutch_90_small', 'r', encoding="utf-8") as current_file:
    text = current_file.read().encode('utf-8')[1:]
    dutch_90 = text.decode('utf-8', 'ignore')

dutch_10 =''
with open('lm_corpus_dutch_10_small', 'r', encoding="utf-8") as current_file:
    text = current_file.read().encode('utf-8')[1:]
    dutch_10 = text.decode('utf-8', 'ignore')

print("dutch texts loaded!")

# language = "dutch"
# # # dutch texts
# dutch_100 =''
# with open('lm_corpus_dutch_100', 'r', encoding="utf-8") as current_file:
#     text = current_file.read().encode('utf-8')[1:]
#     dutch_100 = text.decode('utf-8', 'ignore')
#     dutch_100 = dutch_100[:int(len(dutch_100)/3)]
# file = open("lm_corpus_"+language+"_100_small", "w")
# file.write(dutch_100)


# dutch_90 =''
# with open('lm_corpus_dutch_90', 'r', encoding="utf-8") as current_file:
#     text = current_file.read().encode('utf-8')[1:]
#     dutch_90 = text.decode('utf-8', 'ignore')
#     dutch_90 = dutch_90[:int(len(dutch_90)/3)]
#     # dutch_90 = dutch_90[:int(len(dutch_90))]
# file = open("lm_corpus_"+language+"_90_small", "w")
# file.write(dutch_90)

# dutch_10 =''
# with open('lm_corpus_dutch_10', 'r', encoding="utf-8") as current_file:
#     text = current_file.read().encode('utf-8')[1:]
#     dutch_10 = text.decode('utf-8', 'ignore')
#     dutch_10 = dutch_10[:int(len(dutch_10)/3)]
#     # dutch_10 = dutch_10[:int(len(dutch_10))]
# file = open("lm_corpus_"+language+"_10_small", "w")
# file.write(dutch_10)

