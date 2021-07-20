from os import error
from flask import Flask, render_template, request, url_for
from model import predict
import pickle

# app = Flask('__main__')
app = Flask(__name__, template_folder='templates')
print(f'templates folder path : {app.template_folder}')
with open('rfcModel','rb') as file:
    clf = pickle.load(file)

@app.route('/', methods = ['GET'])
def home():
    error = -1
    res = None
    base_url =  None
    if request.args:
        url = request.args['url_input']
        if 'http' in url:
            res = predict(url, clf)
            base_url = url.split('/')[2]
            error = 1 if res == -1 else 0
        else:
            error = 2

    return render_template('index.html', result = res, fname = 'index.css', error = error, url = base_url)

if __name__ == "__main__":
    app.run(threaded = True, debug=True)