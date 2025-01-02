# from search import VideoSearcher

# if __name__ == "__main__":
#     searcher = VideoSearcher(limit=5)
#     query = input("Enter a search query: ").strip()
#     videos = searcher.search(query)

#     if videos:
#         print("Videos found:")
#         for idx, video in enumerate(videos, start=1):
#             print(f"{idx}. {video.title} - {video.url}")

from textual.app import App, ComposeResult
from textual.screen import Screen
from textual.widgets import Header, Input


class SearchScreen(Screen):
    def compose(self) -> ComposeResult:
        yield Header(name="YTClipy", show_clock=True, time_format="%H:%M")
        yield Input(placeholder="Search for YouTube videos")


class YTClipy(App):
    def on_ready(self) -> None:
        self.push_screen(SearchScreen())


if __name__ == "__main__":
    app = YTClipy()
    app.run()
