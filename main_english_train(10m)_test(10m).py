from lm_results import *
from small_modulate_text import *
import pickle as p

"""
	Gutenberg (ordered)
	Train -- 10m
	Test  --  1m (novel tokens)
"""
train = ModulateText(english_gutenberg_10m, state="ordered outbound", language="english")
model = NgramModel(train.tokens, alpha=0.01, n=3)
print("LM setup complete!")
t = LMResults(model, train)
t.get_results("(10/13/20)_ENGLISH_gutenberg(train[10m]_test[10m])_a0.01_OO.txt")
file = open("ENGLISH_gutenberg_model(train[10m])_a0.01", "wb")
p.dump(model, file)
print("LM created!")