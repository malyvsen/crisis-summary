from crisis import Feed, rss_sources

def test_summarize():
    feed = Feed.from_rss_source(rss_sources[0])
    question = "How can I help?"
    answer, most_important = feed.prompt(question)
    print("Anwer to the question {} :  {}".format(question, answer))
    print("Based on the following tweets: ")
    for tweet in most_important:
        print(tweet)
        print("---------------")

test_summarize()