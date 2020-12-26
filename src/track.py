class Track:
    """ This represents one music """

    def __init__(self, name, id, artist):
        self.name = name
        self.id = id
        self.artist = artist


    def create_spotify_url(self):
        return f"spotify:track:{self.id}"

    def __str__(self):
        return self.name + "by " + self.artist
       