from imdb import Cinemagoer
import json
import pprint
import api_query

pp = pprint.PrettyPrinter(indent=4)

cg = Cinemagoer()
movies = []

years = list(range(1990, 2021))
json_list = api_query.search_movies(years)

for j in json_list:
    #Iterate movies to get ID and then the reviews
    for m in j:
        movie_id = m['id'].replace('tt', '')
        movie = cg.get_movie(movie_id)
        pp.pprint(movie)
        cg.update(movie, info=['original title', 'votes', 'rating', 'reviews' ])

        #Some movies dosen't have review so we skip that ones
        try:
            movies.append( {'title':movie['original title'], 'reviews': movie['reviews']})
        except:
            pass

#Save json file 
with open('reviews_dump.json', 'w') as dump_file:
    json_string = json.dumps(movies)
    json.dump(movies, dump_file)
