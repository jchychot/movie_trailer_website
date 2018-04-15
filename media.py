"""Defines the Movie class that contains the details of a movie."""


class Movie():
    """ This class provides a way to store movie related information.

     Attributes:
        tile (str): Title of the movie
        storyline (str): Short plot of the movie
        poster_image_url (str): Poster image URL
        trailer_youtube_url (str): Youtube trailer URL
        release_date (str): Movie relase date (USA)
    """

    # Movie class data structure
    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube, movie_release_date):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.release_date = movie_release_date

