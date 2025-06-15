# This script allows you to download YouTube videos or playlists using the yt-dlp library.
# It provides options to download a single video or an entire playlist.
# The downloaded files are saved in the specified download directory.
import os
from yt_dlp import YoutubeDL

# Constants – Set your default download directory
DOWNLOAD_DIR = "path/to/your/download/directory"  # Change this to your desired download directory


if not os.path.exists(DOWNLOAD_DIR):
    os.makedirs(DOWNLOAD_DIR)  # Create the directory if it doesn't exist


# Options for yt-dlp

YDL_OPTIONS = {
    'outtmpl': os.path.join(DOWNLOAD_DIR, '%(title)s.%(ext)s'),  # Output file format
    'format': 'best',  # Best available format with audio and video
    'merge_output_format': 'mp4',  # Merge output into MP4 (optional)
    'noplaylist': True,  # Avoid playlists unless explicitly downloading them
    'quiet': False,  # Show progress in the console
    'concurrent_fragments': 5,  # Multithreaded fragment downloads
    'http_chunk_size': 16 * 1024 * 1024,  #
    'no_warnings': True,  # Suppress warnings
}


def download_video(video_url):
    """
    Downloads a single video using yt-dlp.
    """
    try:
        print(f"Downloading video: {video_url}")
        # Create a YoutubeDL object with the specified options
        with YoutubeDL(YDL_OPTIONS) as ydl:
            ydl.download([video_url])
        print(f"Downloaded video successfully: {video_url}")
    except Exception as e:
        print(f"Error downloading video: {video_url}")
        print(str(e))


def download_playlist(playlist_url):
    """
    Downloads all videos from a playlist using yt-dlp.
    """
    try:
        print(f"Downloading playlist: {playlist_url}")
        # Update options for playlist support
        playlist_options = YDL_OPTIONS.copy()
        playlist_options['noplaylist'] = False  # Allow playlists

        # Create a YoutubeDL object with updated options
        with YoutubeDL(playlist_options) as ydl:
            ydl.download([playlist_url])
        print(f"Downloaded playlist successfully: {playlist_url}")
    except Exception as e:
        print(f"Error downloading playlist: {playlist_url}")
        print(str(e))


if __name__ == "__main__":
    print("YouTube Video and Playlist Downloader (yt-dlp)")
    print("===============================================")
    print("Options:")
    print("1. Download a single video")
    print("2. Download an entire playlist")

    choice = input("Enter your choice (1 or 2): ").strip()

    if choice == '1':
        video_url = input("Enter the YouTube video URL: ").strip()
        download_video(video_url)
    elif choice == '2':
        playlist_url = input("Enter the YouTube playlist URL: ").strip()
        download_playlist(playlist_url)
    else:
        print("Invalid choice. Please run the script again.")
