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
        docs.append(
            "{} user **@{}** tweeted: *{}*".format(formatted_time, author, text)
        )

    result = openai.Answer.create(
        model=model,
        question=question,
        documents=docs,
        temperature=temperature,
        examples_context="Air travel is suspended due to #HurricaneIrma - so that's that for my vacation in #Bermuda next week",
        examples=[
            ["What hurricane is affecting Bermuda?", "Hurricane Irma.\n"],
            ["Where is the hurricane?", "In Bermuda.\n"],
            ["Is air traffic open?", "No.\n"],
            ["How many people were killed?", "I don't know.\n"],
        ],
        max_rerank=n_most_important,
        stop=["\n", "<|endoftext|>"],
        max_tokens=max_tokens,
    )

    most_important = [x.text for x in result.selected_documents]
    return result.answers[0], most_important


Feed.prompt = prompt
