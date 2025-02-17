class Song:
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre

        # Increment song count
        Song.add_song_to_count()

        # Add to genres and update genre_count
        Song.add_to_genres(self.genre)

        # Add to artists and update artist_count
        Song.add_to_artists(self.artist)

    @classmethod
    def add_song_to_count(cls):
        cls.count += 1

    @classmethod
    def add_to_genres(cls, genre):
        if genre not in cls.genres:
            cls.genres.append(genre)
        # Update genre_count histogram
        if genre in cls.genre_count:
            cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre] = 1

    @classmethod
    def add_to_artists(cls, artist):
        if artist not in cls.artists:
            cls.artists.append(artist)
        # Update artist_count histogram
        if artist in cls.artist_count:
            cls.artist_count[artist] += 1
        else:
            cls.artist_count[artist] = 1



      
    
ninety_nine_problems = Song("99 Problems", "Jay Z", "Rap")
hello = Song("Hello", "Adele", "Pop")
rolling_in_the_deep = Song("Rolling in the Deep", "Adele", "Pop")

print(Song.count)  # Output: 3
print(Song.genres)  # Output: ['Rap', 'Pop']
print(Song.genre_count)  # Output: {'Rap': 1, 'Pop': 2}
print(Song.artists)  # Output: ['Jay-Z', 'Adele']
print(Song.artist_count)  # Output: {'Jay-Z': 1, 'Adele': 2}
