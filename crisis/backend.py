from dataclasses import dataclass
import openai

from crisis import RssSource, Feed, rss_sources


@dataclass
class GPT3Api:
    api_key: str
    engine: str
    temperature: float
    max_tokens: int

    def get_summarization(self, topic: str, question: str) -> str:
        openai.api_key = self.api_key

        rss_name_to_src = {r.name: r for r in rss_sources}

        feed = Feed.from_rss_source(rss_name_to_src[topic])

        print(feed.tweets)

        return "My answer is 42"
