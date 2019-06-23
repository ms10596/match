from flask import Flask, render_template
from flask import request
from flask_cors import CORS
import json
from release import Prediction

app = Flask(__name__)
app.debug = True
CORS(app)

@app.route('/', methods=['GET'])
def page():
    return render_template('home.html')


@app.route('/', methods=['POST'])
def process():
    article = request.form.get('article')
    x = Prediction()
    result = x.predict(article)
    return render_template('home.html', result=result)

@app.route('/extension', methods=['POST'])
def extension():
    article = request.get_json()
    x = Prediction()
    result = x.predict(article['txt'])
    return result

@app.route('/extension/simplify', methods=['POST'])
def simplification():
    article = request.get_json()
    x = Prediction()
    result = x.simplify(article['txt'])
    return render_template('home.html', result=result)


if __name__ == '_main__':
    app.run(debug=True)
