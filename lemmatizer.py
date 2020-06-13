from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()

pos_dict = {'V': 'v', 'J': 'a', 'N': 'n', 'R': 'r'}


def filter_pos(pos):
    return


def lemmatize(words_arr):
    lemmas_arr = []
    try:
        for word_tuple in words_arr:
            word = word_tuple[0]
            pos = word_tuple[1]

            if pos[0] in pos_dict.keys():
                lemma = lemmatizer.lemmatize(word, pos = pos_dict[pos[0]])
                # print(word, lemma, pos, pos_dict[pos[0]])
                lemmas_arr.append(lemma)
            else:
                # print(word_tuple)
                lemmas_arr.append(word)
    except:
        print(word_tuple)

    return lemmas_arr

