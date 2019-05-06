import os
import csv
import json

from flask import Flask
from flask import render_template

app = Flask(__name__)

fieldnames = ("close","movie_title","opening_theaters","opening_day_date",
"opening_gross_amount","rank","studio","total_theaters","total_gross","year",
"title","rated","released","runtime_in_min","genre","director","writer","actors",
"plot","language","country","awards","poster","ratings","metascore","imdbrating",
"imdbvotes","imdbid","dvd","boxoffice","production","website","action","adventure",
"animation","biography","comedy","crime","documentary","drama","family","fantasy",
"film_noir","history","horror","music","musical","mystery","romance","sci-fi","short",
"sport","superhero","thriller","war","western","actors_avg_total_gross",
"actors_avg_number_of_movies","actors_avg_best_picture_gross","director_total_gross",
"director_number_of_movies","director_best_picture_gross","title_negative_sentiment",
"title_neutral_sentiment","title_positive_sentiment","title_compound_sentiment",
"poster_color","black","white","gray","red","yellow","green","cyan","blue","magenta",
"rotten_tomatoes_score")

with open ('db/movies.csv', 'r') as csvfile:
    with open ('db/movies.json', 'w') as jsonfile:
        reader = csv.DictReader(csvfile, fieldnames)
        movies = {}
        for row in reader:
            movies[row["movie_title"]] = {
                "close": ["close"],
                "opening_theaters": ["opening_theaters"],
                "opening_day_date": ["opening_day_date"],
                "opening_gross_amount": ["opening_gross_amount"],
                "rank": ["rank"],
                "studio": ["studio"],
                "total_theaters": ["total_theaters"],
                "total_gross": ["total_gross"],
                "year": ["year"],
                "rated": ["rated"],
                "released": ["released"],
                "runtime_in_min": ["runtime_in_min"],
                "genre": ["genre"],
                "director": ["director"],
                "writer": ["writer"],
                "actors": ["actors"],
                "plot": ["plot"],
                "language": ["language"],
                "country": ["country"],
                "awards": ["awards"],
                "poster": ["poster"],
                "ratings": ["ratings"],
                "metascore": ["metascore"],
                "imdbrating": ["imdbrating"],
                "imdbvotes": ["imdbvotes"],
                "imdbid": ["imdbid"],
                "dvd": ["dvd"],
                "boxoffice": ["boxoffice"],
                "production": ["production"],
                "website": ["website"],
                "action": ["action"],
                "adventure": ["adventure"],
                "animation": ["animation"],
                "biography": ["biography"],
                "comedy": ["comedy"],
                "crime": ["crime"],
                "documentary": ["documentary"],
                "drama": ["drama"],
                "family": ["family"],
                "fantasy": ["fantasy"],
                "film_noir": ["film_noir"],
                "history": ["history"],
                "horror": ["horror"],
                "music": ["music"],
                "musical": ["musical"],
                "mystery": ["mystery"],
                "romance": ["romance"],
                "sci-fi": ["sci-fi"],
                "short": ["short"],
                "sport": ["sport"],
                "superhero": ["superhero"],
                "thriller": ["thriller"],
                "war": ["war"],
                "western": ["western"],
                "actors_avg_total_gross": ["actors_avg_total_gross"],
                "actors_avg_number_of_movies": ["actors_avg_number_of_movies"],
                "actors_avg_best_picture_gross": ["actors_avg_best_picture_gross"],
                "director_total_gross": ["director_total_gross"],
                "director_number_of_movies": ["director_number_of_movies"],
                "director_best_picture_gross": ["director_best_picture_gross"],
                "title_negative_sentiment": ["title_negative_sentiment"],
                "title_neutral_sentiment": ["title_neutral_sentiment"],
                "title_positive_sentiment": ["title_positive_sentiment"],
                "title_compound_sentiment": ["title_compound_sentiment"],
                "poster_color": ["poster_color"],
                "black": ["black"],
                "white": ["white"],
                "gray": ["gray"],
                "red": ["red"],
                "yellow": ["yellow"],
                "green": ["green"],
                "cyan": ["cyan"],
                "blue": ["blue"],
                "magenta": ["magenta"],
                "rotten_tomatoes_score": ["rotten_tomatoes_score"]
            }
        json.dump(movies, jsonfile)
        jsonfile.write('\n')