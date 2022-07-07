# https://pytube.io/en/latest/ use PyTube

from pytube import YouTube

def download_song(url, destination):
    """ This function takes in the URL of a song from YouTube and downloads the MP3 version.
        It then and saves that song to the specified file location """
    pass

def get_metadata(url):
    """ This function takes in the URL of a song, and returns an object containing that song's metadata.
        i.e. Artist, Title, Album, Album Artwork """
    pass

def set_metadata(mp3_file, song_data):
    """ This function takes in the metadata of a song, and then edits the given MP3 file's metadata to reflect that """
    pass