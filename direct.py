import os

def getSonglist():
    songList = []
    with os.scandir('songs/') as entries:
        for entry in entries:
            songList.append(entry.name)
    return songList