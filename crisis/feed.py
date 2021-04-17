from typing import List
from dataclasses import dataclass
import requests
import xmltodict
from crisis.tweet import Tweet


@dataclass(frozen=True)
class Feed:
    tweets: List[Tweet]

    @classmethod
    def from_rss_url(cls, url: str):
        return cls.from_rss(requests.get(url).text)

    @classmethod
    def from_rss(cls, rss_text: str):
        return cls(
            tweets=[
                Tweet.from_rss(item)
                for item in xmltodict.parse(rss_text)["rss"]["channel"]["item"]
            ]
        )

    @classmethod
    def union(cls, *feeds):
        return cls(
            tweets=sorted(
                set.union(*[set(feed.tweets) for feed in feeds]),
                key=lambda tweet: tweet.time,
                reverse=True,
            )
        )
