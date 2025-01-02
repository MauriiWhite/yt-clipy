import json

import yt_dlp

# from utils.types.video import VideoInfo

URL = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"

ydl_opts = {
    "quiet": True,
    "skip_download": True,
    "default_search": "ytsearch",
    "noplaylist": True,
    "format": "bestvideo[height<=1080][ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]",
    "merge_output_format": "mp4",
}

if __name__ == "__main__":
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        results = ydl.extract_info(URL, download=False)
        with open("video.json", "w") as f:
            json.dump(results, f, indent=4)

    # video_info = VideoInfo(**results)
    # print(video_info.model_dump())
