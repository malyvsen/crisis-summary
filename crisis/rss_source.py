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
]
