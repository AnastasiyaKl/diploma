import pandas as pd
from os import listdir
from os.path import isfile, join

INPUT_PATH = 'lemmatized'


input_files = [(join(INPUT_PATH, file)) for file in listdir(INPUT_PATH) if isfile(join(INPUT_PATH, file))]
print(input_files)

combined_csv = pd.concat([pd.read_csv(f) for f in input_files ])
combined_csv.to_csv( "combined_csv.csv", index=False)