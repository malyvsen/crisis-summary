from typing import List, Tuple

import openai
from crisis.feed import Feed


def prompt(
    feed: Feed,
    question: str,
    model: str = "curie",
    temperature=0.4,
    max_tokens: int = 32,
    n_most_important: int = 3,
) -> Tuple[str, List[str]]:
    docs = []
    for tweet in feed.tweets:
        text = tweet.title
        author = tweet.user
        formatted_time = tweet.time.strftime("At %H:%M on %d %b %Y")
        docs.append("{} user {} tweeted: {}".format(formatted_time, author, text))

    result = openai.Answer.create(
        model=model,
        question=question,
        documents=docs,
        temperature=temperature,
        examples_context="In 2017, U.S. life expectancy was 78.6 years.",
        examples=[["What is human life expectancy in the United States?", "78 years."]],
        max_rerank=20,
        stop=["\n", "<|endoftext|>"],
        max_tokens=max_tokens,
    )

    most_important = [
        x.text
        for x in sorted(result.selected_documents, key=lambda x: x.score, reverse=True)[
            :n_most_important
        ]
    ]
    return result.answers[0], most_important


Feed.prompt = prompt
