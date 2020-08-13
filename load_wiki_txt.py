import os
import requests
from download_local_gutenberg_texts import *

# # Turkish texts
# turkish_100 =''
# with open('lm_corpus_turkish_100', 'r', encoding="utf-8") as current_file:
#     text = current_file.read().encode('utf-8')[1:]
#     turkish_100 = text.decode('utf-8', 'ignore')

# turkish_90 =''
# with open('lm_corpus_turkish_90', 'r', encoding="utf-8") as current_file:
#     text = current_file.read().encode('utf-8')[1:]
#     turkish_90 = text.decode('utf-8', 'ignore')

# turkish_10 =''
# with open('lm_corpus_turkish_10', 'r', encoding="utf-8") as current_file:
#     text = current_file.read().encode('utf-8')[1:]
#     turkish_10 = text.decode('utf-8', 'ignore')

# print("turkish texts loaded!")

# Dutch texts
# dutch_100 =''
# with open('lm_corpus_dutch_100', 'r', encoding="utf-8") as current_file:
#     text = current_file.read().encode('utf-8')[1:]
#     dutch_100 = text.decode('utf-8', 'ignore')

# dutch_90 =''
# with open('lm_corpus_dutch_90', 'r', encoding="utf-8") as current_file:
#     text = current_file.read().encode('utf-8')[1:]
#     dutch_90 = text.decode('utf-8', 'ignore')
#     dutch_90 = dutch_90[:int(len(dutch_90)*.05)]

# dutch_10 =''
# with open('lm_corpus_dutch_10', 'r', encoding="utf-8") as current_file:
#     text = current_file.read().encode('utf-8')[1:]
#     dutch_10 = text.decode('utf-8', 'ignore')
#     dutch_10 = dutch_10[:int(len(dutch_10)*.05)]


# print("dutch texts loaded!")


# chinese_90 = text[:int(l*.9)] 
# chinese_10 = text[int(l*.9):]
# turkish_90 = text[:int(l*.9/5)] 
# turkish_10 = text[int(l*.9):]


# max_len = 1000000
# current_len = 0
# english_text = ''
# with open('enwiki-20181001-corpus.xml.txt', 'r', encoding="utf-8") as current_file:
#     text = current_file.readlines()
#     for line in text:
#         text = line.encode('utf-8')[1:]
#         text = text.decode('utf-8', 'ignore')
#         # text = text[:int(len(text))]
#         l = len(text)
#         if current_len >= max_len:
#             break
#         else:
#             english_text += text
#             current_len += l

# english_full = english_text[:1000000]
# print("English text loaded!")
# print(len(english_full))


# # text = ''
# with open('dutch_corpus_size_small', 'r', encoding="utf-8") as current_file:
#     text = current_file.read().encode('utf-8')[1:]
#     text = text.decode('utf-8', 'ignore')
#     l = len(text)
#     text = text[:int(l/73)]

# dutch_full = text
# print("Dutch text loaded!")

# # file = open("dutch_corpus_size_small", "w")
# # file.write(dutch_full)
# print("DONE")
