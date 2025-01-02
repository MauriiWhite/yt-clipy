from search import VideoSearcher

if __name__ == "__main__":
    searcher = VideoSearcher(limit=5)
    query = input("Enter a search query: ").strip()
    videos = searcher.search(query)

    if videos:
        print("Videos found:")
        for idx, video in enumerate(videos, start=1):
            print(f"{idx}. {video.title} - {video.url}")
