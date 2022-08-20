from imdb import Cinemagoer
import json
import pprint
import os
import requests

pp = pprint.PrettyPrinter(indent=4)

titles = ['inception', 'joker', 'toy story', 'harry potter']

cg = Cinemagoer()
movies = []

def get_id(movie_title):
    api_key = 'k_ifa2ua8e'

    url = f"https://imdb-api.com/en/API/SearchMovie/{api_key}/{movie_title}"
    
    payload = {}
    headers= {}
    
    response = requests.request("GET", url, headers=headers, data = payload)
    
    data = response.text 
    json_data = json.loads(data)

    return json_data['results'][0]['id']

#Iterate through files in folder and search reviews

for t in titles:
    id = get_id(t)
    movie_id = id.replace('tt', '')
    movie = cg.get_movie(movie_id)

    cg.update(movie, info=['original title', 'votes', 'rating', 'reviews' ])
    movies.append( {'title':movie['original title'], 'reviews': movie['reviews']})

#Save json file 
with open('reviews_dump_prueba.json', 'w') as dump_file:
    json_string = json.dumps(movies)
    json.dump(movies, dump_file)


