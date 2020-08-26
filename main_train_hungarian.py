from lm_results import *
import pickle as p

# Hungarian
"""
	gutenberg:
		-tokens:  4,938,104
		-vocab:     369,911
		-t/v:          13.3
"""
file_name = "LM_n3_(hungarian_100_gutenberg)_a0_OO" # [4.9m_tokens]
train = ModulateText(hungarian_100, state="ordered outbound", language="hungarian", id_hungarian="hungarian_100")
model = NgramModel(train.tokens, alpha=0, n=3)
# file = open(file_name, "wb")
# p.dump(model, file)
print("LM created!")
print("LM setup complete!")
# test = ModulateText(hungarian_10, language="hungarian", id_hungarian="hungarian_10")
print("Test text created!")
t = LMResultsBaseline(model, train)
t.get_results(file_name+".txt")
print("Done!")

# # # Get Results (Train Random Outbound 90, Test Random Inbound 10)
# file_name = "LM_n3_(hungarian_90_gutenberg)_a0.001_R_train(90_o)_test(10_i)"
# train = ModulateText(hungarian_90, language="hungarian", state="random", randomize_across_sentence=True, id_hungarian="hungarian_90")
# model = NgramModel(train.tokens, alpha=0.001, n=3)
# file = open(file_name, "wb")
# p.dump(model, file)
# print("LM created!")
# print("LM setup complete!")
# test = ModulateText(hungarian_10, language="hungarian", state="random", randomize_within_sentence=True, id_hungarian="hungarian_10")
# print("Test text created!")
# t = LMResults(model, test)
# t.get_results(file_name+".txt")
# print("Done!")

