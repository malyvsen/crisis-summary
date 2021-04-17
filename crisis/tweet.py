from dataclasses import dataclass
from datetime import datetime
from bs4 import BeautifulSoup


@dataclass(frozen=True)
class Tweet:
    title: str
    description: str
    user: str
    time: datetime

    @classmethod
    def from_rss(cls, rss_item: dict):
        description_soup = BeautifulSoup(rss_item["description"], "html.parser")
        return cls(
            title=rss_item["title"],
            description=(
                description_soup.p.text
                if description_soup.p is not None
                else description_soup.text
            ),
            user=rss_item["dc:creator"],
            time=datetime.strptime(rss_item["pubDate"], "%a, %d %b %Y %H:%M:%S %Z"),
        )
