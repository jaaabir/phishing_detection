import pandas as pd 
import numpy as np 
from features.feature_extractor import extract_features as ef

df = pd.read_csv('dataset_phishing.csv')

def add_col(row):
    new_row = []
    for ind, i in enumerate(row):
        if ind == 35: new_row.append(0)
        new_row.append(i)

    return new_row

def update(url, output):
    if len(url) != len(output) : return 'url and output should have same number of indeces'
    for i in range(len(url)):
        rows = ef(url[i], output[i])
        row = add_col(rows)
        df.loc[len(df)] = row
    df.to_csv('dataset_phishing.csv',index = False)
    print('updated to the dataset_phishing.csv...')


def check_last_updated():
    print(df.tail())