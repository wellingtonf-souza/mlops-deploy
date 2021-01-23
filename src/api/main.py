
from flask import Flask, request, jsonify
from flask_basicauth import BasicAuth
from textblob import TextBlob
import pickle as pkl
import pandas as pd
import os

model = pkl.load(open('models/model.pkl','rb'))

app = Flask(__name__)

app.config['BASIC_AUTH_USERNAME'] = os.environ.get('BASIC_AUTH_USERNAME')
app.config['BASIC_AUTH_PASSWORD'] = os.environ.get('BASIC_AUTH_PASSWORD')

basic_auth = BasicAuth(app)

@app.route('/')
def home():
    return 'API running with automated deploy'

@app.route('/sentiment/<frase>/')
def sentiment_analysis(frase):
    tb = TextBlob(frase)
    if tb.detect_language() != 'en':
        tb_en = tb.translate(to='en')
        polaridade = tb_en.sentiment.polarity 
    else:   
        polaridade = tb.sentiment.polarity
    return 'polaridad: {}'.format(polaridade)

@app.route('/house_price/',methods=['POST'])
@basic_auth.required
def house_price():
    content = request.get_json()
    df = [[content['tamanho'],content['ano'],content['garagem']]]
    value = model.predict(df)
    return jsonify({'value':float(value)})


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')