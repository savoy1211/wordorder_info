import os
import requests
# from download_local_gutenberg_texts import *

# English
"""
    english_wiki:
        -tokens: 11,440,830
        -vocab:     249,110
        -t/v:          45.9
--------------------------------
    -----WIKI-----
    (10m tokens) -- Training set
    english_wiki[:int(len(english_wiki)*10/11.440830)]
        -tokens: 10,008,956
        -vocab:     228096
        -t/v:          43.9
--------------------------------
    -----WIKI-----
    (1m tokens) -- Test set
    english_wiki[int(len(english_wiki)*(1-(1.01/11.440830))):]
        -tokens:  1,003,141
        -vocab:       60471
        -t/v:          16.6
--------------------------------
    -----WIKI-----
    (5m tokens) -- Training set
    english_wiki[:int(len(english_wiki)/2.15)]
        -tokens:  5,328,333
        -vocab:     160720
        -t/v:          33.2
--------------------------------
    -----WIKI-----
    (500k tokens) -- Test set
    english_wiki[int(len(english_wiki)*(1-(.504/11.440830))):]
        -tokens:    500,424
        -vocab:      40169
        -t/v:          12.5
--------------------------------
    -----WIKI-----
    (100k tokens) -- Test set 
    english_wiki[:int(len(english_wiki)*.1/11.440830)]
        -tokens:    100,416
        -vocab:      14,666
        -t/v:           6.8
--------------------------------
    english_gutenberg:
        -tokens: 12,977,277
        -vocab:     100615
        -t/v:         129.0
--------------------------------
    --GUTENBERG--
    (10m tokens) -- Training set
    english_gutenberg[:int(len(english_gutenberg)*10/12.977277)]
        -tokens: 10,008,099
        -vocab:      90,816
        -t/v:         110.2
--------------------------------
    --GUTENBERG--
    (1m tokens) -- Test set
    english_gutenberg[int(len(english_gutenberg)*(1-(1.1/12.977277))):]
        -tokens:  1,083,085
        -vocab:      28,241
        -t/v:          38.4
--------------------------------
    --GUTENBERG--
    (5m tokens) -- Training set
    english_gutenberg[:int(len(english_gutenberg)/2.44)]
        -tokens:  5,334,034
        -vocab:      56,954
        -t/v:          93.7
--------------------------------
    --GUTENBERG--
    (500k tokens) -- Test set 
    english_gutenberg[int(len(english_gutenberg)*(1-(.5/12.977277))):]
        -tokens:    502325
        -vocab:      19,131
        -t/v:          26.3
--------------------------------
    --GUTENBERG--
    (100k tokens) -- Test set 
    english_gutenberg[:int(len(english_gutenberg)*0.104/12.977277)]
        -tokens:    101,560
        -vocab:       8,306
        -t/v:          12.2
"""
english_100 =''
english_gutenberg = ''
english_wiki = ''
with open('texts/gutenberg_corpus_english_100', 'r', encoding="utf-8") as current_file:
    text = current_file.read().encode('utf-8')[1:]
    english_100 = text.decode('utf-8', 'ignore')
    english_gutenberg = english_100

with open('texts/wiki_corpus_english_100', 'r', encoding="utf-8") as current_file:
    text = current_file.read().encode('utf-8')[1:]
    english_wiki = text.decode('utf-8', 'ignore')

# english_wiki_10m = english_wiki[:int(len(english_wiki)*10/11.440830)]
# english_wiki_1m = english_wiki[int(len(english_wiki)*(1-(1.01/11.440830))):]
# english_wiki_5m = english_wiki[:int(len(english_wiki)/2.15)]
# english_wiki_500k = english_wiki[int(len(english_wiki)*(1-(.504/11.440830))):]

# english_gutenberg_10m = english_gutenberg[:int(len(english_gutenberg)*10/12.977277)]
# english_gutenberg_1m = english_gutenberg[int(len(english_gutenberg)*(1-(1.1/12.977277))):]
# english_gutenberg_5m = english_gutenberg[:int(len(english_gutenberg)/2.44)]
# english_gutenberg_500k = english_gutenberg[int(len(english_gutenberg)*(1-(.5/12.977277))):]

