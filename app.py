from flask import Flask, render_template, request, send_file
from pytubefix import YouTube
import os

app = Flask(__name__)

DOWNLOADS_DIR = "downloads"
os.makedirs(DOWNLOADS_DIR, exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        url = request.form.get("url")
        try:
            yt = YouTube(url)
            stream = yt.streams.get_highest_resolution()
            filepath = stream.download(DOWNLOADS_DIR)
            return send_file(filepath, as_attachment=True)
        except Exception as e:
            return f"Error: {e}"
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
