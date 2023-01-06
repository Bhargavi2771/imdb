import IMDb

#top 10 movies

ia=imdb.imdb()
search=ia.get_top250_movies()
for i in range(10):
    print(search[i])

    ia.search_movie ("simha")

def detail(movie_name):
   moviesDB = imdb.imdb()
   movies = moviesDB.search_movie(movie_name)

   if movies:
      id = movies(0).getid()
      movie=moviesDB.get_movies(id)

      print("movie details.....")

      print(f"{movie['title']}:{movie['year']}")
      print(f"rating : {movie['rating']}")

      directors = movie['director']
      casting = movie['cast']

      directors=''.join(map(str , directors))
      print(f"directors : {directors}")
      actors = ",".join(map(str , casting[0:5]))
      print(f"actors ; (actors)")

movie_name = input("Enter the movie name......")
detail(movie_name)
