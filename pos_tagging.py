import nltk
from nltk.corpus import stopwords
from nltk.tokenize import TreebankWordTokenizer
from lemmatizer import lemmatize

stop_words = set(stopwords.words('english'))


def tagging(txt):
    tokenized = TreebankWordTokenizer().tokenize(txt)

    # print("tokenized: ", tokenized)
    wordsList = [w for w in tokenized if not w in stop_words]

    tagged = nltk.pos_tag(wordsList)

    return lemmatize(tagged)