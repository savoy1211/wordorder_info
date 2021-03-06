from modulate_text import *
from small_ngram_model import *

# from load_wiki_txt import *
from small_load_txt import *

# from test_token_vocab_size import *
# from hungarian_tokens_sents import *
import numpy as np
import pandas as pd
import scipy.special
import itertools
import time
import slider
import re

class LMResults:
  def __init__(self, trained_model, test_text):
    assert trained_model.alpha > 0
    # assert len(output_file) > 0
    
    self.test_state = test_text.state
    self.trained_model = trained_model
    self.test_text = test_text
    # self.get_results(output_file)


  def get_results(self, output_file):
    start = time.time()
    h_words, h_wordset = [], []
    for i in range(1,6):
      h_words_current, h_wordset_current = self.survey_text(self.trained_model, self.test_text, i)
      print("h_words",h_words_current, "h_wordset", h_wordset_current)
      h_words.append(h_words_current)
      h_wordset.append(h_wordset_current)

    d = { 'h_words': h_words, 'h_wordset': h_wordset}
    df = pd.DataFrame(data=d, dtype=np.float64)
    if self.test_state == "ordered":
      pd.DataFrame(df).to_csv(output_file)
      print("Done! Created "+output_file)
    else:
      pd.DataFrame(df).to_csv(output_file)
      print("Done! Created "+output_file)
    end = time.time()
    print(end-start)
    
    self.results = {"results_dict": d, "results_dataframe": df}

  def logp_words(self, tokens):
      """Get conditional plog of words using ngram model"""
      prob = self.trained_model.window_logprob(tokens)
      # if prob == -float("inf"):
      #   print("got 0")
        # return 0
      return prob
    
  def logp_word_set(self, tokens): 
      """Get plog sum of each tokens' permutations"""
      logprobs = [self.logp_words(reordered_tokens) for reordered_tokens in itertools.permutations(tokens)]
      # print(logprobs)
      if not logprobs:
          logprobs = [0]
      return scipy.special.logsumexp(logprobs)

  def get_windows_sentence_inbound(self, test, window_size):
    # ... for a sliding window of contiguous words of size window_size, get H[words] and H[word set] ...
    windows = []
    print("INBOUND")
    sentences = self.get_sents(test)
    sentences_filtered = [s for s in sentences if len(s) > 0]
    print("filtered!")
    for sentence in sentences_filtered:
      sentence = self.get_sent_tokens(test, sentence)
      window = []
      append_number, sentence_trunc = 0, sentence
      num_windows = lambda tokens, window_size: 1 if tokens < window_size else tokens-window_size+1
      while append_number != num_windows(len(sentence), window_size):
        window = sentence_trunc[:window_size]
        if len(window) > 0 and len(window) == window_size:
          windows.append(window)
        append_number += 1
        sentence_trunc = sentence_trunc[1:]
    return windows

  def get_sents(self, test):
    if test.language == "english":
      sent_detector = nltk.data.load('tokenizers/punkt/english.pickle')
      return sent_detector.tokenize(test.text.strip(), realign_boundaries=False)
    elif test.language == "chinese":
      return list(self.chinese_sents(test.text))
    # elif test.language == "dutch" or test.language == "turkish":
    else:
      # nlp = Dutch()
      # nlp.add_pipe(nlp.create_pipe('sentencizer'))
      # doc = nlp(test.text)
      print(test.language)
      sent_detector = nltk.data.load('tokenizers/punkt/'+test.language+'.pickle')
      return sent_detector.tokenize(test.text.strip(), realign_boundaries=False)
      # return [str(sent) for sent in list(doc.sents)]

  def get_sent_tokens(self, test, sentence):
    if test.language == "english":
      return [token.casefold() for token in nltk.tokenize.word_tokenize(sentence) if token.isalnum()]
    elif test.language == "chinese":
      tokens = [token for token in jieba.cut(text, cut_all=True)]
      stop = l = [ '︰', '︰“', '︰「', '︼', '﹁', '﹂，', '﹍﹍」', '﹐', '﹒', '﹔', '﹔??', '﹔「', '﹔」', '﹔『', '﹕', '﹕“', '﹕「', '﹕「『', '﹕『', '﹕【', '﹖', '﹖”', '﹖」', '﹗', '﹗”', '﹛', '﹞', '！', '！"', '！"□', "！'", '！\'"', "！'」", '！??', '！`', '！——', '！’', '！’”', '！’”《', '！’\ue21e', '！“', '！”', '！”——', '！”“', '！”《', '！”〔', '！•', '！………」', '！……」', '！□', '！《', ' ！「', '！」', '！」[', '！」《', '！」「', '！」」', '！」\ue3fd', '！」（', '！」）。', '！」），', '！」，', '！」－－「', '！『', '！』', '！』」', '！【', '！〔', '！〕」', '！（', '！）', '！，', '！，”', '！－－', '！？', '！［', '＃', '（', '（?', '（??）', '（“', '（《', '（「', '（〕', '）', "）'", '）[', '）、', '）。', '）。」', '）。』', '）〉', '）」', '）】', '）〔', '）！', '）！」', ' ）（', '），', '），[', '），〔', '）：', '）；', '）？', ' ）？」', '）？』', '）？【', '）？［', '＊', '＋', '，', '，"', "，'", '，(', '，*【', '，<', '，?', '，[', '，[[', '，`', '，{', '，Ш', '，——', '，‘', '，’', '，’”', '，’”《', '，’《', '，“', '，“𩥡', '，”', '，”《', '，……', '，……"', '，……」', '，……［', '，…」', '，─', '，═', '，══', '，▉', '，■', '，□', '，□□', '，□□□□', '，□□，', '，□、', '，□、□、', '，□。', '，□々', '，□，', '，、', '，。', '，〈', '，《', '\n',]
      more_stop = ["', ",'?','!','(',')',']','[',':','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','.','-','/','*','.',',',"'",'"']
      for each in more_stop:
          stop.append(each)
      for each in stop:
          tokens = [t.replace(each, "") for t in tokens]
      new_tokens = []
      for t in tokens:
          if len(t) == 1:
              new_tokens.append(t)
          else:
              list_tokens = list(t)
              for each in list_tokens:
                  new_tokens.append(each)
      return [str(token) for token in new_tokens]
    # elif test.language == "dutch" or test.language == "turkish":
    else:
      return [token.casefold() for token in nltk.tokenize.word_tokenize(sentence, language=test.language) if token.isalnum()]


  def chinese_sents(self, paragraph):
      for sent in re.findall(u'[^!?。\.\!\?]+[!?。\.\!\?]?', paragraph, flags=re.U):
          yield sent

  def get_windows_sentence_outbound(self, test, window_size):
    # ... for a sliding window of contiguous words of size window_size, get H[words] and H[word set] ...

    # # ... for a sliding window of contiguous words of size window_size, get H[words] and H[word set] ...
    print("OUTBOUND :)")
    windows, window = [], []
    t = test.random_tokens if test.state == "random outbound" else test.tokens
    return self.sliding(t, window_size)
    # windows, window = [], []
    # t = test.random_tokens if test.state == "random across sentence" else test.tokens
    # append_number, sentence_trunc = 0, t
    # num_windows = lambda tokens, window_size: 1 if tokens < window_size else tokens-window_size+1
    # while append_number != num_windows(len(t), window_size):
    #   window = sentence_trunc[:window_size]
    #   if len(window) > 0 and len(window) == window_size:
    #     windows.append(window)
    #   append_number += 1
    #   sentence_trunc = sentence_trunc[1:]
    # return windows
  
  def get_windows(self, test, window_size):
    if test.state == "random outbound" or test.state == "ordered outbound":
      windows = self.get_windows_sentence_outbound(test, window_size)
    else:
      windows = self.get_windows_sentence_inbound(test, window_size)
    return windows
  
  def survey_text(self, model, test, window_size):
    # ... for a sliding window of contiguous words of size window_size, get H[words] and H[word set] ...
    windows = self.get_windows(test, window_size)
    print("got windows!")
    logps_words = np.array([self.logp_words(list(window)) for window in list(windows)])
    windows = self.get_windows(test, window_size)
    print('got windows, again!')
    logps_word_sets = np.array([self.logp_word_set(list(window)) for window in list(windows)])
    H_words = -np.mean(logps_words)
    H_word_sets = -np.mean(logps_word_sets)
    return H_words, H_word_sets
    
  def sliding(self, iterable, n):
      assert n >= 0
      its = itertools.tee(iterable, n)
      for i, iterator in enumerate(its):
          for _ in range(i):
              try:
                  next(iterator)
              except StopIteration:
                  return zip([])
      return zip(*its)
    
