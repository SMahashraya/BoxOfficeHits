from flask import Flask
from flask import render_template

import csv
import json

import numpy as np
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', data = 'movies.json')
    
if __name__ == '__main__':
    app.run(debug = True, use_reloader = True)