
class Movie():
    """ This class provides a way to store movie related information.

    Included movie title, poster image and the movies trailer from
    youtube.
    """

    # Movie class data structure
    def __init__(self, movie_title, poster_image, trailer_youtube):
        self.title = movie_title
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
