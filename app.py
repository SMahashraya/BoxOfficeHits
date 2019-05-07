import csv, json

f = open( 'db/movies.csv', 'r')
reader = csv.DictReader( f, fieldnames = ("close","movie_title","opening_theaters","opening_day_date",
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
"rotten_tomatoes_score"))

store = []
framenames = []

for row in reader: 
    frame = {"Movie Title": row["movie_title"], 
    "IMDB id": row["imdbid"], 
    "Opening Gross": row["opening_gross_amount"], 
    "Opening Date": row["opening_day_date"], 
    "Rotten Tomatoes Score": row["rotten_tomatoes_score"]}

    if row["movie_title"] not in framenames:
        framenames.append(row["movie_title"])
        store.append(frame)

f = open( 'movies.json', 'w')

out = json.dumps(store, indent = 4)
f.write(out)
# score = {"rotten_tomatoes_score": ""}

# for frame in store:
#     f = open( 'movies.csv', 'rU' )
#     reader = csv.DictReader( f, fieldnames = ("close","movie_title","opening_theaters","opening_day_date",
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
# "rotten_tomatoes_score"))

# for row in reader:
#     if frame["Movie Title"] == row["movie_title"]:
#         if score["Rotten Tomatoes Score"] != row["rotten_tomatoes_score"]:
#             score = {
                
#             }