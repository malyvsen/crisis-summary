from crisis import Feed, rss_sources

def test_summarize():
    feed = Feed.from_rss_source(rss_sources[0])
    answer, most_important = feed.summarize()
    print("Summary of what happened:", answer)
    print("Based on the following tweets: ")
    for tweet in most_important:
        print(tweet)
        print("---------------")

test_summarize()