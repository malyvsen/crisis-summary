from datetime import datetime
from crisis import Feed, Tweet


def test_from_url():
    feed = Feed.from_rss_url("https://rss.app/feeds/wTXzZFTDgpaDTNTc.xml")
    assert len(feed.tweets) > 0


def test_union():
    hi = Tweet(
        title="Hi!", description="", user="programmer", time=datetime(2020, 12, 3)
    )
    hello = Tweet(
        title="Hello!", description="", user="programmer", time=datetime(2020, 12, 2)
    )
    cow = Tweet(title="Hi!", description="", user="cow", time=datetime(2020, 12, 1))
    assert Feed.union(Feed(tweets=[hi, hello]), Feed(tweets=[hi, cow])) == Feed(
        tweets=[hi, hello, cow]
    )
