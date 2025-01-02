from typing import List

from yt_dlp import YoutubeDL

from utils.types import VideoSearchInfo


class VideoSearcher:
    def __init__(self, limit: int = 10):
        self.__limit = limit
        self.__options = {
            "quiet": True,
            "skip_download": True,
            "extract_flat": True,
            "default_search": "ytsearch",
            "noplaylist": True,
        }

    def search(self, query: str) -> List[VideoSearchInfo]:
        query = query.strip()
        if not query:
            print("Search query is empty.")
            return []

        try:
            with YoutubeDL(self.__options) as ydl:
                search_query = f"ytsearch{self.__limit}:{query}"
                results = ydl.extract_info(search_query, download=False)

            entries = results.get("entries", [])
            if not entries:
                print("No entries found for the query.")
                return []

            videos = [VideoSearchInfo(**entry) for entry in entries]
            print(f"Found {len(videos)} videos for the query: '{query}'")
            return videos

        except Exception as e:
            print(f"An error occurred while searching: {e}")
            return []


if __name__ == "__main__":
    searcher = VideoSearcher(limit=5)
    query = input("Enter a search query: ").strip()
    videos = searcher.search(query)

    if videos:
        print("Videos found:")
        for idx, video in enumerate(videos, start=1):
            print(f"{idx}. {video.title} - {video.url}")
