import requests
import json

def get_movie():
    url = 'https://api.themoviedb.org/3/movie/popular?api_key=e67fd4cae34071117f73a8090324311b&language=en-US'
    movies = requests.get(url).json()
    total_data = []

    for movie in movies['results']:
        if movie.get('release_date', ''):
            fields = {
                'movie_id': movie['id'],
                'title': movie['title'],
                'released_date': movie['release_date'],
                'popularity': movie['popularity'],
                'overview': movie['overview'],
                'poster_path': movie['poster_path'],
                'genres': movie['genre_ids'],
                # 'actors': movie[]
            }

            data = {
                "pk": movie['id'],
                "model": "movies.movie",
                "fields": fields
            }

            total_data.append(data)

    with open("movie_data.json", "a", encoding="utf-8") as a:
        json.dump(total_data, a, indent="\t", ensure_ascii=False)

get_movie()