from dataclasses import dataclass
from datetime import datetime
from bs4 import BeautifulSoup


@dataclass
class Tweet:
    title: str
    description: str
    user: str
    time: datetime

    @classmethod
    def from_rss(cls, rss_item: dict):
        return cls(
            title=rss_item["title"],
            description=BeautifulSoup(rss_item["description"], "html.parser").p.text,
            user=rss_item["dc:creator"],
            time=datetime.strptime(rss_item["pubDate"], "%a, %d %b %Y %H:%M:%S %Z"),
        )
