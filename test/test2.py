import json

import yt_dlp

URL = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"

INTER = False


class MyLogger:
    def debug(self, msg):
        if msg.startswith("[debug] "):
            print
        else:
            self.info(msg)

    def info(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        print(msg)


def my_hook(d):

    global INTER

    if d["status"] == "finished":
        if not INTER:
            INTER = True

            # print(d["status"])

            print(json.dumps(d["info_dict"], indent=2))

            # print(d["filename"])
            # print(d["downloaded_bytes"])
            # print(d["total_bytes"])
            # print(d["elapsed"])
            # print(d["speed"])


ydl_opts = {
    "logger": MyLogger(),
    "progress_hooks": [my_hook],
}


if __name__ == "__main__":
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.extract_info(URL, download=False)
