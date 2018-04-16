"""Stores details of movies and displays them on a website."""
import media
import fresh_tomatoes


# Main function to create movie instances amd open web page
def main():
    """ Creates movie library consisting of including movie title,
    box art URL (or poster URL) and a YouTube link to the movie trailer.
    """
    toy_story = media.Movie("Toy Story",
                            "A story of a boy and his toys that come to life",
                            "https://upload.wikimedia.org/wikipedia/en/1/13/"
                            "Toy_Story.jpg",
                            "https://www.youtube.com/watch?v=KYz2wyBy3kc",
                            "22 November 1995")

    avatar = media.Movie("Avatar",
                         "A marine on an alien planet",
                         "https://upload.wikimedia.org/wikipedia/en/b/b0/"
                         "Avatar-Teaser-Poster.jpg",
                         "https://youtu.be/5PSNL1qE6VY",
                         "18 December 2009")

    pulp_fiction = media.Movie("Pulp Fiction",
                               "Hitmen with a penchant for philosophical"
                               " discussions.",
                               "https://upload.wikimedia.org/wikipedia/en/3/"
                               "3b/Pulp_Fiction_%281994%29_poster.jpg",
                               "https://www.youtube.com/watch?v=s7EdQ4FqbhY",
                               "14 October 1994")

    ghostbusters = media.Movie("Ghostbusters",
                               "Three former parapsychology professors set up"
                               " shop as a unique ghost removal service.",
                               "https://upload.wikimedia.org/wikipedia/en/2/"
                               "2f/Ghostbusters"
                               "_%281984%29_theatrical_poster.png",
                               "https://www.youtube.com/watch?v=BbGkEP9XwRk",
                               "8 June 1984")

    airplane = media.Movie("Airplane!",
                           "A man afraid to fly must ensure that a plane lands"
                           " safely.",
                           "https://upload.wikimedia.org/wikipedia/en/f/f5/"
                           "Airplane%21.jpg",
                           "https://www.youtube.com/watch?v=rzRJWy-3_Dc",
                           "2 July 1980")

    caddyshack = media.Movie("Caddyshack",
                             "An exclusive golf course has to deal with a"
                             " brash new member.",
                             "https://upload.wikimedia.org/wikipedia/en/8/84/"
                             "Caddyshack_poster.jpg",
                             "https://www.youtube.com/watch?v=x9Nl39uWEYk",
                             "25 July 1980")

    # Group all the movies instances together in a sorted list
    movies = [toy_story, avatar, pulp_fiction,
              ghostbusters, airplane, caddyshack]
    movies.sort(key=lambda x: x.title,)

    # Generate a website that displays these movies
    fresh_tomatoes.open_movies_page(movies)

# Run Main
if __name__ == "__main__":
    main()
