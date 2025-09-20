YouTube Downloader Web App

A simple web app built with Python and Flask that allows users to download YouTube videos at the highest resolution. Users can enter a YouTube URL, and the app will automatically download the best video and audio streams, merge them, and send the final video to the browser. The app runs locally on your computer.

Features:
- Enter a YouTube URL and download the video
- Automatically downloads and merges the best video-only and best audio streams
- Runs locally on your PC

Requirements:
- Python 3.8 or higher
- Python packages: flask, pytubefix
- ffmpeg installed and added to your system PATH

Installation:
1. Clone the repository:
git clone https://github.com/generalpooria/youtube-downloader.git

2. Install dependencies:
pip install -r requirements.txt
Or manually install flask and pytubefix.
3. Make sure ffmpeg is installed and accessible from your terminal or command prompt.

Usage:
1. Run the Flask server:
python app.py

2. Open your browser and go to:
http://127.0.0.1:5000
3. Paste a YouTube URL and click Download. The video will be saved in the downloads folder and sent to your browser.

Folder structure:
youtube-downloader/
├─ app.py           # Flask backend
├─ requirements.txt # Python packages
├─ downloads/       # Temporary video storage
└─ templates/
   └─ index.html    # HTML page for user input

Notes:
- For local and personal use only
- Downloading videos may violate YouTube's Terms of Service if used publicly
- Highest resolution videos may take longer to download and merge

License:
Free to use and redistribute.
