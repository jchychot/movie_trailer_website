import media
import fresh_tomatoes
toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc" )
avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://youtu.be/5PSNL1qE6VY")
pulp_fiction = media.Movie("Pulp Fiction",
                           "Vincent Vega (John Travolta) and Jules Winnfield"
                           "(Samuel L. Jackson) are hitmen with a penchant for"
                           "philosophical discussions.",
                           "https://upload.wikimedia.org/wikipedia/en/3/3b/Pulp_Fiction_%281994%29_poster.jpg",
                           "https://www.youtube.com/watch?v=s7EdQ4FqbhY")
ghostbusters = media.Movie("Ghostbusters",
                           "After the members of a team of scientists"
                           " (Harold Ramis, Dan Aykroyd, Bill Murray) lose their cushy positions at a university in New"
                           " York City, they decide to become ghostbusters to wage a high-tech battle with the"
                           " supernatural for money. They stumble upon a gateway to another dimension, a doorway that"
                           " will release evil upon the city. The Ghostbusters must now save New York from complete"
                           " destruction.",
                           "https://upload.wikimedia.org/wikipedia/en/2/2f/Ghostbusters"
                           "_%281984%29_theatrical_poster.png",
                           "https://www.youtube.com/watch?v=BbGkEP9XwRk")
airplane = media.Movie("Airplane!",
                       "This spoof comedy takes shots at the slew of disaster movies that were released in the 70s."
                       " When the passengers and crew of a jet are incapacitated due to food poisoning, a rogue pilot"
                       " with a drinking problem must cooperate with his ex-girlfriend turned stewardess to bring the"
                       "plane to a safe landing.",
                       "https://upload.wikimedia.org/wikipedia/en/f/f5/Airplane%21.jpg",
                       "https://www.youtube.com/watch?v=rzRJWy-3_Dc")
caddyshack = media.Movie("Caddyshack",
                          "Danny Noonan (Michael O'Keefe), a teen down on his luck, works as a caddy at the"
                          " snob-infested Bushwood Country Club to raise money for his college education. In an attempt"
                          " to gain votes for a college scholarship reserved for caddies, Noonan volunteers to caddy"
                          " for a prominent and influential club member (Ted Knight). Meanwhile, Danny struggles to"
                          " prepare for the high pressure Caddy Day golf tournament while absorbing New Age advice from"
                          " wealthy golf guru Ty Webb (Chevy Chase).",
                          "https://upload.wikimedia.org/wikipedia/en/8/84/Caddyshack_poster.jpg",
                          "https://www.youtube.com/watch?v=x9Nl39uWEYk")

movies = [toy_story, avatar, pulp_fiction, ghostbusters, airplane, caddyshack]
movies.sort(key=lambda x: x.title,)
fresh_tomatoes.open_movies_page(movies)