from os import error
from flask import Flask, render_template, request, url_for
from model import predict

app = Flask('__main__')


@app.route('/', methods = ['GET'])
def home():
    error = 0
    res = None
    if request.args:
        url = request.args['url_input']
        if 'http' in url:
            res = predict(url)
            error = 1 if res == -1 else 0
        else:
            error = 2

    return render_template('index.html', result = res, fname = 'index.css', error = error)

if __name__ == "__main__":
    app.run()