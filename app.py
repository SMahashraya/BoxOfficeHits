from flask import Flask
from flask import render_template

import csv
import json

import numpy as np
import pandas as pd

app = Flask(__name__)