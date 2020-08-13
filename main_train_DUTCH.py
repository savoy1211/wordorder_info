from lm_results import *
import pickle as p

# Dutch
# Get Results (Ordered Inbound 100)
# test = ModulateText(dutch_100, language="dutch")
# print("Test text created!")
# model = NgramModel(test.tokens, alpha=0, n=3)
# print("LM setup complete!")
# t = LMResultsBaseline(model, test)
# t.get_results("LM_n3_(DUTCH)_a0.1_OI_train(100)_test(100).txt")
# file = open("LM_n3_(DUTCH)_a0.1_OI_train(100)_test(100)", "wb")
# p.dump(model, file)
# print("LM created!")

# # Get Results (Ordered Inbound 100)
# test = ModulateText(dutch_100, language="dutch")
# print("Test text created!")
# model = NgramModel(test.tokens, alpha=0.1, n=3)
# print("LM setup complete!")
# t = LMResults(model, test)
# t.get_results("LM_n3_(DUTCH)_a0.1_OI_train(100)_test(100).txt")
# file = open("LM_n3_(DUTCH)_a0.1_OI_train(100)_test(100)", "wb")
# p.dump(model, file)
# print("LM created!")

# Get Results (Train Ordered Inbound 90, Test Ordered Inbound 10)
train = ModulateText(dutch_90, language="dutch")
model = NgramModel(train.tokens, alpha=0.1, n=3)
print("LM setup complete!")
test = ModulateText(dutch_10, language="dutch")
print("Test text created!")
t = LMResults(model, test)
t.get_results("LM_n3_(DUTCH)_a0.1_OI_train(90)_test(10).txt")
file = open("LM_n3_(DUTCH)_a0.1_OI_train(100)_test(100)", "wb")
p.dump(model, file)
print("LM created!")

# Get Results (Train Random Outbound 90, Test Random Inbound 10)
train = ModulateText(dutch_90, language="dutch", randomize_across_sentence=True)
model = NgramModel(train.tokens, alpha=0.1, n=3)
file = open("LM_n3_(DUTCH)_a0.1_R_train(90_o)_test(10_i)", "wb")
p.dump(model, file)
print("LM setup complete!")
test = ModulateText(dutch_10, language="dutch", randomize_within_sentence=True)
print("Test text created!")
t = LMResults(model, test)
t.get_results("LM_n3_(DUTCH)_a0.1_R_train(90_o)_test(10_i).txt")





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