class LMResultsBaseline(LMResults):
  def __init__(self, trained_model, test_text):
    assert trained_model.alpha == 0
    # assert len(output_file) > 0
    
    self.test_state = test_text.state
    self.trained_model = trained_model
    self.test_text = test_text
    self.zero_prob_ratios = []

  def get_results(self, output_file):
    start = time.time()
    h_words, h_wordset, zeros_permutations = [], [], []
    for i in range(1,6):
      h_words_current, h_wordset_current, zeros_permutations_current = self.survey_text(self.trained_model, self.test_text, i)
      print("h_words",h_words_current, "h_wordset", h_wordset_current, "zeros_permutations", zeros_permutations_current)
      h_words.append(h_words_current)
      h_wordset.append(h_wordset_current)
      zeros_permutations.append(zeros_permutations_current)

    d = { 'h_words': h_words, 'h_wordset': h_wordset, 'zeros_permutations': zeros_permutations}
    df = pd.DataFrame(data=d, dtype=np.float64)
    if self.test_state == "ordered":
      pd.DataFrame(df).to_csv(output_file)
      print("Done! Created "+output_file)
    else:
      pd.DataFrame(df).to_csv(output_file)
      print("Done! Created "+output_file)
    end = time.time()
    print(end-start)
    
    self.results = {"results_dict": d, "results_dataframe": df}

  def logp_word_set(self, tokens): 
      """Get plog sum of each tokens' permutations"""
      logprobs = [self.logp_words(reordered_tokens) for reordered_tokens in itertools.permutations(tokens)]
      # print([t for t in itertools.permutations(tokens)])
      if not logprobs:
          logprobs = [0]
      self.zero_prob_ratios.append(logprobs.count(-INF)/len(logprobs))
      return scipy.special.logsumexp(logprobs)
  
  def survey_text(self, model, test, window_size):
    self.zero_prob_ratios = []
    # ... for a sliding window of contiguous words of size window_size, get H[words] and H[word set] ...
    windows = self.get_windows(test, window_size)
    print("got windows!")
    logps_words = np.array([self.logp_words(list(window)) for window in list(windows)])
    windows = self.get_windows(test, window_size)
    print('got windows, again!')    
    logps_word_sets = np.array([self.logp_word_set(list(window)) for window in list(windows)])
    ratio_of_zeros_permuted_windows = np.mean(self.zero_prob_ratios)
    H_words = -np.mean(logps_words)
    H_word_sets = -np.mean(logps_word_sets)
    return H_words, H_word_sets, ratio_of_zeros_permuted_windows