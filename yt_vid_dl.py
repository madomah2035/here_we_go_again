import os
from pytube import YouTube


# Function to create a folder on desktop if it doesn't exist
def create_folder():
    folder_path = os.path.expanduser("~/Desktop/YT_videos")
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    return folder_path


# Function to download YouTube video
def download_video(url, folder_path):
    try:
        yt = YouTube(url)
        video = yt.streams.get_highest_resolution()
        video.download(folder_path)
        print("Video downloaded successfully!")
    except Exception as e:
        print("Error:", str(e))


# Get YouTube video URL from user
video_url = input("Enter the YouTube video URL: ")

# Create the folder on desktop
folder = create_folder()

# Download the video
download_video(video_url, folder)
