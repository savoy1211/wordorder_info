import os
import requests
# from download_local_gutenberg_texts import *

# chinese texts
chinese_100 =''
with open('lm_corpus_chinese_100_small', 'r', encoding="utf-8") as current_file:
    text = current_file.read().encode('utf-8')[1:]
    chinese_100 = text.decode('utf-8', 'ignore')

chinese_90 =''
with open('lm_corpus_chinese_90_small', 'r', encoding="utf-8") as current_file:
    text = current_file.read().encode('utf-8')[1:]
    chinese_90 = text.decode('utf-8', 'ignore')

chinese_10 =''
with open('lm_corpus_chinese_10_small', 'r', encoding="utf-8") as current_file:
    text = current_file.read().encode('utf-8')[1:]
    chinese_10 = text.decode('utf-8', 'ignore')

print("chinese texts loaded!")

# language = "chinese"
# # # chinese texts
# chinese_100 =''
# with open('lm_corpus_chinese_100', 'r', encoding="utf-8") as current_file:
#     text = current_file.read().encode('utf-8')[1:]
#     chinese_100 = text.decode('utf-8', 'ignore')
#     chinese_100 = chinese_100[:int(len(chinese_100)/3)]
# file = open("lm_corpus_"+language+"_100_small", "w")
# file.write(chinese_100)


# chinese_90 =''
# with open('lm_corpus_chinese_90', 'r', encoding="utf-8") as current_file:
#     text = current_file.read().encode('utf-8')[1:]
#     chinese_90 = text.decode('utf-8', 'ignore')
#     chinese_90 = chinese_90[:int(len(chinese_90)/3)]
#     # chinese_90 = chinese_90[:int(len(chinese_90))]
# file = open("lm_corpus_"+language+"_90_small", "w")
# file.write(chinese_90)

# chinese_10 =''
# with open('lm_corpus_chinese_10', 'r', encoding="utf-8") as current_file:
#     text = current_file.read().encode('utf-8')[1:]
#     chinese_10 = text.decode('utf-8', 'ignore')
#     chinese_10 = chinese_10[:int(len(chinese_10)/3)]
#     # chinese_10 = chinese_10[:int(len(chinese_10))]
# file = open("lm_corpus_"+language+"_10_small", "w")
# file.write(chinese_10)

