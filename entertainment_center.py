import fresh_tomatoes
import media

""" These are the instance objects of the Movie Class """
toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life.",
                        "https://upload.wikimedia.org/wikipedia/en/thumb/1/13"
                        "/Toy_Story.jpg/220px-Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=vwyZH85NQC4")

avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "https://images-na.ssl-images-amazon.com/images/M"
                     "/MV5BMTYwOTEwNjAzMl5BMl5BanBnXkFtZTcwODc5MTUwMw@@"
                     "._V1_.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")

hackers = media.Movie("Hackers",
                      "Hack the planet!",
                      "https://images-na.ssl-images-amazon.com/images/M"
                      "/MV5BODg0NjQ5ODQ3OF5BMl5BanBnXkFtZTcwNjU4MjkzNA@"
                      "@._V1_UX182_CR0,0,182,268_AL_.jpg",
                      "https://www.youtube.com/watch?v=Rn2cf_wJ4f4")

pirates = media.Movie("Pirates of Silicon Valley",
                      "History of Apple and Microsoft",
                      "https://images-na.ssl-images-amazon.com/images/M"
                      "/MV5BNDc2NTE0NzE4N15BMl5BanBnXkFtZTgwMDQ5MzgwMzE"
                      "@._V1_.jpg",
                      "https://www.youtube.com/watch?v=lEyrivrjAuU")

wargames = media.Movie("WarGames",
                       "A young man finds a back door into a military central "
                       "computer in which reality is confused wit"
                       "h game-playing, possibly starting World War III.",
                       "https://images-na.ssl-images-amazon.com/images/M"
                       "/MV5BMTMyMTE3OTk3NF5BMl5BanBnXkFtZTcwOTkwNDc3NA"
                       "@@._V1_SY1000_CR0,0,666,1000_AL_.jpg",
                       "https://www.youtube.com/watch?v=hbqMuvnx5MU")

sneakers = media.Movie("Sneakers",
                       "A security pro finds his past coming back to haunt "
                       "him, when he and his unique team are tasked "
                       "with retrieving a particularly important item.",
                       "https://images-na.ssl-images-amazon.com/images/M"
                       "/MV5BYWM2OWI0OTAtYTVlOC00YTA0LTllMTItNWM5OTIwZD"
                       "JlYWFmXkEyXkFqcGdeQXVyNDk3NzU2MTQ@._V1_SY1000_CR0,0,"
                       "666,1000_AL_.jpg",
                       "https://www.youtube.com/watch?v=G_XRqJV2zdk")

""" This array is the collection of movie objects used to build the html view 
in index.html"""
movies = [toy_story, avatar, hackers, pirates, wargames, sneakers]
fresh_tomatoes.open_movies_page(movies)
