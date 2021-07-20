from features.feature_extractor import extract_features as ef
import pandas as pd 
import numpy as np
import pickle
import warnings


warnings.filterwarnings('ignore')
df = pd.read_csv('dataset_phishing.csv')

def get_features(url):
    x = ef(url, 0)
    x = x[1:47] + x[50:-1] if x is not None else None
    print(x)
    return x

def pred(x, clf):
    x = np.array(x).reshape(1,-1) 
    
    return clf.predict(x)    

def predict(url, clf):
    replace = {
        'legitimate'  : 0,
        'phishing' : 1
    }

    result = df.status[df.url == url].replace(replace)
    if len(result) > 0:
        try:
            result = True if result.values[0] == 1 else False
        except KeyError as error:
            print('its an error :', error)
    else:
        x = get_features(url)
        if x == None or len(x) != 83 : return -1
        result = True if pred(x, clf)[0] == 'legitimate' else False
    return result

    
    