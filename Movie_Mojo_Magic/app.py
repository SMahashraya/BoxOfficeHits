import pandas as pd
import numpy as np
import json
from flask import Flask, render_template
import plotly
import plotly.graph_objs as go

app = Flask(__name__)

@app.route("/")
def index():
    df = pd.read_csv("db/movies.csv")
    chart_data = df.to_dict(orient = "records")
    chart_data = json.dumps(chart_data, indent = 2)
    data = {"chart_data": chart_data}
    return render_template("index.html", data=data)

# @app.route("/<year>")
# def year(data):

if __name__ == "__main__":
    app.run(debug=True)