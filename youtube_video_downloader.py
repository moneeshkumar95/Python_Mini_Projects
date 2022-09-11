"""
Simple YouTube Video Downloader

Requirements -> pytube
"""

from pytube import YouTube
from pytube.exceptions import RegexMatchError


def youtube_video_downloader(link: str) -> None:
    """
    Function to download YouTube video

    :parm: String data
    :return: None
    """
    try:
        yt: YouTube = YouTube(link)
        yd: YouTube.streams = yt.streams.get_audio_only()
        yd.download()
    except RegexMatchError:
        print('Given URL is not YouTube, Please try again')


if __name__ == '__main__':
    ip: str = input("Please enter the YouTube URL: ")
    youtube_video_downloader(ip)
