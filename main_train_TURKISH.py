from lm_results import *
import pickle as p

# turkish
# Get Results (Ordered Inbound 100)
# test = ModulateText(turkish_100, language="turkish")
# print("Test text created!")
# model = NgramModel(test.tokens, alpha=0, n=3)
# print("LM setup complete!")
# t = LMResultsBaseline(model, test)
# t.get_results("LM_n3_(TURKISH)_a0.1_OI_train(100)_test(100).txt")
# file = open("LM_n3_(TURKISH)_a0.1_OI_train(100)_test(100)", "wb")
# p.dump(model, file)
# print("LM created!")

# # Get Results (Ordered Inbound 100)
# test = ModulateText(turkish_100, language="turkish")
# print("Test text created!")
# model = NgramModel(test.tokens, alpha=0.1, n=3)
# print("LM setup complete!")
# t = LMResults(model, test)
# t.get_results("LM_n3_(TURKISH)_a0.1_OI_train(100)_test(100).txt")
# file = open("LM_n3_(TURKISH)_a0.1_OI_train(100)_test(100)", "wb")
# p.dump(model, file)
# print("LM created!")

file_name = "LM_n3_(TURKISH_small_lemmatized)_a0_OI_train(100)_test(100)"
train = ModulateText(turkish_100, language="turkish", lemmatize=True)
model = NgramModel(train.tokens, alpha=0, n=3)
file = open(file_name, "wb")
p.dump(model, file)
print("LM created!")
print("LM setup complete!")
# test = ModulateText(turkish_10, language="turkish", lemmatize=True)
print("Test text created!")
t = LMResults(model, train)
t.get_results(file_name+".txt")
print("Done!")

# # Get Results (Train Ordered Inbound 90, Test Ordered Inbound 10)
# model = NgramModel(test.tokens, alpha=0.1, n=3)
# print("LM setup complete!")
# print("Test text created!")
# t = LMResults(model, test)
# t.get_results("LM_n3_(TURKISH)_a0.1_OI_train(100)_test(100).txt")
# file = open("LM_n3_(TURKISH)_a0.1_OI_train(100)_test(100)", "wb")
# p.dump(model, file)
# print("LM created!")

# # Get Results (Train Random Outbound 90, Test Random Inbound 10)
# train = ModulateText(turkish_90, language="turkish", randomize_across_sentence=True)
# model = NgramModel(train.tokens, alpha=0.1, n=3)
# file = open("LM_n3_(TURKISH)_a0.1_R_train(90_o)_test(10_i)", "wb")
# p.dump(model, file)
# print("LM setup complete!")
# test = ModulateText(turkish_10, language="turkish", randomize_within_sentence=True)
# print("Test text created!")
# t = LMResults(model, test)
# t.get_results("LM_n3_(TURKISH)_a0.1_R_train(90_o)_test(10_i).txt")





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