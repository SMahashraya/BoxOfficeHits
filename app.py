from flask import Flask
from flask import render_template
app = Flask(__name__)
import csv
import pandas as pd
import numpy as np
import json

def get_csv():
    csv_path = './db/movies.csv'
    csv_file = open(csv_path, 'r')
    csv_obj = csv.DictReader(csv_file)
    csv_list = list(csv_obj)
    return csv_list

@app.route("/")
def index():
    object_list = get_csv()
    return render_template('index.html', object_list = object_list)

@app.route("/<Movie_Title>/")
def detail(row_id):
    movieList = get_csv()
    for movie in movieList:
        if movie['Movie_Title'] == movie.Movie_Title:
            return render_template('index.html', object = movie)

if __name__ == '__main__':
    app.run(debug = True, use_reloader = True)