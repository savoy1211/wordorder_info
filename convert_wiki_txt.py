import os
import requests
from download_local_gutenberg_texts import *

len_100 = len(mega_text_100)
len_90 = len(mega_text_90)
len_10 = len(mega_text_10)

language = "dutch"
text = ''
t_100, t_90, t_10 = '','',''
with open('nlwiki-20181001-corpus.xml.txt', 'r', encoding="utf-8") as current_file:
    text = current_file.read().encode('utf-8')[1:]
    text = text.decode('utf-8', 'ignore')
    l = len(text)
    d_100 = int(l/len_100)
    # d_90 = int(l/len_90)
    # d_10 = int(l/len_10)

    t_100 = text[:int(l/d_100)]
    t_90 = t_100[:int(len(t_100)*.9)]
    t_10 = t_100[int(len(t_100)*.9):]

print(language+" texts loaded!")
print("lm_corpus_"+language+"_100")
print("lm_corpus_"+language+"_90")
print("lm_corpus_"+language+"_10")


file = open("lm_corpus_"+language+"_100", "w")
file.write(t_100)
file = open("lm_corpus_"+language+"_90", "w")
file.write(t_90)
file = open("lm_corpus_"+language+"_10", "w")
file.write(t_10)

print("DONE")