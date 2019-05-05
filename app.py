from flask import Flask
from flask import render_template
import csv
import numpy as np
import pandas as pd
import plotly.plotly as py
import plotly.graph_objs as go
import plotly.figure_factory as FF
import json

app = Flask(__name__)

movies = pd.read_csv("db/movies.csv")
movies.to_json(orient = "records")

if __name__ == '__main__':
    app.run(debug = True, use_reloader = True)