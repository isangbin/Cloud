import requests
import json

def get_movie():
    total_data = []
    for j in range(1, 11):
        for i in range(1+50*(j-1), 51+50*(j-1)):
            url = f"https://api.themoviedb.org/3/movie/popular?api_key=e67fd4cae34071117f73a8090324311b&language=ko-KR&page={i}>"
            movies = requests.get(url).json()

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
                        'vote_average': movie['vote_average'],
                    }

                    data = {
                        "pk": movie['id'],
                        "model": "movies.movie",
                        "fields": fields
                    }

                    total_data.append(data)

            with open(f"movie_data_{j}.json", "w", encoding="utf-8") as w:
                json.dump(total_data, w, indent="\t", ensure_ascii=False)

get_movie()