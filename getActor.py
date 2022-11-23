
import requests
import json

TMDB_API_KEY = 'a6cf97bd4b454c941b8d86091ec398b5'
movie_id = ''
# TMDB_API_KEY = str(os.getenv('TMDB_API_KEY'))

def get_movie_datas():
    total_data = []

 

    request_url = f"https://api.themoviedb.org/3/movie/{movie_id}/credits?api_key={TMDB_API_KEY}&language=en-US"
    movies = requests.get(request_url).json()

    for movie in movies['results']:
        if movie.get('release_date', ''):
            fields = {
                'movie_id': movie['id'],
                'title': movie['title'],
                'released_date': movie['release_date'],
                'popularity': movie['popularity'],
                'vote_avg': movie['vote_average'],
                'overview': movie['overview'],
                'poster_path': movie['poster_path'],
                'genres': movie['genre_ids']
            }

            data = {
                "pk": movie['id'],
                "model": "movies.trend",
                "fields": fields
            }

            total_data.append(data)
    print(total_data)
            
    with open("trend_data.json", "w", encoding="utf-8") as w:
        json.dump(total_data, w, indent="  ", ensure_ascii=False)

get_movie_datas()