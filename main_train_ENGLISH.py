from lm_results import *
from small_modulate_text import *
import pickle as p

# """
# 	Gutenberg (ordered)
# 	Train -- 10m
# 	Test  --  1m (novel tokens)
# """
# train = ModulateText(english_gutenberg_10m, language="english")
# model = NgramModel(train.tokens, alpha=0.01, n=3)
# print("LM setup complete!")
# test = ModulateText(english_gutenberg_1m, state="ordered outbound", language="english")
# print("Test text created!")
# t = LMResults(model, test)
# t.get_results("ENGLISH_gutenberg(train[10m]_test[1m])_a0.01_OO.txt")
# file = open("ENGLISH_gutenberg_model(train[10m])_a0.01", "wb")
# p.dump(model, file)
# print("LM created!")

# test = ModulateText(english_gutenberg_1m, language="english")
# print("Test text created!")
# t = LMResults(model, test)
# t.get_results("ENGLISH_gutenberg(train[10m]_test[1m])_a0.01_OI.txt")
# print("LM created!")

# """
# 	Gutenberg (ordered)
# 	Train --   5m
# 	Test  -- 500k (novel tokens)
# """
# train = ModulateText(english_gutenberg_5m, language="english")
# model = NgramModel(train.tokens, alpha=0.01, n=3)
# print("LM setup complete!")
# test = ModulateText(english_gutenberg_500k, state="ordered outbound", language="english")
# print("Test text created!")
# t = LMResults(model, test)
# t.get_results("ENGLISH_gutenberg(train[5m]_test[500k])_a0.01_OO.txt")
# file = open("ENGLISH_gutenberg_model(train[5m])_a0.01", "wb")
# p.dump(model, file)
# print("LM created!")

# train = ModulateText(english_gutenberg_5m, language="english")
# model = NgramModel(train.tokens, alpha=0.01, n=3)
# test = ModulateText(english_gutenberg_500k, language="english")
# print("Test text created!")
# t = LMResults(model, test)
# t.get_results("ENGLISH_gutenberg(train[5m]_test[500k])_a0.01_OI.txt")
# print("LM created!")


# """
# 	Gutenberg (ordered)
# 	Train --   1m
# 	Test  -- 100k (novel tokens)
# """
# # ORDERED OUTBOUND
# train = ModulateText(english_gutenberg_1m, language="english")
# model = NgramModel(train.tokens, alpha=0.01, n=3)
# print("LM setup complete!")
# test = ModulateText(english_gutenberg_100k, state="ordered outbound", language="english")
# print("Test text created!")
# t = LMResults(model, test)
# t.get_results("ENGLISH_gutenberg(train[1m]_test[100k])_a0.01_OO.txt")
# file = open("ENGLISH_gutenberg_model(train[1m])_a0.01", "wb")
# p.dump(model, file)
# print("LM created!")

# # ORDERED INBOUND
# train = ModulateText(english_gutenberg_1m, language="english")
# model = NgramModel(train.tokens, alpha=0.01, n=3)
# test = ModulateText(english_gutenberg_100k, language="english")
# print("Test text created!")
# t = LMResults(model, test)
# t.get_results("ENGLISH_gutenberg(train[1m]_test[100k])_a0.01_OI.txt")
# print("LM created!")


# """
# 	Wiki (ordered)
# 	Train -- 10m
# 	Test  --  1m (novel tokens)
# """
# train = ModulateText(english_wiki_10m, language="english")
# model = NgramModel(train.tokens, alpha=0.01, n=3)
# print("LM setup complete!")
# test = ModulateText(english_wiki_1m, state="ordered outbound", language="english")
# print("Test text created!")
# t = LMResults(model, test)
# t.get_results("ENGLISH_wiki(train[10m]_test[1m])_a0.01_OO.txt")
# file = open("ENGLISH_wiki_model(train[10m])_a0.01", "wb")
# p.dump(model, file)
# print("LM created!")

