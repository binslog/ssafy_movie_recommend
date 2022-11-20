
import requests
import json

TMDB_API_KEY = 'a6cf97bd4b454c941b8d86091ec398b5'

# TMDB_API_KEY = str(os.getenv('TMDB_API_KEY'))

def get_genre_datas():
    total_data = []

    # 1페이지부터 500페이지까지 (페이지당 20개, 총 10,000개)
    
    request_url = f"https://api.themoviedb.org/3/genre/movie/list?api_key={TMDB_API_KEY}&language=en-US"
    genres = requests.get(request_url).json()
    # print(genres)
    # print(genres['genres'])
    for genre in genres['genres']:
    
        fields = {
            'genre_id' : genre['id'],
            'name': genre['name']
        }

        data = {
            "pk": genre['id'],
            "model": "movies.genre",
            "fields": fields
        }

        total_data.append(data)

    with open("genre_data.json", "w", encoding="utf-8") as w:
        json.dump(total_data, w, indent=" ", ensure_ascii=False)

get_genre_datas()
