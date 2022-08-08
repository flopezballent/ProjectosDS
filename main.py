from imdb import Cinemagoer
import pandas as pd
import numpy as np
import json

import pprint
pp = pprint.PrettyPrinter(indent=4)


cg = Cinemagoer()
movies = []



imdb_file = open('mostPopular.json')
json_imdb = json.load(imdb_file)

i = 0

for m in json_imdb['items']:

    movie_id = m['id'].replace('tt', '')
    movie = cg.get_movie(movie_id)

    cg.update(movie, info=['original title', 'votes', 'rating', 'reviews' ])
    movies.append( {'title':movie['original title'], 'reviews': movie['reviews']})
    break



with open('movie_dump_popular.json', 'w') as dump_file:

    json_string = json.dumps(movies)
    json.dump(movies, dump_file)
