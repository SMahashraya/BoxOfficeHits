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

# fieldnames = ("close","movie_title","opening_theaters","opening_day_date",
# "opening_gross_amount","rank","studio","total_theaters","total_gross","year",
# "title","rated","released","runtime_in_min","genre","director","writer","actors",
# "plot","language","country","awards","poster","ratings","metascore","imdbrating",
# "imdbvotes","imdbid","dvd","boxoffice","production","website","action","adventure",
# "animation","biography","comedy","crime","documentary","drama","family","fantasy",
# "film_noir","history","horror","music","musical","mystery","romance","sci-fi","short",
# "sport","superhero","thriller","war","western","actors_avg_total_gross",
# "actors_avg_number_of_movies","actors_avg_best_picture_gross","director_total_gross",
# "director_number_of_movies","director_best_picture_gross","title_negative_sentiment",
# "title_neutral_sentiment","title_positive_sentiment","title_compound_sentiment",
# "poster_color","black","white","gray","red","yellow","green","cyan","blue","magenta",
# "rotten_tomatoes_score")

# with open ('db/movies.csv', 'r') as csvfile:
#     with open ('db/movies.csv', 'w') as jsonfile:
#         next(csvfile)
#         reader = csv.DictReader(csvfile, fieldnames)
#         movies = {}
#         for row in reader:
#             movies = {

#             }

# def get_csv():
#     csv_path = './db/movies.csv'
#     csv_file = open(csv_path, 'r')
#     csv_obj = csv.DictReader(csv_file)
#     csv_list = list(csv_obj)
#     return csv_list

# @app.route("/")
# def index():
#     object_list = get_csv()
#     return render_template('index.html', object_list = object_list)

# @app.route("/<Movie_Title>/")
# def detail(row_id):
#     movieList = get_csv()
#     for movie in movieList:
#         if movie['Movie_Title'] == movie.Movie_Title:
#             return render_template('index.html', object = movie)

if __name__ == '__main__':
    app.run(debug = True, use_reloader = True)