# test = ModulateText(english_wiki_1m, language="english")
# print("Test text created!")
# t = LMResults(model, test)
# t.get_results("ENGLISH_wiki(train[10m]_test[1m])_a0.01_OI.txt")
# print("LM created!")

# """
# 	Wiki (ordered)
# 	Train --   5m
# 	Test  -- 500k (novel tokens)
# """
# train = ModulateText(english_wiki_5m, language="english")
# model = NgramModel(train.tokens, alpha=0.01, n=3)
# print("LM setup complete!")
# test = ModulateText(english_wiki_500k, state="ordered outbound", language="english")
# print("Test text created!")
# t = LMResults(model, test)
# t.get_results("ENGLISH_wiki(train[5m]_test[500k])_a0.01_OO.txt")
# file = open("ENGLISH_wiki_model(train[5m])_a0.01", "wb")
# p.dump(model, file)
# print("LM created!")

train = ModulateText(english_wiki_5m, language="english")
print("Test text created!")
test = ModulateText(english_wiki_500k, language="english")
model = NgramModel(train.tokens, alpha=0.01, n=3)
t = LMResults(model, test)
t.get_results("ENGLISH_wiki(train[5m]_test[500k])_a0.01_OI.txt")
print("LM created!")


# """
# 	wiki (ordered)
# 	Train --   1m
# 	Test  -- 100k (novel tokens)
# """
# # ORDERED OUTBOUND
# train = ModulateText(english_wiki_1m, language="english")
# model = NgramModel(train.tokens, alpha=0.01, n=3)
# print("LM setup complete!")
# test = ModulateText(english_wiki_100k, state="ordered outbound", language="english")
# print("Test text created!")
# t = LMResults(model, test)
# t.get_results("ENGLISH_wiki(train[1m]_test[100k])_a0.01_OO.txt")
# file = open("ENGLISH_wiki_model(train[1m])_a0.01", "wb")
# p.dump(model, file)
# print("LM created!")

# # ORDERED INBOUND
# test = ModulateText(english_wiki_100k, language="english")
# print("Test text created!")
# t = LMResults(model, test)
# t.get_results("ENGLISH_wiki(train[1m]_test[100k])_a0.01_OI.txt")
# print("LM created!")









# Get Results (Train Random Outbound 90, Test Random Inbound 10)
# train = ModulateText(english_90, language="english", randomize_across_sentence=True)
# model = NgramModel(train.tokens, alpha=0.1, n=3)
# file = open("LM_n3_(ENGLISH)_a0.1_R_train(90_o)_test(10_i)", "wb")
# p.dump(model, file)
# print("LM setup complete!")
# test = ModulateText(english_10, language="english", randomize_within_sentence=True)
# print("Test text created!")
# t = LMResults(model, test)
# t.get_results("LM_n3_(ENGLISH)_a0.1_R_train(90_o)_test(10_i).txt")





# file = open("LM_3gram_alpha0_(moby_dick)_ordered_FULL", "rb")
# p.load(file)



# Get Results Ordered Inbound

# model = NgramModel(ModulateText(english_train).tokens, alpha=0.1, n=3)
# test = ModulateText(english_test)
# t = LMResults(model, test, "n3_a0.1_oi_ENGLISH_full")

# file = open("LM_n3_a0.1_oi_ENGLISH_full", "wb")
# p.dump(t, file)

# # Get Results Random Inboun

# model = NgramModel(ModulateText(mega_text_90, randomize_across_sentence=True).random_tokens, alpha=0.1, n=3)
# test = ModulateText(mega_text_10, randomize_within_sentence=True)
# t = LMResults(model, test)

# model = NgramModel(ModulateText(mega_text_90, randomize_across_sentence=True).random_tokens, alpha=0.5, n=3)
# test = ModulateText(mega_text_10, randomize_within_sentence=True)
# t = TestModel(model, test)