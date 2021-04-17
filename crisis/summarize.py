import os
from typing import List
import openai
from crisis.tweet import Tweet


openai.api_key = os.getenv("GPT3_KEY")


def summarize(tweets: List[Tweet]) -> str:
    """Summarize multiple tweets"""
    raise NotImplementedError()
