from flask import Flask, render_template, request

from research.FF.predict import predict_tag

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def hello_world():
    if request.method == 'GET':
        return render_template('Home.html')
    if request.method == 'POST':
        return """<p style="font-size:100px">"""+predict_tag(request.form['text'])+"</p>"


if __name__ == '__main__':
    app.run()
    app.debug = True
