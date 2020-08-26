import nltk
import jieba
from spacy.tokenizer import Tokenizer
from spacy.lang.nl import Dutch
from random import shuffle
from lemmatizer import *
# from hungarian_tokens_sents import *
# from download_local_gutenberg_texts import *
nltk.download('punkt')
class ModulateText:
    def __init__(self, text, state="ordered inbound", randomize_within_sentence=False, randomize_across_sentence=False, language="english", parse_type="by character", lemmatize=False, id_hungarian=""):
        self.text = text
        self.language = language

        if language == "hungarian" and state == "ordered inbound":
            self.tokens = get_hungarian_tokens(id_hungarian)
            self.state = state
            self.id_hungarian = id_hungarian

        elif language == "hungarian":
            tokens = get_hungarian_tokens(id_hungarian)
            shuffle(tokens)
            self.tokens = tokens
            self.state = state
            self.id_hungarian = id_hungarian

        elif language != "chinese":
            if language == "turkish" and lemmatize is True: 
                self.tokens = [get_lemmas(token.casefold(), 1)[0] for token in nltk.tokenize.word_tokenize(text, language=language) if token.isalnum()]
                print(self.tokens[:20])
            else:
                self.tokens = [token.casefold() for token in nltk.tokenize.word_tokenize(text, language=language) if token.isalnum()]
            self.state = state

            if randomize_within_sentence:
                sent_detector = nltk.data.load('tokenizers/punkt/'+language+'.pickle')
                sentences = sent_detector.tokenize(text.strip(), realign_boundaries=False)
                final_randomized_tokens = []
                for sentence in sentences:
                    if language == "turkish" and lemmatize is True:
                        sentence_tokens = [get_lemmas(token.casefold(), 1)[0] for token in nltk.tokenize.word_tokenize(sentence, language=language) if token.isalnum()]
                        print(self.tokens[:20])
                    else:
                        sentence_tokens = [token.casefold() for token in nltk.tokenize.word_tokenize(sentence, language=language) if token.isalnum()]
                    shuffle(sentence_tokens)
                    final_randomized_tokens += sentence_tokens+['.']
                text_randomized = " ".join(final_randomized_tokens)
                self.tokens = final_randomized_tokens
                self.state = "random inbound"
                
            if randomize_across_sentence:
                if language == "turkish" and lemmatize is True:
                    sentence_tokens = [get_lemmas(token.casefold(), 1)[0] for token in nltk.tokenize.word_tokenize(sentence, language=language) if token.isalnum()]
                    print(self.tokens[:20])
                else:
                    sentence_tokens = [token.casefold() for token in nltk.tokenize.word_tokenize(sentence, language=language) if token.isalnum()]
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
            tokens = [str(token) for token in new_tokens]
            self.tokens = tokens
            self.state = state

            if randomize_across_sentence:
                shuffle(tokens)
                self.tokens = tokens
                self.state = "random outbound"

        elif language == "chinese" and parse_type == "by word":
            tokens = [token for token in jieba.cut(text, cut_all=False)]
            tokens = [str(token) for token in tokens]
            self.tokens = tokens
            self.state = state

            if randomize_across_sentence:
                shuffle(tokens)
                self.tokens = tokens
                self.state = "random outbound"
            
            
    
                
