from flask import Flask
from flask import render_template
app = Flask(__name__)
import csv

def get_csv():
    p = './db/movies.csv'
    f = open(p, 'r')
    return list(csv.DictReader(f))

@app.route("/")
def index():
    template = './template/index.html'
    movieList = get_csv()
    return render_template(template, movies = movieList)

@app.route("/<Movie_Title>/")
def detail(row_id):
    template = './template/index.html'
    movieList = get_csv()
    for movie in movieList:
        if movie['Movie_Title'] == movie.Movie_Title:
            return render_template(template, object = movie)

if __name__ == '__main__':
    app.run(debug = True, use_reloader = True)