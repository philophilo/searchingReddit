from nltk.stem import WordNetLemmatizer
from nltk.stem.porter import PorterStemmer
from nltk.tokenize import sent_tokenize, TreebankWordTokenizer
import itertools
import string


class Term(object):
    def __init__(self, full_word):
        self.full_word = full_word
        #TODO: lematization requires downloads
        #wnl = WordNetLemmatizer
        #lemmas = [wnl.lemmatze(token) for token in tokens]
        self.stem= PorterStemmer().stem(full_word).lower()

def is_punctuation(stem):
        return stem in string.punctuation

def stem_and_tokenize_text(text):
    sents = sent_tokenize(text)
    tokens = list(itertools.chain(*[TreebankWordTokenizer().tokenize(sent) for sent in sents]))
    #terms = [Term(token) for token in tokens]
    #print "--", filter(Term.is_punctuation, terms)
    print "===", tokens
    return filter(lambda t: not is_punctuation(t), tokens)

def query_terms(query_row):
# in case query and doc require different processing in the future
    print ">>>...", stem_and_tokenize_text(query_row)
    return stem_and_tokenize_text(query_row)

def doc_terms(doc_row):
    return stem_and_tokenize_text(query_row)
# in case query and doc require different processing in the future
