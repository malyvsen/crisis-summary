from typing import List
from dataclasses import dataclass


@dataclass(frozen=True)
class RssSource:
    name: str
    urls: List[str]


rss_sources = [
    RssSource(
        name="Soufriere volcano eruption",
        urls=[
            "https://rss.app/feeds/wTXzZFTDgpaDTNTc.xml",
            "https://rss.app/feeds/7DOLMpGJzfmgZfiV.xml",
            "https://rss.app/feeds/fWR3QErjuI6IL95P.xml",
            "https://rss.app/feeds/0Y81bZMK48xt9Tzm.xml",
        ],
    ),
    RssSource(
        name="Cox's Bazar fire",
        urls=[
            "https://rss.app/feeds/jejLT0LsCi1cpjGa.xml",
            "https://rss.app/feeds/SWGqKhuZmCGocVUP.xml",
        ],
    ),
    RssSource(
        name="Coronavirus (mid-March 2020)",
        urls=[
            "https://rss.app/feeds/qvVNjfsNEqF1KJjR.xml",
        ],
    ),
]
