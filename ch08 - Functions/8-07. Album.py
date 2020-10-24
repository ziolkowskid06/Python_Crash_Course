"""
Write a function called make_album() that builds a dictionary describing a music album.
"""


def make_album(name, album, songs=None):
    """Create a music dictionary."""
    if songs:
        music_album = {
            'name': name.title(),
            'album': album.title(),
            'songs': songs,
        }
        return music_album
    else:
        music_album = {
            'name': name.title(),
            'album': album.title(),
        }
        return music_album


x = make_album('50 Cent', 'Get Rich or Die Trying', 18)
print(x)
