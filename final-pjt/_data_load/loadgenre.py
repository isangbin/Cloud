import requests
import json

def get_genre():
    url = 'https://api.themoviedb.org/3/genre/movie/list?api_key=e67fd4cae34071117f73a8090324311b&language=ko-KR'
    genres = requests.get(url).json()
    total_data = []
    
    for genre in genres['genres']:
        if genre.get('name', ''):
            fields = {
                'genre_id': genre['id'],
                'name': genre['name'],
            }
            data = {
                "pk": genre['id'],
                "model": "movies.genre",
                "fields": fields
            }

            total_data.append(data)

    with open("genre_data.json", "w", encoding="utf-8") as w:
        json.dump(total_data, w, indent="\t", ensure_ascii=False)

get_genre()