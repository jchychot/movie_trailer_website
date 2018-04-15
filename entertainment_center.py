import media
import fresh_tomatoes


# Movie instances in library
#Toy Story
toy_story = media.Movie("Toy Story",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie("Avatar",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://youtu.be/5PSNL1qE6VY")

pulp_fiction = media.Movie("Pulp Fiction",
                           "https://upload.wikimedia.org/wikipedia/en/3/3b/Pulp_Fiction_%281994%29_poster.jpg",
                           "https://www.youtube.com/watch?v=s7EdQ4FqbhY")

ghostbusters = media.Movie("Ghostbusters",
                           "https://upload.wikimedia.org/wikipedia/en/2/2f/Ghostbusters"
                           "_%281984%29_theatrical_poster.png",
                           "https://www.youtube.com/watch?v=BbGkEP9XwRk")

airplane = media.Movie("Airplane!",
                       "https://upload.wikimedia.org/wikipedia/en/f/f5/Airplane%21.jpg",
                       "https://www.youtube.com/watch?v=rzRJWy-3_Dc")

caddyshack = media.Movie("Caddyshack",
                        "https://upload.wikimedia.org/wikipedia/en/8/84/Caddyshack_poster.jpg",
                        "https://www.youtube.com/watch?v=x9Nl39uWEYk")

# Group all the movies instances together in a sorted list
movies = [toy_story, avatar, pulp_fiction, ghostbusters, airplane, caddyshack]
movies.sort(key=lambda x: x.title,)

# Generate a website that displays these movies
fresh_tomatoes.open_movies_page(movies)