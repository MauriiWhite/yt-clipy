import yt_dlp

from os import system


def search_songs(query, max_results=5):
    ydl_opts = {
        "quiet": True,
        "skip_download": True,
        "format": "bestaudio/best",
        "default_search": "ytsearch",
        "noplaylist": True,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        result = ydl.extract_info(f"ytsearch{max_results}:{query}", download=False)

    songs = []
    if "entries" in result:
        for entry in result["entries"]:
            songs.append(
                {
                    "title": entry["title"],
                    "url": entry["webpage_url"],
                    "duration": entry["duration"],
                }
            )

    return songs


def download_song(url):
    ydl_opts = {
        "format": "bestvideo[height<=1080][ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]",
        "merge_output_format": "mp4",
        "outtmpl": "downloads/%(title)s.%(ext)s",
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])


if __name__ == "__main__":
    while True:
        search_query = input("Enter the song you want to search: ")
        max_results = int(input("Enter the number of results you want: ") or 5)

        print("Searching for songs...")
        songs = search_songs(search_query, max_results)

        if not songs:
            print("No songs found.")
        else:
            print("Songs found:")
            for index, song in enumerate(songs, start=1):
                print(f"{index}. {song['title']} ({song['duration']})")

            choices = input("Enter the song number you want to download: ")
            selected_song = songs[int(choices) - 1]

            print(f"Downloading {selected_song['title']}...")

            download_song(selected_song["url"])
            print("Download complete.")

            system("pause")
            system("cls")
