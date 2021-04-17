import openai
from crisis.feed import Feed


def summarize(feed: Feed) -> str:
    raise NotImplementedError()


Feed.summarize = summarize
