from os import listdir
from os.path import isfile, join
import pandas as pd
import string
from pos_tagging import tagging
import re

# INPUT_PATH = 'input'
INPUT_PATH = 'input-2'
# OUTPUT_PATH = 'lemmatized'
OUTPUT_PATH = 'output_lemmatized'
# OUTPUT_PATH = 'output_significant'

def remove_punctuation(str):
    return "".join([c for c in str if c not in string.punctuation])

def clean_data(str):
    cleaned = str.lower().replace('\n', '').strip().replace('nbsp', '')
    cleaned = re.sub(r'\w*?[\W&[\S]]\w{0,10}', '', cleaned)
    cleaned = re.sub(r'@\w+', '', cleaned)
    # print(cleaned)
    cleaned_extra_spaces = ' '.join(cleaned.split())

    # print(cleaned_extra_spaces)
    if len(cleaned_extra_spaces):
        return remove_punctuation(cleaned_extra_spaces)
    else:
        return False



def main():
    # input_files = [file for file in listdir(INPUT_PATH) if isfile(join(INPUT_PATH, file))]
    input_files = ['train.csv']

    for i in range(len(input_files)):
        try:
            input_file = join(INPUT_PATH, input_files[i])
            output_file = join(OUTPUT_PATH, input_files[i])

            # df = pd.read_csv(input_file)
            df = pd.read_csv(input_file, header=None)
            # df["post"] = df["post"].apply(lambda x : clean_data(x))
            # df.iloc[:,6] = df.iloc[:,6].apply(lambda x : clean_data(x))
            df.iloc[:,6] = df.iloc[:,6].apply(lambda x : clean_data(x) if clean_data(x) else 'not')
            # df.iloc[:,0] = df.iloc[:,0].apply(lambda x : clean_data(x))


            output_arr = []

            # print(df["post"])
            # for post in df["post"]:
            for post in df.iloc[:,6]:
                # print(tagging(post))
                # print(post)
                output_arr.append(' '.join(tagging(post)))
                # return

            # df["data-id"] = df["user_id"].astype(str) + '-' + df["#"].astype(str)
            # df["data"] = output_arr
            df.iloc[:,6] = output_arr

            # print(df)

            # df.to_csv(output_file, index=False, columns=["data-id", "data"])
            df.to_csv(output_file, index=False)

            print("finished " + input_files[i])

        except Exception as e:
            print('ERROR in ' + input_files[i] + ": " + str(e))



main()




