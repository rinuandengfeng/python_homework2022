from flask import Flask
import time

app = Flask(__name__)

@app.route('/lzw')
def index_lzw():
    time.sleep(2)
    return 'Hello lzw'

@app.route('/jay')
def index_jay():
    time.sleep(2)
    return 'Hello Jay'

@app.route('/tom')
def index_tom():
    time.sleep(2)
    return 'Hello tom'