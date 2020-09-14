from lm_results import *
import pickle as p

"""
	Gutenberg (ordered)
	Train -- 10m
	Test  --  1m (novel tokens)
"""
# ORDERED OUTBOUND
train = ModulateText(dutch_gutenberg_10m, language="dutch")
model = NgramModel(train.tokens, alpha=0.001, n=3)
print("LM setup complete!")
test = ModulateText(dutch_gutenberg_1m, state="ordered outbound", language="dutch")
print("Test text created!")
t = LMResults(model, test)
t.get_results("DUTCH_gutenberg(train[10m]_test[1m])_a0.001_OO.txt")
file = open("DUTCH_gutenberg_model(train[10m])_a0.001", "wb")
p.dump(model, file)
print("LM created!")

# ORDERED INBOUND
test = ModulateText(dutch_gutenberg_1m, language="dutch")
print("Test text created!")
t = LMResults(model, test)
t.get_results("DUTCH_gutenberg(train[10m]_test[1m])_a0.001_OI.txt")
print("LM created!")

"""
	Gutenberg (ordered)
	Train --   5m
	Test  -- 500k (novel tokens)
"""
# ORDERED OUTBOUND
train = ModulateText(dutch_gutenberg_5m, language="dutch")
model = NgramModel(train.tokens, alpha=0.001, n=3)
print("LM setup complete!")
test = ModulateText(dutch_gutenberg_500k, state="ordered outbound", language="dutch")
print("Test text created!")
t = LMResults(model, test)
t.get_results("DUTCH_gutenberg(train[5m]_test[500k])_a0.001_OO.txt")
file = open("DUTCH_gutenberg_model(train[5m])_a0.001", "wb")
p.dump(model, file)
print("LM created!")

# ORDERED INBOUND
test = ModulateText(dutch_gutenberg_5m, language="dutch")
print("Test text created!")
t = LMResults(model, test)
t.get_results("DUTCH_gutenberg(train[5m]_test[500k])_a0.001_OI.txt")
print("LM created!")


"""
	Wiki (ordered)
	Train -- 10m
	Test  --  1m (novel tokens)
"""
# ORDERED OUTBOUND
train = ModulateText(dutch_wiki_10m, language="dutch")
model = NgramModel(train.tokens, alpha=0.001, n=3)
print("LM setup complete!")
test = ModulateText(dutch_wiki_1m, state="ordered outbound", language="dutch")
print("Test text created!")
t = LMResults(model, test)
t.get_results("DUTCH_wiki(train[10m]_test[1m])_a0.001_OO.txt")
file = open("DUTCH_wiki_model(train[10m])_a0.001", "wb")
p.dump(model, file)
print("LM created!")

# ORDERED INBOUND
test = ModulateText(dutch_wiki_1m, language="dutch")
print("Test text created!")
t = LMResults(model, test)
t.get_results("DUTCH_wiki(train[10m]_test[1m])_a0.001_OI.txt")
print("LM created!")

"""
	Wiki (ordered)
	Train --   5m
	Test  -- 500k (novel tokens)
"""
# ORDERED OUTBOUND
train = ModulateText(dutch_wiki_5m, language="dutch")
model = NgramModel(train.tokens, alpha=0.001, n=3)
print("LM setup complete!")
test = ModulateText(dutch_wiki_500k, state="ordered outbound", language="dutch")
print("Test text created!")
t = LMResults(model, test)
t.get_results("DUTCH_wiki(train[5m]_test[500k])_a0.001_OO.txt")
file = open("DUTCH_wiki_model(train[5m])_a0.001", "wb")
p.dump(model, file)
print("LM created!")

# ORDERED INBOUND
test = ModulateText(dutch_wiki_5m, language="dutch")
print("Test text created!")
t = LMResults(model, test)
t.get_results("DUTCH_wiki(train[5m]_test[500k])_a0.001_OI.txt")
print("LM created!")



# Get Results (Train Random Outbound 90, Test Random Inbound 10)
# train = ModulateText(dutch_90, randomize_across_sentence=True, language="dutch")
# model = NgramModel(train.tokens, alpha=0.001, n=3)
# print("LM setup complete!")
# test = ModulateText(dutch_10, randomize_within_sentence=True, language="dutch")
# print("Test text created!")
# t = LMResults(model, test)
# t.get_results("LM_n3_(DUTCH_gutenberg)_a0.001_R_train(90_o)_test(10_i).txt")
# # file = open("LM_n3_(DUTCH_gutenberg)_a0.001_R_train(90_o)_test(10_i)", "wb")
# # p.dump(model, file)
# print("LM created!")





# file = open("LM_3gram_alpha0_(moby_dick)_ordered_FULL", "rb")
# p.load(file)



# Get Results Ordered Inbound

# model = NgramModel(ModulateText(dutch_train).tokens, alpha=0.1, n=3)
# test = ModulateText(dutch_test)
# t = LMResults(model, test, "n3_a0.1_oi_DUTCH_full")

# file = open("LM_n3_a0.1_oi_DUTCH_full", "wb")
# p.dump(t, file)

# # Get Results Random Inboun

# model = NgramModel(ModulateText(mega_text_90, randomize_across_sentence=True).random_tokens, alpha=0.1, n=3)
# test = ModulateText(mega_text_10, randomize_within_sentence=True)
# t = LMResults(model, test)

# model = NgramModel(ModulateText(mega_text_90, randomize_across_sentence=True).random_tokens, alpha=0.5, n=3)
# test = ModulateText(mega_text_10, randomize_within_sentence=True)
# t = TestModel(model, test)