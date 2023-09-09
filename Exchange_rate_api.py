from flask import Flask, jsonify
from bs4 import BeautifulSoup
import requests

def get_curreny(in_currency,out_currency):
    url=f"https://www.x-rates.com/calculator/?from={in_currency}&to={out_currency}&amount=1"
    content = requests.get(url).text
    soup= BeautifulSoup(content,'html.parser')
    currency=soup.find('span',class_='ccOutputRslt').get_text().split(" ")[0]
    return currency

app=Flask(__name__)

@app.route('/')
def home():
    return '<h1>Currency Rate API</h1> <p>Example URL: /api/v1/usd-inr</p>'

@app.route('/api/v1/<in_curr>-<out_curr>')
def api(in_curr,out_curr):
    result={
        'input_currentcy':in_curr,
        'output_currency':out_curr,
        'rate':get_curreny(in_curr,out_curr)
        }
    return jsonify(result)
app.run()
