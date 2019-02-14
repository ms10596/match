from flask import Flask, render_template, request

from research.predict import Predict

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def hello_world():
    if request.method == 'GET':
        return render_template('Home.html')
    if request.method == 'POST':
        return Predict().predict_tag(request.form['text'])


if __name__ == '__main__':
    app.run()
    app.debug = True