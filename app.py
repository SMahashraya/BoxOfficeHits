import os
import json

import pandas as pd
import numpy as np

from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

movies = pd.read_csv("db/movies.csv")
movies.to_json(orient = "records")

json.dump(movies)
jsonfile.write('\n')