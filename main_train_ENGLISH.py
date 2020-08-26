from lm_results import *
import pickle as p

# english
# Get Results (Ordered Inbound 100)
# test = ModulateText(english_100, language="english")
# print("Test text created!")
# model = NgramModel(test.tokens, alpha=0, n=3)
# print("LM setup complete!")
# t = LMResultsBaseline(model, test)
# t.get_results("LM_n3_(ENGLISH)_a0.1_OI_train(100)_test(100).txt")
# file = open("LM_n3_(ENGLISH)_a0.1_OI_train(100)_test(100)", "wb")
# p.dump(model, file)
# print("LM created!")

# # Get Results (Ordered Inbound 100)
# test = ModulateText(english_100, language="english")
# print("Test text created!")
# model = NgramModel(test.tokens, alpha=0.1, n=3)
# print("LM setup complete!")
# t = LMResults(model, test)
# t.get_results("LM_n3_(ENGLISH)_a0.1_OI_train(100)_test(100).txt")
# file = open("LM_n3_(ENGLISH)_a0.1_OI_train(100)_test(100)", "wb")
# p.dump(model, file)
# print("LM created!")

# Get Results (Train Ordered Inbound 90, Test Ordered Inbound 10)
train = ModulateText(english_90[:int(len(english_90)/2)], state="ordered outbound", language="english")
model = NgramModel(train.tokens, alpha=0, n=3)
print("LM setup complete!")
# test = ModulateText(english_10, language="english")
print("Test text created!")
t = LMResultsBaseline(model, train)
t.get_results("LM_n3_(ENGLISH_gutenberg_90_d_2)_a0_OO.txt")
# file = open("LM_n3_(ENGLISH_gutenberg)_a0.01_R_train(90_o)_test(10_i)", "wb")
# p.dump(model, file)
print("LM created!")

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