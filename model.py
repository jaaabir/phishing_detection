from features.feature_extractor import extract_features as ef
import pandas as pd 
import numpy as np
# from sklearn.preprocessing import RobustScaler as rbs
# from sklearn.ensemble import RandomForestClassifier as rfc
from features.feature_extractor import extract_features as ef
import pickle
import warnings


warnings.filterwarnings('ignore')
# rb_scaler = rbs()
df = pd.read_csv('dataset_phishing.csv')

def get_features(url):
    x = ef(url, 0)
    x = x[1:47] + x[50:-1] if x is not None else None
    return x

def pred(x):
    x = np.array(x).reshape(1,-1) 
    with open('rfcModel','rb') as file:
        clf = pickle.load(file)
    
    return clf.predict(x)    

def predict(url):
    replace = {
        'legitimate'  : 0,
        'phishing' : 1
    }

    result = df.status[df.url == url].replace(replace)
    if len(result) > 0:
        result = True if result[0] == 1 else False
    else:
        x = get_features(url)
        if x == None or len(x) != 83 : return -1
        result = True if pred(x)[0] == 'legitimate' else False
    return result

    
    