import nltk
import jieba
from spacy.tokenizer import Tokenizer
from spacy.lang.nl import Dutch
from random import shuffle
# from download_local_gutenberg_texts import *

class ModulateText:
    def __init__(self, text, state="ordered inbound", randomize_within_sentence=False, randomize_across_sentence=False, language="english", parse_type="by character"):
        self.text = text
        self.language = language
        # if language == "english":
        #     language = "english"

        # elif language == "turkish":
        #     language = "turkish"

        # elif language == "dutch":
        #     language = "dutch"
            
        self.tokens = [token.casefold() for token in nltk.tokenize.word_tokenize(text, language=language) if token.isalnum()]
        self.state = state

        if randomize_within_sentence:
            sent_detector = nltk.data.load('tokenizers/punkt/'+language+'.pickle')
            sentences = sent_detector.tokenize(text.strip(), realign_boundaries=False)
            final_randomized_tokens = []
            for sentence in sentences:
              sentence_tokens = [token.casefold() for token in nltk.tokenize.word_tokenize(sentence, language=language) if token.isalnum()]
              shuffle(sentence_tokens)
              final_randomized_tokens += sentence_tokens+['.']
            text_randomized = " ".join(final_randomized_tokens)
            self.tokens = final_randomized_tokens
            self.state = "random inbound"
            
        if randomize_across_sentence:
            tokens = [token.casefold() for token in nltk.tokenize.word_tokenize(text, language=language) if token.isalnum()]
            shuffle(tokens)
            self.tokens = tokens
            self.state = "random outbound"

        # elif language == "dutch":
        #     nlp = Dutch()
        #     nlp.add_pipe(nlp.create_pipe('sentencizer'))
        #     doc = nlp(text)
            
        #     tokenizer = Tokenizer(nlp.vocab)
        #     # self.tokens = [str(token) for token in tokenizer(text)]
        #     self.tokens = [token.casefold() for token in nltk.tokenize.word_tokenize(text, language="dutch") if token.isalnum()]
        #     self.state = "ordered"

        #     if randomize_within_sentence:
        #         sentences = [str(sent) for sent in list(doc.sents)]
        #         final_randomized_tokens = []
        #         for sentence in sentences:
        #           sentence_tokens = tokenizer(sentence)
        #           shuffle(sentence_tokens)
        #           final_randomized_tokens += sentence_tokens+['.']
        #         text_randomized = " ".join(final_randomized_tokens)
        #         self.random_tokens = final_randomized_tokens
        #         self.state = "random within sentence"
                
        #     if randomize_across_sentence:
        #         tokens = [str(token) for token in tokenizer(text)]
        #         shuffle(tokens)
        #         self.random_tokens = tokens
        #         self.state = "random across sentence"

        if language == "chinese" and parse_type == "by character":
            tokens = [token for token in jieba.cut(text, cut_all=True)]
            tokens = [str(token) for token in tokens]
            self.tokens = tokens
            self.state = "ordered within sentence"

            if randomize_across_sentence:
                shuffle(tokens)
                self.tokens = tokens
                self.state = "random across sentence"

        elif language == "chinese" and parse_type == "by word":
            tokens = [token for token in jieba.cut(text, cut_all=False)]
            tokens = [str(token) for token in tokens]
            self.tokens = tokens
            self.state = "ordered"

            if randomize_across_sentence:
                shuffle(tokens)
                self.tokens = tokens
                self.state = "random across sentence"
            
            
    
                
