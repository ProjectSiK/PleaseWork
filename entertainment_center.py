import fresh_tomatoes
import media

Devil_Wears_Prada = media.Movie("The Devil Wears Prada",
                                "A journalist joins the fashion world",
                                "https://s-media-cache-ak0.pinimg.com/736x/b7/7b/2f/b77b2f37d3f0dc33587edfb6ff7221f5.jpg",
                                "https://www.youtube.com/watch?v=LG0xYJJbko8")

Seven = media.Movie("Seven",
                    "A psychopath bases his kills off the seven deadly sins.",
                    "http://th03.deviantart.net/fs70/PRE/i/2012/181/6/5/seven_minimalist_poster_by_tchav-d55etn6.jpg",
                    "https://www.youtube.com/watch?v=J4YV2_TcCoE")

Fight_Club = media.Movie("Fight Club",
                         "A man joins a fight club...",
                         "http://alikamran.com/wp-content/uploads/2012/08/fight-club-alternative-poster06.jpeg",
                         "https://www.youtube.com/watch?v=SUXWAEX2jlg")

Alien = media.Movie("Alien",
                    "In space no one can hear you scream",
                    "http://th06.deviantart.net/fs70/PRE/f/2013/247/2/e/alien_by_stormy94-d6l1x9u.png",
                    "https://www.youtube.com/watch?v=bEVY_lonKf4")

American_Psycho = media.Movie("American Psycho",
                              "Normal guy, full blown killer",
                              "http://fc01.deviantart.net/fs70/f/2012/118/c/5/american_psycho_minimalist_movie_poster_by_carlitojay-d4xtfce.jpg",
                              "https://www.youtube.com/watch?v=2GIsExb5jJU")



Memento = media.Movie("Memento",
                      "Not what you think...",
                      "http://fc01.deviantart.net/fs71/i/2010/046/7/2/Minimalist_Memento_Poster_by_premedito.jpg",
                      "https://www.youtube.com/watch?v=0vS0E9bBSL0")

movies = (Devil_Wears_Prada, Seven, Fight_Club, Alien, American_Psycho, Memento)
fresh_tomatoes.open_movies_page (movies)
