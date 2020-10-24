"""
Write a while loop that allows users to enter an album’s artist and title.
"""


def make_album(name, album):
    """Create a music dictionary based on user inputs."""
    music_album = {
        'name': name.title(),
        'album': album.title(),
    }
    return music_album


while True:
    print("\n(Enter 'q' any time to exit)")
    names = input('Artist name: ')
    if names == 'q':
        print('Disconnected!')
        break
    albums = input('Album name: ')
    if albums == 'q':
        print('Disconnected!')
        break
    print('\nDictionary created!')
    print(f"{make_album(names.title(), albums.title())}")
