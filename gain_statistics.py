import pandas as pd
import matplotlib.pyplot as plt

# INPUT_FILE = 'combined_csv.csv'
INPUT_FILE = 'output_lemmatized/texts.txt'
# INPUT_FILE = 'test.csv'
OUTPUT_FILE = 'statistics/train_lemmatized.scv'

dictionary = {}

def count(words):
    for word in words:
        if word in dictionary:
            dictionary[word] += 1
        else:
            dictionary.update({word: 1})

def main():
    df = pd.read_csv(INPUT_FILE)
    # df["data"].apply(lambda post: count(post.split()))
    # df.iloc[:,6].apply(lambda post: len(post) > 0 and count(post.split()))
    try:
        for post in df.iloc[:,0]:
            if isinstance(post, str):
                # print(type(post))
                count(post.split())
            else:
                print('else: ', type(post))
    except:
        print(type(post))


    # print(dictionary)
    # print([*dictionary.values()])
    # print([*dictionary.keys()])

    data = {'word': [*dictionary.keys()], 'count': [*dictionary.values()]}
    df_count = pd.DataFrame(data)
    df_count = df_count.sort_values(by='count', ascending=False)

    df_count.head(100).plot(x='word', y='count', kind='bar')
    plt.show()
    # print(df_count)
    # df_count.to_csv(OUTPUT_FILE, index=False, columns=["word", "count"])

main()




