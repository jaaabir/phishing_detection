from sklearn.preprocessing import StandardScaler as ss 
from sklearn.svm import SVC
import numpy as np 
import pandas as pd 
from sklearn.pipeline import Pipeline
import pickle

df = pd.read_csv('dataset_phishing.csv')
df = df.drop(['url','random_domain','avg_words_raw', 'avg_word_host', 'avg_word_path'], axis = 1)
print(f"dataset shape : {df.shape}")
x = df.drop(['status'], axis = 1)
print(f"x shape : {x.shape}")
y = df.status

std_scaler = ss()
pipeline = Pipeline(steps = [('std', std_scaler), ('svm', SVC(C=10))])
pipeline.fit(x,y)
print('Trained the model...')

with open('svmModel', 'wb') as file:
    pickle.dump(pipeline, file)

print('Saved the model...')