# Greek
"""
--------------------------------
    greek_gutenberg:
        -tokens:  7,987,722
        -vocab:     377,694
        -t/v:          21.1
--------------------------------
    --GUTENBERG--
    (7m tokens) -- Training set 
    greek_gutenberg[int(len(greek_gutenberg)*.77/7.987722):]
        -tokens:   7,186,394
        -vocab:      359,388
        -t/v:           20.0
--------------------------------
    --GUTENBERG--
    (800k tokens) -- Test set
    greek_gutenberg[:int(len(greek_gutenberg)*.77/7.987722)]
        -tokens:    801,328
        -vocab:      79,359
        -t/v:          10.1
--------------------------------
    --GUTENBERG--
    (4m tokens) -- Training set
    greek_gutenberg[:int(len(greek_gutenberg)*3.92/7.987722)]
        -tokens:  3,999,016
        -vocab:     232,569
        -t/v:          17.2
--------------------------------
    --GUTENBERG--
    (397k tokens) -- Test set 
    greek_gutenberg[int(len(greek_gutenberg)*(1-(0.4/7.987722))):]
        -tokens:    396,863
        -vocab:      56,738
        -t/v:           7.0
--------------------------------
    greek_wiki:
        -tokens:  7,841,117
        -vocab:     337,492
        -t/v:          23.2
--------------------------------
    ----WIKI----
    (10m tokens) -- Training set
    greek_wiki[:int(len(greek_wiki)*10.01/11.874453)]
        -tokens: 10,000,546
        -vocab:     366,363
        -t/v:          27.3

"""
dutch_100 =''
dutch_gutenberg = ''
dutch_wiki = ''
with open('texts/gutenberg_corpus_dutch_100_new', 'r', encoding="utf-8") as current_file:
    text = current_file.read().encode('utf-8')[1:]
    dutch_100 = text.decode('utf-8', 'ignore')
    dutch_gutenberg = dutch_100

with open('texts/wiki_corpus_dutch_100_new', 'r', encoding="utf-8") as current_file:
    text = current_file.read().encode('utf-8')[1:]
    dutch_wiki = text.decode('utf-8', 'ignore')


greek_100 =''
greek_gutenberg = ''
greek_wiki = ''
with open('texts/gutenberg_corpus_greek_100', 'r', encoding="utf-8") as current_file:
    text = current_file.read().encode('utf-8')[1:]
    greek_100 = text.decode('utf-8', 'ignore')
    greek_gutenberg = greek_100

with open('texts/wiki_corpus_greek_100_new', 'r', encoding="utf-8") as current_file:
    text = current_file.read().encode('utf-8')[1:]
    greek_wiki = text.decode('utf-8', 'ignore')

# mandarin_100 =''
# mandarin_gutenberg = ''
# mandarin_wiki = ''
# with open('texts/gutenberg_corpus_mandarin_100', 'r', encoding="utf-8") as current_file:
#     text = current_file.read().encode('utf-8')[1:]
#     mandarin_100 = text.decode('utf-8', 'ignore')
#     mandarin_gutenberg = mandarin_100

# with open('texts/wiki_corpus_mandarin_100', 'r', encoding="utf-8") as current_file:
#     text = current_file.read().encode('utf-8')[1:]
#     mandarin_wiki = text.decode('utf-8', 'ignore')

polish_100 =''
polish_lit = ''
polish_wiki = ''
with open('texts/lit_corpus_polish_100', 'r', encoding="utf-8") as current_file:
    text = current_file.read().encode('utf-8')[1:]
    polish_100 = text.decode('utf-8', 'ignore')
    polish_lit = polish_100

# with open('texts/wiki_corpus_polish_100_new', 'r', encoding="utf-8") as current_file:
#     text = current_file.read().encode('utf-8')[1:]
#     polish_wiki = text.decode('utf-8', 'ignore')

# portuguese_wiki = ''
# with open('texts/wiki_corpus_portuguese_100', 'r', encoding="utf-8") as current_file:
#     text = current_file.read().encode('utf-8')[1:]
#     portuguese_wiki = text.decode('utf-8', 'ignore')

# turkish_wiki = ''
# with open('texts/wiki_corpus_turkish_100', 'r', encoding="utf-8") as current_file:
#     text = current_file.read().encode('utf-8')[1:]
#     turkish_wiki = text.decode('utf-8', 'ignore')

hungarian_100 =''
hungarian_gutenberg = ''
hungarian_wiki = ''
with open('texts/gutenberg_corpus_hungarian_100', 'r', encoding="utf-8") as current_file:
    text = current_file.read().encode('utf-8')[1:]
    hungarian_100 = text.decode('utf-8', 'ignore')
    hungarian_gutenberg = hungarian_100

with open('texts/wiki_corpus_hungarian_100', 'r', encoding="utf-8") as current_file:
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

