from lm_results import *
import pickle as p

# Mandarin
"""
	mandarin_wiki: **Simplified
		-tokens: 29,570,843
		-vocab:      13,924
		-t/v:        2123.7
--------------------------------
	mandarin_gutenberg: **Traditional
		-tokens: 14,819,277
		-vocab:      12,445
		-t/v:        1190.8
--------------------------------
	mandarin_wiki[:int(len(mandarin_wiki)/5.56)]: **Simplified
		-tokens: 5,325,850
		-vocab:      8,881
		-t/v:        599.7
--------------------------------
	mandarin_gutenberg[:int(len(mandarin_gutenberg)/2.79)]: **Traditional
		-tokens:  5,389,122
		-vocab:      10,263
		-t/v:         525.1
"""
train = ModulateText(mandarin_100[:int(len(mandarin_100)*0.6/2)], state="ordered outbound", language="chinese", parse_type="by character")
model = NgramModel(train.tokens, alpha=0, n=3)
print("LM setup complete!")
# test = ModulateText(mandarin_10, language="chinese", parse_type="by character")
print("Test text created!")
t = LMResultsBaseline(model, train)
t.get_results("LM_n3_(MANDARIN_gutenberg_[4.5m_tokens])_a0_OO.txt")
# file = open("LM_n3_(CHINESE_small)_a1_OI_train(90)_test(10)", "wb")
# p.dump(model, file)
print("LM created!")

# # Get Results (Train Ordered Inbound 90, Test Ordered Inbound 10)
# train = ModulateText(mandarin_90, language="chinese", parse_type="by character", randomize_across_sentence=True)

# test = ModulateText(mandarin_10, language="chinese", parse_type="by character", randomize_within_sentence=True)
# model = NgramModel(train.tokens, alpha=1, n=3)
# print("LM setup complete!")
# print("Test text created!")
# t = LMResults(model, test)
# t.get_results("LM_n3_(MANDARIN_gutenberg_medium)_a1_R_train(90)_test(10).txt")


