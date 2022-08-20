import requests
import json

def search_movies(years):    
    json_data_all = []

    for y in years:
        #Call to IMDB API searching movies released between 2010 and 2020
        api_key = 'k_ifa2ua8e'

        url = f"https://imdb-api.com/API/AdvancedSearch/{api_key}?title_type=feature,tv_movie&release_date={y}-01-01,{y}-12-31&count=500&sort=year,asc"

        payload = {}
        headers= {}

        response = requests.request("GET", url, headers=headers, data = payload)

        #Convert API response to JSON 
        data = response.text 
        json_data = json.loads(data)

        results = json_data['results']
        json_data_all.append(results)

    return json_data_all

#Save JSON 
#with open('movies_2010_2020.json', 'w') as dump_file:
#    json_string = json.dumps(json_data_all)
#    json.dump(json_data_all, dump_file)