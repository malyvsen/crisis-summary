import openai
from crisis.feed import Feed


def summarize(feed: Feed) -> str:
    docs = []
    for tweet in feed.tweets:
        text = tweet.title
        author = tweet.user
        formatted_time = tweet.time.strftime("At %H:%M on %d %b %Y")
        docs.append("{} user {} tweeted: {}".format(formatted_time, author, text))
    
    result = openai.Answer.create(
        model="curie",
        question="Describe in details what happened", 
        documents=docs,
        temperature=0.4,
        examples_context="In 2017, U.S. life expectancy was 78.6 years.", 
        examples=[["What is human life expectancy in the United States?", "78 years."]],
        max_rerank=20,
        stop=["\n", "<|endoftext|>"],
        max_tokens=64,
    )

    most_important = [x.text for x in sorted(result.selected_documents, key=lambda x: x.score, reverse=True)[:3]]
    return result.answers[0], most_important


Feed.summarize = summarize
